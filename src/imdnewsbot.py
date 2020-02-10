from src.newshandler import NewsHandler
from src.templatehandler import TemplateHandler

from telegram.ext import Updater


class IMDNewsBot(object):
    def __init__(self, channel_id, telegram_token):
        super(IMDNewsBot, self).__init__()
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
        news_handler.load_collected_news()
        news_handler.load_published_news()

        unpublished_news = news_handler.get_unpublished_news()
        for news_hash in unpublished_news:
            news_data = news_handler.get_news_data(news_hash)

            message_template = TemplateHandler('message')
            message = message_template.render(news_data)
            self._send_to_channel(message)

        news_handler.save_unpublished_news()
