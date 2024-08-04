import asyncio
from .callback import CallbackQuery, Message
from .create_bot import dp
from .users_base import sqlite3, cursor

async def add_user(username : str, user_id : int):
    with sqlite3.connect("users_data.db") as db:
        cursor.execute(f"INSERT INTO users_data WHERE user_id = {id} (username, user_id) VALUE(?,?)",(username, user_id))
        cursor.commit()

async def check_user(username : str, user_id : int):
    with sqlite3.connect("users_data.db") as db:
        cursor.execute("SELECT * FROM users_data WHERE user_id = ? AND username = ?", (username, user_id))
        user = cursor.fetchone()
        return user is not None 
    
async def plus_click(count_clicks : int, points : int, user_id : int):
    cursor.execute("SELECT count_clicks, points FROM users_data WHERE user_id = ?" (user_id))
    result = cursor.fetchone()

    if result:
        count_clicks, points = result
        count_clicks += 1
        points += 1

        cursor.execute("UPDATE users_data SET count_clicks = ?, points = ? WHERE user_id = ?" (count_clicks, points, user_id))
        cursor.commit()

    else: 
        Message.answer ("Вас не нашли в базе данных")
        cursor.commit()
