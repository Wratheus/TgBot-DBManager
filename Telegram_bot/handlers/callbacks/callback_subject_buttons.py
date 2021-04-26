from aiogram import types
from aiogram.dispatcher.filters import Text
from loader import dp, bot, db

from keyboards.inline import group


@dp.callback_query_handler()
async def set_subject_keyboard(call):

    if call.data == "eng":
        await call.message.edit_reply_markup()
        await call.message.delete()
        subject_id = 1
        await call.message.answer(subject_id)

    elif call.data == "IT":
        await call.message.edit_reply_markup()
        await call.message.delete()
        subject_id = 2
        await call.message.answer(subject_id)

    elif call.data == "math":
        await call.message.edit_reply_markup()
        await call.message.delete()
        subject_id = 3
        await call.message.answer(subject_id)

    elif call.data == "physics":
        await call.message.edit_reply_markup()
        await call.message.delete()
        subject_id = 4
        await call.message.answer(subject_id)

    elif call.data == "logic":
        await call.message.edit_reply_markup()
        await call.message.delete()
        subject_id = 5
        await call.message.answer(subject_id)

    elif call.data == "TMP":
        await call.message.edit_reply_markup()
        await call.message.delete()
        subject_id = 6
        await call.message.answer(subject_id)

    elif call.data == "phylos":
        await call.message.edit_reply_markup()
        await call.message.delete()
        subject_id = 7
        await call.message.answer(subject_id)

    elif call.data == "OIB":
        await call.message.edit_reply_markup()
        await call.message.delete()
        subject_id = 8
        await call.message.answer(subject_id)

    elif call.data == "PE":
        await call.message.edit_reply_markup()
        await call.message.delete()
        subject_id = 9
        await call.message.answer(subject_id)

    elif call.data == "BD":
        await call.message.edit_reply_markup()
        await call.message.delete()
        subject_id = 10
        await call.message.answer(subject_id)
#await db.get_subject_id()