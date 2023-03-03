from aiogram import types

main_menu_keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)

incomes = types.KeyboardButton(text="💵 Доходы")
expenses = types.KeyboardButton(text="🛒 Расходы")
categories = types.KeyboardButton(text="📋 Категории")
stats = types.KeyboardButton(text="📊 Статистика")

main_menu_keyboard.add(incomes, expenses)
main_menu_keyboard.add(categories, stats)
