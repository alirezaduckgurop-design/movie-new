# Project: movie-new
# Author: alirezaghaderi

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.models.movie import Movie
from uuid import UUID


class MovieRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

async def get_all(self):
    result = await self.db.execute(select(Movie))
    return result.scalars().all()

async def get_by_id(self, movie_id: UUID):
    return await self.db.get(Movie, movie_id)

async def add(self, movie: Movie):
    self.db.add(movie)
    await self.db.commit()
    await self.db.refresh(movie)
    return movie

async def update(self, movie_obj: Movie, data: dict):
    for key, value in data.items():
        setattr(movie_obj, key, value)
        await self.db.commit()
        await self.db.refresh(movie_obj)
        return movie_obj

async def delete(self, movie_obj: Movie):
    await self.db.delete(movie_obj)
    await self.db.commit()
    return True

async def count(self):
    result = await self.db.execute(select(Movie))
    return len(result.scalars().all())