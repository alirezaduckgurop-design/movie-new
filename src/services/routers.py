# Project: movie-new
# Author: Alireza Ghaderi

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from pydantic import BaseModel
from src.models.movie import Movie
from src.db.database import get_session  

movies = APIRouter(prefix="/movies", tags=["Movies"])
stats = APIRouter(prefix="/stats", tags=["Stats"])


class MovieCreate(BaseModel):
    title: str
    genre: str | None = None
    release_year: int | None = None


@movies.get("/", summary="Get all movies")
async def get_movies(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Movie))
    movies_list = result.scalars().all()
    return movies_list


@movies.post("/", summary="Add a new movie")
async def add_movie(movie: MovieCreate, session: AsyncSession = Depends(get_session)):
    new_movie = Movie(
        title=movie.title,
        genre=movie.genre,
        release_year=movie.release_year,
    )
    session.add(new_movie)
    await session.commit()
    await session.refresh(new_movie)
    return {"message": "Movie added", "movie": new_movie}


@stats.get("/count", summary="Get movies count")
async def movies_count(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(func.count(Movie.id)))
    count = result.scalar()
    return {"total_movies": count}