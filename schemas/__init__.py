from datetime import datetime
from typing import List
from pydantic import BaseModel


class News(BaseModel):
    id: int = None
    url: str
    title: str
    thumbnail_url: str = None
    local_id: str
    description: str
    publish_date: datetime
    tags: List[str]

    class Config:
        orm_mode = True


class Share(BaseModel):
    news_id: str
    channel: str

    class Config:
        orm_mode = True
