from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

database_url = "sqlite:///photos.db"

engine = create_engine(database_url, echo=True)

base = declarative_base()

#make to class with tablename and columns
class Photo(base):
    __tablename__ = 'photos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    photo_file_name = Column(String, nullable=False)
