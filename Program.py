import os
import shutil

from shutil import Error
from dateutil.parser import parse
from dateutil.parser import ParserError



def convert_data(dict_data, folder1, folder2, fpath):
    try:
        dt = parse(dict_data)
        dict_data = dt.date()
        return dict_data
    except ParserError as er:
        print(f"Ошибка при форматировании даты\n {er.args}")
        trans_dir(folder1, folder2, fpath)


def convert_f_name(name, old_fold, new_fold, fpath):
    try:
        if name.count("_") == 2:
            name = name.split("_")
            return name
        else:
            print("Нарушен формат имени файла Дата_Рейс_Аэропорт")
    except:
        print("Невозможно преобразовать имя файла")
        trans_dir(old_fold, new_fold, fpath)


def create_dir(fpath):
    try:
        list_path = [
            fpath + "\\In",
            fpath + "\\Err",
            fpath + "\\Ok",
            fpath + "\\Out",
            fpath + "\\DB"
        ]
        for i in list_path:
            if os.path.exists(i):
                print(f"Данная папка существует \n{i}")
                print("_______________________________________________________")
            else:
                print(f"Создана папка {i}")
                os.mkdir(i)
                print("_______________________________________________________")
        return list_path
    except:
        print("Ошибка создания директорий")


def trans_dir(old_dir, new_dir, fpath):
    try:
        shutil.move(old_dir, new_dir)

    except Error as er:
        print(f"Ошибка при смене директории\n {er}")
        create_dir(fpath)
        shutil.move(old_dir, new_dir)
