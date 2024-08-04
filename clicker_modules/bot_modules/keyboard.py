from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton

main_kb = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
    [InlineKeyboardButton(text="Играть!", callback_data="game")],
    [InlineKeyboardButton(text="Меню", callback_data="menu"),
     InlineKeyboardButton(text="Магазин", callback_data="shop")],
    [InlineKeyboardButton(text="Топ игроков", callback_data="top_of_user")]
])

game_list = InlineKeyboardMarkup(row_width=1, inline_keyboard=[
    [InlineKeyboardButton(text="Жми!", callback_data="click")]
])

menu_list = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
    [InlineKeyboardButton(text="Правила", callback_data="rules"), 
     InlineKeyboardButton(text="Код", callback_data="code")]
])

# shop_list = InlineKeyboardMarkup(row_width = 1 , inline_keyboard = [
#     None
# ])