import logging
import os

from aiogram import Bot, Dispatcher, executor

from middlewares import AccessMiddleware

logging.basicConfig(level=logging.INFO)

API_TOKEN = os.getenv("TELEGRAM_API_TOKEN")
ACCESS_ID = os.getenv("TELEGRAM_ACCESS_ID")

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(AccessMiddleware(int(ACCESS_ID)))


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
