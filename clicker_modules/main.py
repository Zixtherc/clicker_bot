import asyncio
from bot_modules.create_bot import dp, bot

async def main():
    await dp.start_polling(bot)
asyncio.run(main())
