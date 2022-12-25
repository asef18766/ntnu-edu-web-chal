from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
SQLALCHEMY_DATABASE_URL = "sqlite:///save.db"
engine = create_engine(
    f"{SQLALCHEMY_DATABASE_URL}?check_same_thread=False", echo=True
)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
session = Session()