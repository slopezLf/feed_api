import datetime
from .base import Base
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref

MAX_TITLE_LENGTH = 80

class Comment(Base):
    __tablename__ = 'comment'

    id = Column(Integer, autoincrement=True, primary_key=True)
    post_id = Column(Integer, ForeignKey('post.id'))
    body = Column(Text)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    post = relationship("Post", back_populates="comments", foreign_keys=[post_id])

    def __repr__(self):
        return '<Comment: {} for Post{}>'.format(self.id, self.post.id)

