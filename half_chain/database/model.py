from sqlalchemy import Column, Integer, String
from . import Base, engine

class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True, autoincrement=True)
    content = Column(String(48763))

    def __init__(self, comment:str):
        self.content = comment

    def __repr__(self):
        return f"<{self.id}:{self.content}>"

Base.metadata.create_all(engine, checkfirst=True)
