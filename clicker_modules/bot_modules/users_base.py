import sqlite3

with sqlite3.connect("users_data.db") as db:
    cursor = db.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        username TEXT NOT NULL,
        user_id INTEGER NOT NULL,
        points INTEGER NOT NULL,
        count_clicks INTEGER NOT NULL
    )
    """)
    db.commit()