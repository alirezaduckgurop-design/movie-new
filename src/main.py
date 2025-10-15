#Project:movie-new
#author:alirezaghaderi

import uvicorn
from fastapi import FastAPI
from sqlalchemy.ext.asyncio import create_async_engine
from src.models.movie import Base
from src.services.routers.movies import router as movies
from src.services.routers.stats import router as stats
from src.db.database import engine, Base

app = FastAPI(
    title="Movies",
    description="Movie management API",
    version="1.0.0"
)
app.include_router(movies)
app.include_router(stats)

@app.get("/health", tags=["System"])
async def health_check():
    return {"status": "ok"}

@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


if __name__ == "__main__":
    uvicorn.run("src.main:app", host="127.0.0.1", port=8000, reload=True)