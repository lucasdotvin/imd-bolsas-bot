import os
from datetime import datetime

from scrapy.exceptions import DropItem


class SanitizeDatePipeline(object):
    MONTH_NAME_TRANSLATION_TABLE = {
        'fev': 'feb',
        'abr': 'apr',
        'mai': 'may',
        'ago': 'aug',
        'set': 'sep',
        'out': 'oct',
        'dez': 'dec'
    }


    def _translate_month_name(self, item_date):
        for pt_month_name in self.MONTH_NAME_TRANSLATION_TABLE:
            en_month_name = self.MONTH_NAME_TRANSLATION_TABLE.get(
                pt_month_name
            )

            item_date = item_date.replace(pt_month_name, en_month_name)

        return item_date


    def process_item(self, item, spider):
        item['date'] = self._translate_month_name(item['date'])
        item['date'] = datetime.strptime(item['date'], r'%d %b %Y')
        return item


class WantedTagsFilterPipeline(object):
    def __init__(self):
        self._load_wanted_tags()


    def _load_wanted_tags(self):
        wanted_tags = os.getenv('NEWS_WANTED_TAGS')
        wanted_tags = wanted_tags.split(', ')
        wanted_tags = [tag.strip().lower()
                       for tag in wanted_tags]

        self._wanted_tags = wanted_tags


    def process_item(self, item, spider):
        item_tags = set(item['tags'])
        item_has_wanted_tags = item_tags & set(self._wanted_tags)

        if not item_has_wanted_tags:
            item_id = item['id']
            raise DropItem(
                f'Item does not contains wanted tags. ID: {item_id}'
            )

        return item
