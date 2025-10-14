#Project:movie-new
#author:alirezaghaderi

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Enum
import enum

Base = declarative_base()

class MovieStatus(str, enum.Enum):
    want_to_watch = "want_to_watch"
    watched = "watched"

class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    genre = Column(String, nullable=True)
    release_year = Column(Integer, nullable=True)
    status = Column(Enum(MovieStatus), nullable=False, default=MovieStatus.want_to_watch)
    rating = Column(Integer, nullable=True)
    notes = Column(String, nullable=False)