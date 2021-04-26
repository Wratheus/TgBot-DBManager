# from aiogram import types
# from aiogram.dispatcher.filters import Command
# from aiogram.dispatcher import FSMContext
#
# from keyboards.default import menu
# from loader import dp
# from states.fio import Fio
#
#
# @dp.message_handler(Command("menu"))
# async def show_menu(message: types.Message):
#     await message.answer("Что Вы хотите получить?", reply_markup=menu)
#
#
# @dp.message_handler(text="Получить успеваемость", state=Fio.last_name)
# async def get_marks(message: types.Message, state: FSMContext):
#     await message.answer(f"Введите Ваше ФИО")
#     answer = message.text
#
#     await state.update_data(answer1=answer)
#
#     await Fio.last_name.set()
#
#
# @dp.message_handler(text="Получить посещаемость", state=Fio.last_name)
# async def get_attend(message: types.Message, state: FSMContext):
#     await message.answer(f"Введите Ваше ФИО")
#     answer = message.text
#
#     await state.update_data(answer1=answer)
#
#     await Fio.last_name.set()
#
