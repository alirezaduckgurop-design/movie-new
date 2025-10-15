# Project:movie-new
# Author:alirezaghaderi

import os
from pathlib import Path

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    f"sqlite+aiosqlite:///{Path(__file__).resolve().parent.parent}/test.db"
)

APP_TITLE = "Movies"
APP_DESCRIPTION = "Movie management API"
APP_VERSION = "1.0.0"
DEBUG = True