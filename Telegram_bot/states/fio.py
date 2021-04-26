from aiogram.dispatcher.filters.state import StatesGroup, State


class Fio(StatesGroup):
    last_name = State()