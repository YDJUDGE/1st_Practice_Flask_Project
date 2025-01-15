from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .database import db

class Post(db.Model):
    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False, unique=False)
    description = Column(String(250), nullable=False, default="Описания пока нет")

    c = relationship("ViewCount", backref="post", uselist=False)
    comments = relationship("Comment", back_populates="post_for_comment", lazy='dynamic')

    def __repr__(self):
        return f"{self.__class__.__name__}(id{self.id}, Заголовок={self.title}, Описание={self.description})"

