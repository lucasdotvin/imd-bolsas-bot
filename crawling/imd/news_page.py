from datetime import datetime
import os
import requests_html

from schemas import News


async def get_news_page(url: str, session: requests_html.AsyncHTMLSession) -> requests_html.HTML:
    request_url = '/'.join([os.getenv('IMD_BASE_URL'), url])
    request = await session.get(request_url)

    return request.html


def parse_news_page(page: requests_html.HTML) -> News:
    url = page.xpath('//meta[@property="og:url"]/@content', first=True)
    title = page.xpath('//meta[@property="og:title"]/@content', first=True)
    thumbnail_url = page.xpath('//meta[@property="og:image"]/@content', first=True)
    local_id = url.split('/')[-1]
    description = page.find('div.titulo-principal > h5', first=True).text
    tags = [badge.text for badge in page.find('span.badge.card-tags')]
    publish_date = _get_publish_date(page)

    news = News(url=url,
                title=title,
                thumbnail_url=thumbnail_url,
                local_id=local_id,
                description=description,
                publish_date=publish_date,
                tags=tags)

    return news


def _get_publish_date(page: requests_html.HTML) -> datetime:
    publish_date = page.xpath('//meta[@property="article:published_time"]/@content', first=True)
    publish_date = publish_date.split(' ')[0]
    publish_date = datetime.strptime(publish_date, '%Y-%m-%d')

    return publish_date
