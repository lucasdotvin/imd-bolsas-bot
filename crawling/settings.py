# -*- coding: utf-8 -*-

BOT_NAME = 'IMDBolsasBot'

SPIDER_MODULES = ['crawling.spiders']
NEWSPIDER_MODULE = 'crawling.spiders'

USER_AGENT = 'IMDBolsasBot (+https://t.me/imdbolsasbot)'

ITEM_PIPELINES = {
    'crawling.pipelines.DuplicateItemPipeline': 0,
    'crawling.pipelines.SanitizeDatePipeline': 1,
    'crawling.pipelines.WantedTagsFilterPipeline': 2,
    'crawling.exporters.DBExporterPipeline': 3
}

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
'''
HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 0
HTTPCACHE_DIR = 'httpcache'
HTTPCACHE_IGNORE_HTTP_CODES = []
HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
'''
