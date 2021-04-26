from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp
from aiogram import types
from states.test import Test


@dp.message_handler(Command("test"))
async def testing(message : types.Message):
    await message.answer("1 вопрос")

    await Test.Q1.set()


@dp.message_handler(state=Test.Q1)
async def ans_q1(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(answer1=answer)

    await message.answer("2 вопрос")
    await Test.Q2.set()


@dp.message_handler(state=Test.Q2)
async def ans_q2(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer1 = data.get("answer1")
    answer2 = message.text

    await message.answer("Спасибо")
    await message.answer(f"Ответ 1: {answer1}\n"
                         f"Ответ 2: {answer2}"
                         )

    await state.finish()