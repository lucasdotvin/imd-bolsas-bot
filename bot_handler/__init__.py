from news_handler import NewsHandler
from templates_handler import TemplateHandler

from telegram.ext import Updater


class BotHandler(object):
    def __init__(self, channel_id, telegram_token):
        super(BotHandler, self).__init__()
        self.channel_id = channel_id
        self.telegram_token = telegram_token


    def _start_bot(self):
        self._updater = Updater(
            token=self.telegram_token,
            use_context=True
        )

        self._dispatcher = self._updater.dispatcher


    def _send_to_channel(self, message):
        self._dispatcher.bot.send_message(
            chat_id=self.channel_id,
            text=message,
            parse_mode='HTML'
        )


    def run(self):
        self._start_bot()

        news_handler = NewsHandler()
        unpublished_news = news_handler.get_unpublished_news()
        for news in unpublished_news:
            news_data = news.__dict__

            print(news_data['published_at'])
            print(type(news_data['published_at']))

            message_template = TemplateHandler('message')
            message = message_template.render(news_data)
            self._send_to_channel(message)

        news_handler.save_unpublished_news()
