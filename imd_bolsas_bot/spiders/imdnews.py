# -*- coding: utf-8 -*-
import re
import scrapy


class IMDNews(scrapy.Spider):
    name = 'imdnews'
    start_urls = ['https://www.imd.ufrn.br/portal/noticias']


    def get_news_title(self, news_box):
        TITLE_SELECTOR = 'h4.card-title ::text'
        return news_box.css(TITLE_SELECTOR).extract_first()


    def get_news_summary(self, news_box):
        SUMMARY_SELECTOR = 'p.card-text ::text'
        return news_box.css(SUMMARY_SELECTOR).extract_first()


    def get_news_author(self, news_box):
        AUTHOR_SELECTOR = 'div.card-date > a ::text'
        return news_box.css(AUTHOR_SELECTOR).extract_first()


    def get_news_date(self, news_box):
        DATE_SELECTOR = 'div.card-date > h6 ::text'
        date = news_box.css(DATE_SELECTOR).extract_first()
        date = date.strip(' por ')
        return date


    def get_news_tags(self, news_box):
        TAGS_SELECTOR = 'div.tags > h6 ::text'
        tags = news_box.css(TAGS_SELECTOR).extract_first()
        tags = tags.lower()
        tags = tags.split(' | ')

        return tags


    def extract_id_from_url(self, url):
        ID_REGULAR_EXPRESSION = r'\/\d+\/'
        id_ = re.search(ID_REGULAR_EXPRESSION, url)

        if id_:
            id_ = id_.group()
            id_ = id_.strip('/')
            id_ = int(id_)
        else:
            id_ = -1

        return id_


    def get_news_id(self, news_box):
        LINK_XPATH = 'a[@href != "#"]/@href'
        url = news_box.xpath(LINK_XPATH).extract_first()
        url = url.strip()
        id_ = self.extract_id_from_url(url)

        return id_


    def parse(self, response):
        NEWS_BOX_SELECTOR = '.col-xs-12.col-sm-3 .card-block.p-2'
        NEXT_PAGE_URL_XPATH = '''
            //a[contains(@title, "Próxima página")]/@href
        '''

        for news_box in response.css(NEWS_BOX_SELECTOR):
            yield {
                'id': self.get_news_id(news_box),
                'title': self.get_news_title(news_box),
                'summary': self.get_news_summary(news_box),
                'author': self.get_news_author(news_box),
                'date': self.get_news_date(news_box),
                'tags': self.get_news_tags(news_box)
            }
