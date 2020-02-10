# -*- coding: utf-8 -*-

BOT_NAME = 'imd_bolsas_bot'

SPIDER_MODULES = ['imd_bolsas_bot.spiders']
NEWSPIDER_MODULE = 'imd_bolsas_bot.spiders'

ITEM_PIPELINES = {
    'imd_bolsas_bot.exporters.PerIDJSONExportPipeline': 1000
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
