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
        movies_list = result.scalars().all()
        return len(movies_list)

    async def delete_movie(self, movie_id: UUID):
        movie_obj = await self.db.get(Movie, movie_id)
        if not movie_obj:
            return False
        await self.db.delete(movie_obj)
        await self.db.commit()
        return True

    async def update_movie(self, movie_id: UUID, title, genre, release_year, watched):
        movie_obj = await self.db.get(Movie, movie_id)
        if not movie_obj:
            return None
        movie_obj.title = title
        movie_obj.genre = genre
        movie_obj.release_year = release_year
        movie_obj.status = "watched" if watched else "want_to_watch"