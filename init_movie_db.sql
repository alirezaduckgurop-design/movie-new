-- Project: movie-new
-- Author: alirezaghaderi

DROP TABLE IF EXISTS movies;

CREATE TABLE movies (
    movie_uuid TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    genre TEXT,
    release_year INTEGER,
    status TEXT CHECK(status IN ('watched', 'want_to_watch')) DEFAULT 'want_to_watch',
    rating INTEGER CHECK(rating >= 0 AND rating <= 5),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

