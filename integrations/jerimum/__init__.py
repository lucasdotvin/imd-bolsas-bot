import re
import requests
import os
from typing import List

from schemas import News

from . import raw_news


async def retrieve_news() -> List[News]:
    raw_news_data = _get_raw_news_data()
    news_data = [raw_news.parse_raw_news_data(raw_data) for raw_data in raw_news_data]

    return news_data


def _get_raw_news_data() -> list:
    request_url = '/'.join([os.getenv('JERIMUM_BASE_URL'), 'jerimumjobs/oportunidade/listarJSON/1'])
    request = requests.get(request_url)

    return request.json()
