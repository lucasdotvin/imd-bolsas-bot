from sqlalchemy import Column, DateTime, Integer, JSON, Text, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


Base = declarative_base()


class News(Base):
    __tablename__ = 'news'
    id = Column(Integer, primary_key=True)
    url = Column(String)
    title = Column(String)
    thumbnail_url = Column(String, nullable=True)
    local_id = Column(String)
    description = Column(Text)
    publish_date = Column(DateTime)
    tags = Column(JSON)
    source = Column(String)
    created_time = Column(DateTime, server_default=func.now())
    updated_time = Column(DateTime, server_default=func.now())

    shares = relationship('NewsShare', back_populates='news')


class NewsShare(Base):
    __tablename__ = 'news_shares'
    news_id = Column(Integer, ForeignKey('news.id'), primary_key=True)
    channel = Column(String, primary_key=True)
    created_time = Column(DateTime, server_default=func.now())

    news = relationship('News')
