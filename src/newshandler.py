import json
import os
from hashlib import md5


class NewsHandler(object):
    def load_collected_news(self):
        news = {}
        news_tree = os.walk('results')
        for root, _, files in news_tree:
            for file_name in files:
                file_path = os.path.join(root, file_name)
                with open(file_path, 'rb') as file_handler:
                    file_content = file_handler.read()
                    file_hash = md5(file_content).hexdigest()

                    news[file_hash] = file_path

        self.collected_news = news


    def load_published_news(self):
        news = {}
        file_path = 'published-news.json'
        if os.path.exists(file_path):
            with open(file_path, 'r') as file_handler:
                news = json.load(file_handler)

        self.published_news = news


    def get_unpublished_news(self):
        unpublished_news_set = set(self.collected_news)
        unpublished_news_set -= set(self.published_news)

        unpublished_news_dict = {key: self.collected_news[key]
                                 for key in unpublished_news_set}

        return unpublished_news_dict


    def get_news_data(self, news_hash):
        file_path = self.collected_news[news_hash]
        with open(file_path, 'r') as file_handler:
            news_data = json.load(file_handler)
            news_data = news_data[0]

        return news_data


    def save_unpublished_news(self):
        file_path = 'published-news.json'
        with open(file_path, 'w') as file_handler:
            json.dump(self.collected_news, file_handler)
