import datetime

from .base import Base
from sqlalchemy import Column, Integer, String, Text, DateTime

MAX_TITLE_LENGTH = 80

class Post(Base):
    __tablename__ = 'post'

    id = Column(Integer, autoincrement=True, primary_key=True)
    title = Column(String(MAX_TITLE_LENGTH))
    body = Column(Text)

    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    edited_at = Column(DateTime, default=None, onupdate=datetime.datetime.utcnow)

    def __repr__(self):
        return '<Post {}: {}>'.format(self.id, self.title)