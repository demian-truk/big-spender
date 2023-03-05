import logging
import os

from aiogram import Bot, Dispatcher, executor, types

from keyboards import main_menu_keyboard
from middlewares import AccessMiddleware

logging.basicConfig(level=logging.INFO)

API_TOKEN = os.getenv("TELEGRAM_API_TOKEN")
ACCESS_ID = os.getenv("TELEGRAM_ACCESS_ID")

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(AccessMiddleware(int(ACCESS_ID)))


@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    """Send a welcome message"""
    await message.answer(
        "Привет 👋\nСобираешься опять потратить наши денежки? 😄",
        reply_markup=main_menu_keyboard,
    )


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
