from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.inline.subject_buttons import group
from loader import dp, db
from states.fio import Fio

list = []


@dp.message_handler(CommandStart())
async def start(message: types.Message):
    await message.answer(f'Привет, {message.from_user.full_name}!\n'
                         f"Чтобы продолжить работу со мной введите Ваше ФИО")
    await Fio.last_name.set()


@dp.message_handler(state=Fio.last_name)
async def we_got_it(message: types.Message, state: FSMContext):
    answer = message.text
    global list
    try:
        user = db.check_student(student_name=answer)
        if len(user) > 0:
            student_id = db.get_id(answer)
            list.append(student_id)
            await state.finish()
            await message.answer("Выбери предмет", reply_markup=group)
        else:
            await message.answer("🐀")
    finally:
        print("Something else went wrong")

