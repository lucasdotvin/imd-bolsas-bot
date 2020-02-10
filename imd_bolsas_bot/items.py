# -*- coding: utf-8 -*-

import scrapy


class QuotesbotItem(scrapy.Item):
    id = scrapy.Field()
    title = scrapy.Field()
    author = scrapy.Field()
    published_time = scrapy.Field()
    thumbnail = scrapy.Field()
    content = scrapy.Field()
    tags = scrapy.Field()
