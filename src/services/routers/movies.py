#Project:movie-new
#author:alirezaghaderi

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src.db.database import get_db
from src.logic.movie_logic import MovieLogic
from src.schemas.movie import MovieCreate, MovieUpdate, MovieOut

router = APIRouter(prefix="/movies", tags=["Movies"])

@router.get("/", summary="Get all movies", response_model=list[MovieOut])
async def get_movies(db: AsyncSession = Depends(get_db)):
    logic = MovieLogic(db)
    return await logic.get_all_movies()

@router.get("/{movie_uuid}", summary="Get movie by UUID", response_model=MovieOut)
async def get_movie(movie_uuid: str, db: AsyncSession = Depends(get_db)):
    logic = MovieLogic(db)
    movie = await logic.get_movie(movie_uuid)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie

@router.post("/", summary="Add a new movie", response_model=MovieOut)
async def add_movie(movie: MovieCreate, db: AsyncSession = Depends(get_db)):
    logic = MovieLogic(db)
    return await logic.add_movie(
        title=movie.title,
        genre=movie.genre,
        release_year=movie.release_year,
        watched=movie.watched
    )

@router.put("/{movie_uuid}", summary="Update a movie", response_model=MovieOut)
async def update_movie(movie_uuid: str, movie: MovieUpdate, db: AsyncSession = Depends(get_db)):
    logic = MovieLogic(db)
    updated = await logic.update_movie(movie_uuid, movie)
    if not updated:
        raise HTTPException(status_code=404, detail="Movie not found")
    return updated

@router.delete("/{movie_uuid}", summary="Delete a movie")
async def delete_movie(movie_uuid: str, db: AsyncSession = Depends(get_db)):
    logic = MovieLogic(db)
    deleted = await logic.delete_movie(movie_uuid)
    if not deleted:
        raise HTTPException(status_code=404, detail="Movie not found")
    return {"message": "Movie deleted"}