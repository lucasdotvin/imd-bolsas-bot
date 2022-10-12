from datetime import datetime
import requests_html
from schemas import News


def parse_raw_news_data(raw_news_data: dict) -> News:
    local_id = raw_news_data['id']
    title = raw_news_data['title']['rendered']
    url = raw_news_data['link']

    publish_date = datetime.strptime(raw_news_data['date'], '%Y-%m-%dT%H:%M:%S')

    thumbnail_url = _get_image(raw_news_data)
    description = _parse_raw_description(raw_news_data)

    news = News(url=url,
                title=title,
                thumbnail_url=thumbnail_url,
                local_id=local_id,
                description=description,
                publish_date=publish_date,
                tags=['Editais'])

    return news


def _parse_raw_description(raw_news_data: dict) -> str:
    parsed_markup = requests_html.HTML(html=raw_news_data['content']['rendered'])
    description = parsed_markup.text
    
    return description


def _get_image(raw_news_data: dict) -> str:
    images = raw_news_data['yoast_head_json']['og_image']

    if len(images):
        return images[0]['url']

    return ''
