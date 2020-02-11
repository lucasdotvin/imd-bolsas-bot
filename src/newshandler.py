from datetime import datetime

import database as db


class NewsHandler(object):
    def __init__(self):
        self._session = db.Session()


    def get_unpublished_news(self):
        unpublished_news = self._session.query(
            db.News
        ).filter_by(
            processed_at=None
        ).all()

        return unpublished_news


    def save_unpublished_news(self):
        unpublished_news = self._session.query(
            db.News
        ).filter_by(
            processed_at=None
        ).update({
            'processed_at': datetime.now()
        })

        self._session.commit()
