"""
Helper Script for generate_faces.py
Needs to run once if db.sqlite does not exist.
"""

import sqlite3 as sql

DB = sql.connect('db.sqlite', check_same_thread=False)

with DB:
    DB.execute("""
        CREATE TABLE if NOT EXISTS image_record (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            gender TEXT,
            age INTEGER,
            filename TEXT,
            hosting TEXT,
            date_added INTEGER,
            source TEXT,
            last_served INTEGER,
            created_at INTEGER,
            updated_at INTEGER,
            is_deleted INTEGER,
            deleted_at INTEGER
        );
    """)