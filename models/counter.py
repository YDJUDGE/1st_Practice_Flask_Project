from sqlalchemy import Column, Integer, ForeignKey
from models import db

class ViewCount(db.Model):
    id = Column(Integer, primary_key=True)
    count = Column(Integer, default=0)
    view_count = Column(Integer, ForeignKey("post.id"))

    def plus_count(self):
        self.count += 1
        db.session.commit()


