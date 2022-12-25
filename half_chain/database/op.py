from typing import List
from . import session, engine
from .model import Comment
from sqlalchemy.exc import NoResultFound
from sqlalchemy.inspection import inspect

def add_comment(text:str):
    session.add(Comment(text))
    session.commit()

def query_comment(cid:int)->str:
    try:
        return session.query(Comment).filter_by(id=cid).one().content
    except NoResultFound:
        return None

def query_ids()->List[str]:
    return [ i[0] for i in session.query(Comment.id).all() ]

def update_comment(cid:int, user_input:str):
    engine.connect().execute(f"update {Comment.__tablename__} set content = \"{user_input}\" where id = {cid}")
