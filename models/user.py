from sqlalchemy import Column, Integer, String, Boolean
from .database import db

class User(db.Model):
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    is_author = Column(Boolean, nullable=False, server_default="FALSE", default=False)

    def __repr__(self):
        return f"{self.__class__.__name__} (id{self.id}, username={self.username!r})"
