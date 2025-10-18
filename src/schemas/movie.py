# Project: movie-new
# Author: alirezaghaderi

from pydantic import BaseModel
from typing import Optional
from enum import Enum


class MovieStatus(str, Enum):
    want_to_watch = "want_to_watch"
    watched = "watched"


class MovieBase(BaseModel):
    title: str
    genre: Optional[str] = None
    release_year: Optional[int] = None


class MovieCreate(MovieBase):
    watched: bool = False  


class MovieUpdate(MovieBase):
    watched: Optional[bool] = None

class MovieOut(MovieBase):
    movie_uuid: str  
    status: MovieStatus
    rating: Optional[int] = None
    notes: Optional[str] = None

    class Config:
        from_attributes = True