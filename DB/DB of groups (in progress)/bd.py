import sqlite3
from sqlite3 import Error

#con = sqlite3.connect('tg.db') #connection - объкт предствления бд
#cur = conn.cursor() #cursor - объект, чтоб делать запросы к бд

'''
cur.execute("""INSERT INTO users(userid, fname, lname, gender) 
   VALUES('00001', 'Alex', 'Smith', 'male');""") execute - запрос
conn.commit() - commit, чтоб сохранить

cur.execute("INSERT INTO users VALUES(?, ?, ?, ?);", user)  вопросы авотматически подставят значения кортежа user = (1, 2, 3, 4)
conn.commit()                                               executemany("...VALUES(?,?..);" more_users)  more_users = [(1,2..), (3,4..)....]
'''
con = sqlite3.connect('tg.db')

def sql_connection():
    try:
        con = sqlite3.connect('tg.db')
        print("Connection is established: Database is created in memory")
    except Error:
        print(Error)
    return con

def sql_create_table_group(con):
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS mda(stud_id INTEGER PRIMARY KEY AUTOINCREMENT, name_stud VARCHAR(50))''')
    con.commit()

def sql_insert(con, val):
    cur = con.cursor()
    cur.execute('''INSERT INTO mda(name_stud) VALUES(?)''', (val,))
    con.commit()

def sql_print_all(con):
    with con:
        cur = con.cursor()
        cur.execute('''SELECT * FROM mda''')
        while True:
            row = cur.fetchone()
            if row == None:
                break
            print(row[0], row[1])

def sql_del_table(con):
    cur = con.cursor()
    cur.execute('''DROP TABLE IF EXISTS mda''')
    con.commit()

bd_names_9 = ("Ананьев Дмитрий Александрович", "Антипович Дарья Витальевна", "Бухтиярова Дарья Олеговна", "Бушманов Николай Васильевич", "Ворончихин Владимир Владимирович", "Гудочкина Анна Романовна", "Дмитриев Сергей Сергеевич", "Евсеев Владислав Дмитриевич", "Клюев Денис", "Кочергин Данил Андреевич", "Курилюк Кирилл Александрович", "Лобов Сергей Александрович", "Лободина Елизавета Артемовна", "Лухманов Иван Николаевич", "Мирошников Никита Александрович", "Михайлов Владимир Олегович", "Москвин Виталий Александрович", "Муленко Валерий Павлович", "Мякишева Юлия Михайловна", "Наумова Татьяна Дмитриевна", "Ниталиев Артём Жумагалиевич", "Павленко Александр Сергеевич", "Райлян Даниил Павлович", "Решетников Михаил Игоревич", "Самохин Григорий Андреевич", "Смирнов Алексей Сергеевич", "Улахияне Абделлах", "Умаров Руслан Ибрагимович", "Фомичев Виталий Артурович", "Халилова Рената Руслановна", "Хлопов Александр Михайлович", "Черняева Александра Сергеевна", "Шестакова Виктория Артуровна")
bd_names_7 = ("Алиев Айдын Джаббарович", "Браун Леонид Андреевич", "Валуйская Эльвира Денисовна", "Воробьев Артём Валерьевич", "Герасенкова Ксения Игоревна", "Готьятов Владислав Михайлович", "Данилов Максим Алексеевич", "Ермачкова Мария Владиславовна", "Ивлева Полина Витальевна", "Икоева Лаура Федоровна", "Инг Висал", "Кахаров Дамир Толибович", "Кукушкин Максим Михайлович", "Магеррамов Тимур Вугар оглы", "Марочкин Даниил Алексеевич", "Мохнаткин Николай Викторович", "Муравьев Кирилл Васильевич", "Муравьев Максим Игоревич", "Насир Махмуд Сухибович", "Рогозин Вадим Дмитриевич", "Рубацкий Роман Андреевич", "Садовская Александра Владимировна", "Саразова Инна Александровна", "Сманцырева Вероника Вадимовна", "Спицына Лилия Алексеевна", "Усанова Анна Евгеньевна", "Уткин Сергей Алексеевич", "Хамед Мохамед Махфуд", "Чахир Арина Александровна", "Шайер Адриан Владимирович", "Шестаков Семён Михайлович", "Щербаков Владимир", "Якубовский Иван Александрович")

sql_connection()

print("Выберите номер группы: 9 или 7")
number = int(input())
if number == 7 or number == 9:
    sql_create_table_group(con)
else:
    print("Ошибка ввода")

if number == 9:
    for i in range(len(bd_names_9)):
        sql_insert(con, bd_names_9[i])
else:
    for i in range(len(bd_names_7)):
        sql_insert(con, bd_names_7[i])


sql_print_all(con)

sql_del_table(con)
print("Таблица удалена из памяти")



