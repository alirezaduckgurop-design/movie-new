# Project: movie-new
# Author: alirezaghaderi

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.models.movie import Movie
from uuid import UUID

class MovieLogic:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def add_movie(self, title, genre, release_year, watched):
        new_movie = Movie(
            title=title,
            genre=genre,
            release_year=release_year,
            status="watched" if watched else "want_to_watch"
        )
        self.db.add(new_movie)
        await self.db.commit()
        await self.db.refresh(new_movie)
        return new_movie

    async def get_all_movies(self):
        result = await self.db.execute(select(Movie))
        return result.scalars().all()

    async def count_movies(self):
        result = await self.db.execute(select(Movie))
        return len(result.scalars().all())

    async def delete_movie(self, movie_id: UUID):
        movie_obj = await self.db.get(Movie, movie_id)
        if not movie_obj:
            return False
        await self.db.delete(movie_obj)
        await self.db.commit()
        return True

    async def update_movie(self, movie_id: UUID, movie_data):
        movie_obj = await self.db.get(Movie, movie_id)
        if not movie_obj:
            return None

    
        if movie_data.title is not None:
            movie_obj.title = movie_data.title
        if movie_data.genre is not None:
            movie_obj.genre = movie_data.genre
        if movie_data.release_year is not None:
            movie_obj.release_year = movie_data.release_year
        if movie_data.watched is not None:
            movie_obj.status = "watched" if movie_data.watched else "want_to_watch"

        await self.db.commit()
        await self.db.refresh(movie_obj)
        return movie_obj