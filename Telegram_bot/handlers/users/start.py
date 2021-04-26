from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.inline.subject_buttons import group
from loader import dp, db
from states.fio import Fio


@dp.message_handler(CommandStart())
async def start(message: types.Message):
    await message.answer(f'Привет, {message.from_user.full_name}!\n'
                         f"Чтобы продолжить работу со мной введите Вашу фамилию")
    await Fio.last_name.set()

@dp.message_handler(state=Fio.last_name)
async def we_got_it(message: types.Message, state: FSMContext):
    answer = message.text
    try:
        user = await db.check_student(student_name=answer)
        if user == "Бушманов Николай Васильевич":
            student_id = await db.get_id(answer)
            await state.finish()
            await message.answer("Выбери предмет", reply_markup=group)
            #Переменная для id предмета
            #вкидываем в тюпл

        else:
            await message.answer("🐀")
    finally:
        print("Something else went wrong")

