import csv
import os
import json

from Program import trans_dir
from json import JSONDecodeError
from csv import Error

def read_csv(file, new_dir, fpath):
    try:
        result = []
        with open(file, newline='') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=";")
            for row in reader:
                result.append(dict(row))

        print("Вернул словарь с данными о пассажирах")
        return result
    except Error:
        print(f"{Error} ошибка считывания из scv файла")
        trans_dir(file, new_dir, fpath)
    finally:
        print("Закончил работу с файлом")
        csvfile.close()


def list_files(path):
    try:
        files = os.listdir(path)
        print(path)
        print(files)
        if files:
            files = [os.path.join(path, file) for file in files]
            files = [file for file in files if os.path.isfile(file)]
            print(f"Вернул списко файлов \n{files}")
            return files
        else:
            print("Файлов в данной папке нет")
    except:
        print("Ошибка при составлении списка файлов или файлов в данной папке нет")
    finally:
        print("Закончил поиск файлов")


def file_name(file_path, new_dir, fpath):
    try:
        name = os.path.basename(rf'{file_path}')
        file_path = os.path.splitext(name)[0]
        return file_path
    except:
        print("Невозможно преобразовать имя файла")
        trans_dir(file_path, new_dir, fpath)


def create_json(dir_path, file_name, ready_info):
    try:
        with open(f'{dir_path}\\{file_name}.json', 'w') as json_file:
            json.dump(ready_info, json_file, indent=2)
        print("JSON-файл создан и наполнен")
    except JSONDecodeError:
        print(f"{JSONDecodeError} ошибка при создании или записи в файл")
    finally:
        print("Закончил работу с JSON-файлом")



