import os
import tempfile
import requests
import tweepy

import templates_handler
from schemas import News


auth = tweepy.OAuthHandler(os.getenv('TWITTER_API_KEY'), os.getenv('TWITTER_API_SECRET'))
auth.set_access_token(os.getenv('TWITTER_ACCESS_TOKEN'), os.getenv('TWITTER_ACCESS_TOKEN_SECRET'))
api = tweepy.API(auth)

client = tweepy.Client(consumer_key=os.getenv('TWITTER_API_KEY'),
                       consumer_secret=os.getenv('TWITTER_API_SECRET'),
                       bearer_token=os.getenv('TWITTER_BEARER_TOKEN'),
                       access_token=os.getenv('TWITTER_ACCESS_TOKEN'),
                       access_token_secret=os.getenv('TWITTER_ACCESS_TOKEN_SECRET'))


def share_news(news: News):
    post_template = templates_handler.environment.get_template('twitter-post.html.jinja')
    post_text = post_template.render(news.dict())

    media_ids = None

    if news.thumbnail_url:
        media_ids = [_upload_thumbnail(news)]

    client.create_tweet(text=post_text, media_ids=media_ids)


def _upload_thumbnail(news: News) -> str:
    thumbnail_file_path = _download_thumbnail(news)
    media = api.media_upload(thumbnail_file_path)

    return media.media_id


def _download_thumbnail(news: News) -> str:
    with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as file:
        file.write(requests.get(news.thumbnail_url).content)

    file_path = file.name

    return file_path
