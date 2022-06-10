from datetime import datetime
import requests_html
import os
from schemas import News


def parse_raw_news_data(raw_news_data: dict) -> News:
    local_id = raw_news_data['id']
    title = raw_news_data['titulo']
    description = raw_news_data['descricao']
    publish_date = datetime.strptime(raw_news_data['data_abertura'], '%Y-%m-%d')

    url = _build_url(local_id)
    description = _parse_raw_description(raw_news_data)
    tags = _get_tags(raw_news_data)

    news = News(url=url,
                title=title,
                thumbnail_url=None,
                local_id=local_id,
                description=description,
                publish_date=publish_date,
                tags=tags)

    return news


def _get_tags(raw_news_data: dict) -> str:
    news_areas = raw_news_data['areaAtuacao']
    news_tags = [area['descricao'] for area in news_areas]

    return news_tags


def _build_url(id: str) -> str:
    base_url = os.getenv('JERIMUM_BASE_URL')
    news_url = '/'.join([base_url, 'jerimumjobs/oportunidade', repr(id)])
    
    return news_url


def _parse_raw_description(raw_news_data: dict) -> str:
    parsed_markup = requests_html.HTML(html=raw_news_data['descricao'])
    description = parsed_markup.text
    
    return description
