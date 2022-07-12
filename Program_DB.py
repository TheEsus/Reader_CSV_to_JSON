import sqlite3 as sl
from sqlite3 import Error


def create_db(path):
    try:
        base = sl.connect(f"{path}\\flight_Base.db")

        print("База данных создана")
        return base

    except Error:
        print(f"{Error} Ошибка создания БД")


def create_table(db):
    try:
        base_cursor = db.cursor()

        base_cursor.execute("""
                    CREATE TABLE IF NOT EXISTS FLIGHT(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        file_name TEXT NOT NULL,
                        flt INTEGER NOT NULL,
                        depdate DATE NOT NULL,
                        dep TEXT NOT NULL
                    );
                """)
        print("Таблица flight создана")
    except Error as er:
        print(f"{er.args} Ошибка создания таблицы")


def inserter(db, file_name, file_info):
    try:
        print(file_info[1] + " " + str(file_info[0]) + " " + file_info[2])
        base_cursor = db.cursor()
        sql_insert = f"INSERT INTO FLIGHT(file_name, flt, depdate, dep) VALUES (?, {int(file_info[1])}, ?, ?);"
        base_cursor.execute(sql_insert, (file_name, str(file_info[0]), str(file_info[2])))
        db.commit()
        print("Данные записаны в БД")
    except Error as er:
        print(f"{er.args} ошибка при записи в файл")
