# Project:movie-new
# Author:alirezaghaderi

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE_URL = f"sqlite+aiosqlite:///{BASE_DIR}/test.db"

APP_TITLE = "Movies"
APP_DESCRIPTION = "Movie management API"
APP_VERSION = "1.0.0"
DEBUG = True