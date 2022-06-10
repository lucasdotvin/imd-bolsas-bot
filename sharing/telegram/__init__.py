import os
import tempfile
import requests
from telegram import Bot

import templates_handler
from schemas import News


bot = Bot(token=os.getenv('TELEGRAM_BOT_TOKEN'))


def share_news(news: News):
    template_data = _format_template_data(news)

    message_template = templates_handler.environment.get_template('telegram-message.html.jinja')
    message_text = message_template.render(template_data)

    if news.thumbnail_url:
        return _send_image(message_text, news)

    _send_plain_message(message_text, news)


def _send_image(message_text: str, news: News):
    thumbnail_path = _download_thumbnail(news)

    bot.send_photo(chat_id=os.getenv('TELEGRAM_CHANNEL_ID'),
                   photo=open(thumbnail_path, 'rb'),
                   caption=message_text,
                   parse_mode='HTML')


def _download_thumbnail(news: News) -> str:
    with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as file:
        file.write(requests.get(news.thumbnail_url).content)

    file_path = file.name

    return file_path


def _send_plain_message(message_text: str, news: News):
    bot.send_message(chat_id=os.getenv('TELEGRAM_CHANNEL_ID'), parse_mode='HTML', text=message_text)


def _format_template_data(news: News):
    template_data = news.dict()

    description_words = news.description.split(' ')
    truncated_description = ''

    while len(truncated_description) < 128 and len(description_words) > 0:
        truncated_description = ' '.join([truncated_description, description_words.pop(0)])

    if len(description_words):
        truncated_description += '...'

    template_data['description'] = truncated_description

    return template_data
