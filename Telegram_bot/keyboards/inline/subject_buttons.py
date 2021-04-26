from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

group = InlineKeyboardMarkup()
group1 = InlineKeyboardButton("Иностранный язык", callback_data='eng')
group2 = InlineKeyboardButton("Информатика", callback_data='IT')
group3 = InlineKeyboardButton("Математика", callback_data='math')
group4 = InlineKeyboardButton("Физика", callback_data='physics')
group5 = InlineKeyboardButton("Математическая логика", callback_data='logic')
group6 = InlineKeyboardButton("Технологии и методы программирования", callback_data='TMP')
group7 = InlineKeyboardButton("Философия", callback_data='phylos')
group8 = InlineKeyboardButton("Основы информационной безопасности", callback_data='OIB')
group9 = InlineKeyboardButton("Практикум по физической культуре и спорту", callback_data='PE')
group10 = InlineKeyboardButton("Базы данных", callback_data='BD')

group.add(group1, group2, group3, group4, group5, group6, group7, group8, group9, group10)

