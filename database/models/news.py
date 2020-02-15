from sqlalchemy import *
from database.base import Base


class News(Base):
    __tablename__ = 'news'

    id = Column(Integer, primary_key=True)
    url = Column(String, nullable=False)
    title = Column(String, nullable=False)
    summary = Column(String, nullable=False)
    author = Column(String, nullable=False)
    published_at = Column(Date, nullable=True)
    tags = Column(String, nullable=False)
    processed_at = Column(DateTime, nullable=True)
