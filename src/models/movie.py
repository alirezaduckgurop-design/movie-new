#Project:movie-new
#author:alirezaghaderi

import enum
import uuid
from sqlalchemy import Column, String, Integer, Enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class MovieStatus(str, enum.Enum):
    want_to_watch = "want_to_watch"
    watched = "watched"

class Movie(Base):
    __tablename__ = "movies"

    movie_uuid = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    title = Column(String, nullable=False)
    genre = Column(String, nullable=True)  
    release_year = Column(Integer, nullable=True)
    status = Column(Enum(MovieStatus), nullable=False, default=MovieStatus.want_to_watch)
    rating = Column(Integer, nullable=True)  
    notes = Column(String, nullable=True)