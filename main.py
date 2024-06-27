import sqlite3


def copy_to_file(db_name, file_name):
    with sqlite3.connect(f"{db_name}") as con:

        with open(f"{file_name}", "w") as f:
            for sql in con.iterdump():
                f.write(sql)

        with open(f"{file_name}", "r") as f_:
            return f_.read()


def copy_to_db(file_name, new_db):
    with sqlite3.connect(f"{new_db}") as con:
        cur = con.cursor()

        with open(f"{file_name}", "r") as f:
            sql = f.read()
            cur.executescript(sql)

            return sql


def result():

    answer = int(input("Копирование данных в файл ( 1 ), Загрузить данные из файла в новую базу данных ( 0 ) "))
    if answer:
        db_name = input("Введите имя базы данных >> ")
        file_name = input("Имя файла >> ")
        message = copy_to_file(db_name=db_name, file_name=file_name)
    else:
        f_name = input("Имя файла >> ")
        new_db = input("Имя новый база данных >> ")
        message = copy_to_db(file_name=f_name, new_db=new_db)

    return message


print(result())




