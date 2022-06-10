import os
import requests_html


async def get_base_news_page(session: requests_html.AsyncHTMLSession) -> requests_html.HTML:
    request_url = '/'.join([os.getenv('IMD_BASE_URL'), 'portal/noticias'])
    request = await session.get(request_url)

    return request.html


def get_news_urls_from_base(base_page: requests_html.HTML) -> set:
    news_boxes = base_page.find('.card.card-noticia')
    news_urls = {box.links.pop() for box in news_boxes}

    return news_urls
