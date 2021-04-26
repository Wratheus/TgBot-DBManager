from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Получить успеваемость"),
            KeyboardButton(text="Получить посещаемость"),
        ]

    ],
    resize_keyboard=True
)
