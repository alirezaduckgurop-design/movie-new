import sqlite3

conn = sqlite3.connect("movies.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS movies (
    movie_uuid TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    genre TEXT,
    release_year INTEGER,
    status TEXT CHECK(status IN ('want_to_watch', 'watched')) DEFAULT 'want_to_watch',
    rating INTEGER,
    notes TEXT
);
""")

conn.commit()
conn.close()

print(" Database and table created successfully (movies.db)")
