import asyncio
from typing import List
import requests_html

from schemas import News

from . import base_page, classifier, news_page


async def retrieve_news() -> List[News]:
    session = requests_html.AsyncHTMLSession()

    base_news_page = await base_page.get_base_news_page(session)
    news_urls = base_page.get_news_urls_from_base(base_news_page)

    news_pages = await asyncio.gather(*(news_page.get_news_page(url, session) for url in news_urls))
    news_data = [news_page.parse_news_page(page) for page in news_pages]

    wanted_news = [news for news in news_data if classifier.check_if_news_matches_criterion(news)]

    return wanted_news
