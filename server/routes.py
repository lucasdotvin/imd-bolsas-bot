import os
import schemas
from crawling import imd
from database.models import News, NewsShare
from fastapi import APIRouter, Depends, HTTPException
from fastapi_sqlalchemy import db
from integrations import jerimum
from sharing import telegram, twitter
from server import auth

RETRIEVING_MODULES = {'imd': imd, 'jerimum': jerimum}
SHARING_MODULES = {'telegram': telegram, 'twitter': twitter}

router = APIRouter()


@router.get('/health')
async def health():
    return {'status': 'ok'}


@router.get('/health/auth', dependencies=[Depends(auth.check_api_key)])
async def health():
    return {'status': 'ok'}


@router.get('/retrievers')
async def retrievers():
    available_retrievers = list(RETRIEVING_MODULES.keys())

    return {'data': available_retrievers}


@router.get('/sharers')
async def sharers():
    available_sharers = list(SHARING_MODULES.keys())

    return {'data': available_sharers}


@router.get('/retrieve', dependencies=[Depends(auth.check_api_key)])
async def retrieve(retriever: str):
    if retriever not in RETRIEVING_MODULES:
        raise HTTPException(status_code=404, detail='Retriever not found')

    retriever_module = RETRIEVING_MODULES[retriever]
    news_data = await retriever_module.retrieve_news()

    already_retrieved_news = db.session.query(News)\
        .filter(News.local_id.in_([news.local_id for news in news_data]))\
        .filter(News.source == retriever)\
        .values(News.local_id)

    already_retrieved_news = [news.local_id for news in already_retrieved_news]

    unprecedented_news = [news for news in news_data if news.local_id not in already_retrieved_news]

    for news in unprecedented_news:
        news_model = News(**news.dict())
        news_model.source = retriever
        db.session.add(news_model)

    db.session.commit()

    return {'data': unprecedented_news}


@router.get('/share', dependencies=[Depends(auth.check_api_key)])
async def share(channel: str):
    if channel not in SHARING_MODULES:
        raise HTTPException(status_code=404, detail='Channel not found')

    not_shared_news = db.session.query(News)\
        .filter(~News.shares.any(NewsShare.channel == channel))\
        .limit(os.getenv('POSTS_PER_RUN'))\
        .all()

    sharer_module = SHARING_MODULES[channel]
    formatted_news = [schemas.News.from_orm(news) for news in not_shared_news]

    for news in formatted_news:
        sharer_module.share_news(news)

        db.session.add(NewsShare(news_id=news.id, channel=channel))
        db.session.commit()

    return {'data': formatted_news}
