import database as db


class DBExporterPipeline(object):
    def open_spider(self, spider):
        self._session = db.Session()


    def close_spider(self, spider):
        self._session.commit()


    def process_item(self, item, spider):
        news = db.News(
            id=item['id'],
            url=item['url'],
            title=item['title'],
            summary=item['summary'],
            author=item['author'],
            published_at=item['date'],
            tags=', '.join(item['tags'])
        )

        self._session.add(news)

        return item
