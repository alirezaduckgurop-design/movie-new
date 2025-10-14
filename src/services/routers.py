# Project: movie-new
# Author: alirezaghaderi

from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from src.db.database import get_db
from src.logic.movie_logic import MovieLogic

movies = APIRouter(prefix="/movies", tags=["Movies"])
stats = APIRouter(prefix="/stats", tags=["Stats"])

class MovieCreate(BaseModel):
    title: str
    genre: str | None = None
    release_year: int | None = None
    watched: bool = False

@movies.get("/", summary="Get all movies")
async def get_movies(db: AsyncSession = Depends(get_db)):
    logic = MovieLogic(db)
    return await logic.get_all_movies()

@movies.post("/", summary="Add a new movie")
async def add_movie(movie: MovieCreate, db: AsyncSession = Depends(get_db)):
    logic = MovieLogic(db)
    new_movie = await logic.add_movie(
        title=movie.title,
        genre=movie.genre,
        release_year=movie.release_year,
        watched=movie.watched
    )
    return {"message": "Movie added", "movie": new_movie}

@stats.get("/count", summary="Get movies count")
async def movies_count(db: AsyncSession = Depends(get_db)):
    logic = MovieLogic(db)
    total = await logic.count_movies()
    return {"total_movies": total}