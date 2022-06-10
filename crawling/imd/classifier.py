import os
from schemas import News


def check_if_news_matches_criterion(news: News) -> bool:
    wanted_tags = os.getenv('WANTED_TAGS').split(',')

    for tag in wanted_tags:
        if tag in news.tags:
            return True

        if tag in news.title.lower():
            return True

        if tag in news.description.lower():
            return True

    return False
