from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .database import db
from datetime import datetime

class Comment(db.Model):
    id = Column(Integer, primary_key=True)
    body = Column(String(1500))
    data = Column(DateTime, default=datetime.utcnow())
    post_id = Column(Integer, ForeignKey("post.id"))

    post_for_comment = relationship('Post', back_populates='comments')

    def __repr__(self):
        return f"{self.__class__.__name__}, (id{self.id}, body={self.body}, data={self.data})"

