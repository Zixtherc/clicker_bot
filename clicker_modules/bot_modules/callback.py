from bot_modules.create_bot import dp
from aiogram.types import Message, CallbackQuery
from aiogram import F
from aiogram.filters import Command, CommandStart
from .keyboard import main_kb, menu_list, game_list
from .handler import add_user, check_user, plus_click

@dp.message(CommandStart)
async def hello(message : Message):
    await message.answer("Привет!", reply_markup = main_kb)

@dp.callback_query(F.data == "game1")
async def game(callback : CallbackQuery):
    await callback.message.edit_text("Жми на кнопук!", reply_markup = game_list)
    await plus_click(count_clicks = 0, points = 0 , user_id = 0)
    await callback.answer("Сработало")