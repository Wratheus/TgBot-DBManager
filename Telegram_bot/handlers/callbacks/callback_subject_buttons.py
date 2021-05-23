from aiogram import types
from aiogram.dispatcher.filters import Text
from loader import dp, bot, db
from handlers.users.start import list

from keyboards.inline import group


@dp.callback_query_handler()
async def set_subject_keyboard(call):
    if call.data == "eng":
        await call.message.edit_reply_markup()
        await call.message.delete()
        subject_id = 1
        st_id = str(list[0][0])
        grade = db.grades(st_id, subject_id)
        attends = db.attend(st_id, subject_id)
        try:
            mess1 = "Ваша успеваемость: "
            mess2 = "Ваша посещаемость: "
            await call.message.answer(mess1)
            await call.message.answer("\n".join([f"отметка № {i + 1} : {val}"
                                                 for i, val in enumerate(grade[0].split(','))]))

            await call.message.answer(mess2)
            await call.message.answer("\n".join([f"Присутствие на занятии № {i + 1} : {val}"
                                                 for i, val in enumerate(attends[0].split(','))]))
        except AttributeError as err:
            await call.message.answer(
                "Данных по данному предмету нет.\nПопробуйте другую дисциплину.\nВведите команду start.")

        list.clear()

    elif call.data == "IT":
        await call.message.edit_reply_markup()
        await call.message.delete()
        subject_id = 2
        st_id = str(list[0][0])
        grade = db.grades(st_id, subject_id)
        attends = db.attend(st_id, subject_id)
        try:
            mess1 = "Ваша успеваемость: "
            mess2 = "Ваша посещаемость: "
            await call.message.answer(mess1)
            await call.message.answer("\n".join([f"отметка № {i + 1} : {val}"
                                                 for i, val in enumerate(grade[0].split(','))]))

            await call.message.answer(mess2)
            await call.message.answer("\n".join([f"Присутствие на занятии № {i + 1} : {val}"
                                                 for i, val in enumerate(attends[0].split(','))]))
        except AttributeError as err:
            await call.message.answer(
                "Данных по данному предмету нет.\nПопробуйте другую дисциплину.\nВведите команду start.")
        list.clear()

    elif call.data == "math":
        await call.message.edit_reply_markup()
        await call.message.delete()
        subject_id = 3
        st_id = str(list[0][0])
        grade = db.grades(st_id, subject_id)
        attends = db.attend(st_id, subject_id)
        mess1 = "Ваша успеваемость: "
        mess2 = "Ваша посещаемость: "
        try:
            await call.message.answer(mess1)
            await call.message.answer("\n".join([f"отметка № {i + 1} : {val}"
                                                 for i, val in enumerate(grade[0].split(','))]))

            await call.message.answer(mess2)
            await call.message.answer("\n".join([f"Присутствие на занятии № {i + 1} : {val}"
                                                 for i, val in enumerate(attends[0].split(','))]))
        except AttributeError as err:
            await call.message.answer(
                "Данных по данному предмету нет.\nПопробуйте другую дисциплину.\nВведите команду start.")
        list.clear()

    elif call.data == "physics":
        await call.message.edit_reply_markup()
        await call.message.delete()
        subject_id = 4
        st_id = str(list[0][0])
        grade = db.grades(st_id, subject_id)
        attends = db.attend(st_id, subject_id)
        mess1 = "Ваша успеваемость: "
        mess2 = "Ваша посещаемость: "
        try:
            await call.message.answer(mess1)
            await call.message.answer("\n".join([f"отметка № {i + 1} : {val}"
                                                 for i, val in enumerate(grade[0].split(','))]))

            await call.message.answer(mess2)
            await call.message.answer("\n".join([f"Присутствие на занятии № {i + 1} : {val}"
                                                 for i, val in enumerate(attends[0].split(','))]))
        except AttributeError as err:
            await call.message.answer(
                "Данных по данному предмету нет.\nПопробуйте другую дисциплину.\nВведите команду start.")
        list.clear()

    elif call.data == "logic":
        await call.message.edit_reply_markup()
        await call.message.delete()
        subject_id = 5
        st_id = str(list[0][0])
        grade = db.grades(st_id, subject_id)
        attends = db.attend(st_id, subject_id)
        mess1 = "Ваша успеваемость: "
        mess2 = "Ваша посещаемость: "
        try:
            await call.message.answer(mess1)
            await call.message.answer("\n".join([f"отметка № {i + 1} : {val}"
                                                 for i, val in enumerate(grade[0].split(','))]))

            await call.message.answer(mess2)
            await call.message.answer("\n".join([f"Присутствие на занятии № {i + 1} : {val}"
                                                 for i, val in enumerate(attends[0].split(','))]))
        except AttributeError as err:
            await call.message.answer(
                "Данных по данному предмету нет.\nПопробуйте другую дисциплину.\nВведите команду start.")
        list.clear()

    elif call.data == "TMP":
        await call.message.edit_reply_markup()
        await call.message.delete()
        subject_id = 6
        st_id = str(list[0][0])
        grade = db.grades(st_id, subject_id)
        attends = db.attend(st_id, subject_id)
        mess1 = "Ваша успеваемость: "
        mess2 = "Ваша посещаемость: "
        try:
            await call.message.answer(mess1)
            await call.message.answer("\n".join([f"отметка № {i + 1} : {val}"
                                                 for i, val in enumerate(grade[0].split(','))]))

            await call.message.answer(mess2)
            await call.message.answer("\n".join([f"Присутствие на занятии № {i + 1} : {val}"
                                                 for i, val in enumerate(attends[0].split(','))]))
        except AttributeError as err:
            await call.message.answer(
                "Данных по данному предмету нет.\nПопробуйте другую дисциплину.\nВведите команду start.")
        list.clear()

    elif call.data == "phylos":
        await call.message.edit_reply_markup()
        await call.message.delete()
        subject_id = 7
        st_id = str(list[0][0])
        grade = db.grades(st_id, subject_id)
        attends = db.attend(st_id, subject_id)
        mess1 = "Ваша успеваемость: "
        mess2 = "Ваша посещаемость: "
        try:
            await call.message.answer(mess1)
            await call.message.answer("\n".join([f"отметка № {i + 1} : {val}"
                                                 for i, val in enumerate(grade[0].split(','))]))

            await call.message.answer(mess2)
            await call.message.answer("\n".join([f"Присутствие на занятии № {i + 1} : {val}"
                                                 for i, val in enumerate(attends[0].split(','))]))
        except AttributeError as err:
            await call.message.answer(
                "Данных по данному предмету нет.\nПопробуйте другую дисциплину.\nВведите команду start.")
        list.clear()

    elif call.data == "OIB":
        await call.message.edit_reply_markup()
        await call.message.delete()
        subject_id = 8
        st_id = str(list[0][0])
        grade = db.grades(st_id, subject_id)
        attends = db.attend(st_id, subject_id)
        mess1 = "Ваша успеваемость: "
        mess2 = "Ваша посещаемость: "
        try:
            await call.message.answer(mess1)
            await call.message.answer("\n".join([f"отметка № {i + 1} : {val}"
                                                 for i, val in enumerate(grade[0].split(','))]))

            await call.message.answer(mess2)
            await call.message.answer("\n".join([f"Присутствие на занятии № {i + 1} : {val}"
                                                 for i, val in enumerate(attends[0].split(','))]))
        except AttributeError as err:
            await call.message.answer(
                "Данных по данному предмету нет.\nПопробуйте другую дисциплину.\nВведите команду start.")
        list.clear()

    elif call.data == "PE":
        await call.message.edit_reply_markup()
        await call.message.delete()
        subject_id = 9
        st_id = str(list[0][0])
        grade = db.grades(st_id, subject_id)
        attends = db.attend(st_id, subject_id)
        mess1 = "Ваша успеваемость: "
        mess2 = "Ваша посещаемость: "
        try:
            await call.message.answer(mess1)
            await call.message.answer("\n".join([f"отметка № {i + 1} : {val}"
                                                 for i, val in enumerate(grade[0].split(','))]))

            await call.message.answer(mess2)
            await call.message.answer("\n".join([f"Присутствие на занятии № {i + 1} : {val}"
                                                 for i, val in enumerate(attends[0].split(','))]))
        except AttributeError as err:
            await call.message.answer(
                "Данных по данному предмету нет.\nПопробуйте другую дисциплину.\nВведите команду start.")
        list.clear()

    elif call.data == "BD":
        await call.message.edit_reply_markup()
        await call.message.delete()
        subject_id = 10
        st_id = str(list[0][0])
        grade = db.grades(st_id, subject_id)
        attends = db.attend(st_id, subject_id)
        mess1 = "Ваша успеваемость: "
        mess2 = "Ваша посещаемость: "
        try:
            await call.message.answer(mess1)
            await call.message.answer("\n".join([f"отметка № {i + 1} : {val}"
                                                 for i, val in enumerate(grade[0].split(','))]))

            await call.message.answer(mess2)
            await call.message.answer("\n".join([f"Присутствие на занятии № {i + 1} : {val}"
                                                 for i, val in enumerate(attends[0].split(','))]))
        except AttributeError as err:
            await call.message.answer(
                "Данных по данному предмету нет.\nПопробуйте другую дисциплину.\nВведите команду start.")
        list.clear()
# await db.get_subject_id()
