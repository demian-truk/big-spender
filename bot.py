import logging
import os

from aiogram import Bot, Dispatcher, executor, types

from keyboards import main_menu_keyboard
from main import get_income, update_or_create_income
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


@dp.message_handler(lambda message: message.text.startswith("Доход"))
async def add_income(message: types.Message):
    """Create or update income"""
    user_message = message.text.replace("Доход", "").replace(" ", "")
    update_or_create_income(float(user_message))
    await message.answer("Баланс успешно изменен ✅")


@dp.message_handler()
async def main_menu(message: types.Message):
    if message.text == "💵 Доходы":
        income = get_income()
        if not income:
            await message.answer(
                "В твоих карманах совсем нет эдди 😢"
                + "\n\nДля добавления дохода введи сообщение в формате:\nДоход 125.30"
            )
        else:
            await message.answer(
                "Будь спокоен, ты еще не банкрот 😄🥳"
                + "\n\nОстаток денежных средств:\n"
                + str(income.amount)
                + " BYN"
                + "\n\nДля добавления дохода введи сообщение в формате:\nДоход 125.30"
            )


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
