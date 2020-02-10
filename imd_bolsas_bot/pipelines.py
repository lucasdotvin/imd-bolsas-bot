import os

from scrapy.exceptions import DropItem

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
