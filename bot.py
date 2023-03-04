import logging
import os

from aiogram import Bot, Dispatcher, executor

logging.basicConfig(level=logging.INFO)

API_TOKEN = os.getenv("TELEGRAM_API_TOKEN")

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
