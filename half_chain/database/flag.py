from sqlalchemy import Column, Integer, String
from . import Base, engine, session

class Flag(Base):
    __tablename__ = 's3cret_tbl'
    id = Column(Integer, primary_key=True, autoincrement=True)
    content = Column(String(48763))

    def __init__(self, comment:str):
        self.content = comment

    def __repr__(self):
        return f"<{self.id}:{self.content}>"

Base.metadata.create_all(engine, checkfirst=True)
session.add(Flag("flag{test_flag}"))
session.commit()