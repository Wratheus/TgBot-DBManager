import sqlite3


class Database:
    def __init__(self, path_to_db="test.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parametrs: tuple = None, fetchone=False, commit=False):
        if not parametrs:
            parametrs = tuple()
        connection = self.connection
        cursor = connection.cursor()
        cursor.execute(sql, parametrs)
        data = None
        if commit:
            connection.commit()
        if fetchone:
            data = cursor.fetchone()
        else:
            data = cursor.fetchall()
        connection.close()
        return data

    def check_student(self, student_name):
        sql = """SELECT * FROM students WHERE student_name = ?"""
        tpl = []
        tpl.append(student_name)
        return  self.execute(sql, tuple(tpl))

    def get_id(self, student_name):
        sql = """SELECT student_id FROM students WHERE student_name = ?"""
        tpl = []
        tpl.append(student_name)
        return  self.execute(sql, tuple(tpl), fetchone=True)

    #Использовать для кнопок
    def get_subject_id(self, subject_name):
        sql = """SELECT subject_id FROM subjects WHERE subject_name = ?"""
        tpl = []
        tpl.append(subject_name)
        return self.execute(sql, tuple(tpl), fetchone=True)

    def grades(self, student_id, subject_id):
        sql = """SELECT grades FROM journal WHERE student_id = ? AND subject_id = ?"""
        tpl = []
        tpl.append(student_id)
        tpl.append(subject_id)
        return  self.execute(sql, tuple(tpl), fetchone=True)

    def attend(self, student_id, subject_id):
        sql = """SELECT attendance FROM journal WHERE student_id = ? AND subject_id = ?"""
        tpl = []
        tpl.append(student_id)
        tpl.append(subject_id)
        return self.execute(sql, tuple(tpl), fetchone=True)


    # #Использовать для кнопок
    # async def get_subject_id(self, subject_name):
    #     sql = """SELECT subject_id FROM subjects WHERE subject_name = ?"""
    #     return await self.execute(sql, subject_name, fetchone=True,)
    #
    # #Это нужно закинуть в переменную, и отсортировать строку как список
    # async def grades(self, student_id: str, subject_id: str):
    #     sql = """SELECT grades FROM journal WHERE student_id = ? AND subject_id = ?"""
    #     return await self.execute(sql, student_id, subject_id, fetchall=True,)
    #
    # async def attend(self, student_id: str, subject_id: str):
    #     sql = """SELECT attendance FROM journal WHERE student_id = ? AND subject_id = ?"""
    #     return await self.execute(sql, student_id, subject_id, fetchone=True,)