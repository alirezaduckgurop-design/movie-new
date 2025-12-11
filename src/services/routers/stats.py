#Project:movie-new
#author:alirezaghaderi

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.db.database import get_db
from src.logic.movie_logic import MovieLogic

router = APIRouter(prefix="/stats", tags=["Stats"])

@router.get("/count", summary="Get movies count")
async def movies_count(db: AsyncSession = Depends(get_db)):
    logic = MovieLogic(db)
    total = await logic.count_movies()
    return {"total_movies": total}