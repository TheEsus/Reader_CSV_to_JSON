from DB_func.Program_DB import create_db, create_table, inserter
from ProgramFile import read_csv, list_files, file_name, create_json
from Program import convert_data, convert_f_name, create_dir, trans_dir

import time

path = r'E:\MByWork\S7'


def main():
    print("Создаю основные директории")
    print("_______________________________________________________")

    list_path = create_dir(path)

    print("Создаю базу и таблицу")
    base = create_db(list_path[4])
    create_table(base)

    print("_______________________________________________________")
    print("Провожу поиск файлов на обработку")
    while True:
        full_path = list_files(list_path[0])
        if full_path is not None:
            json_prog(base, full_path, list_path)
        else:
            print("Файлы не найдены")
            time.sleep(20)


def json_prog(base, full_path, list_path):
    print("_______________________________________________________")
    print("Получаю данные из csv файла")
    for i in full_path:
        dict_csv = read_csv(i, list_path[1], path)
        print("_______________________________________________________")
        print("Конвертирую дату в данных под нужный формат YYYY-MM-DD")
        for k in range(len(dict_csv)):
            dict_csv[k]['bdate'] = str(convert_data(dict_csv[k]['bdate'], i, list_path[1], path))
            print(f"Из словаря - {dict_csv[k]['bdate']}")
        print("_______________________________________________________")

        print("Получаю имя файла")
        print(f"Полный путь к файлу = {i}")
        name = file_name(i, list_path[1], path)
        print(f"Имя файла = {name}")
        print("Именя файла получено")

        print("_______________________________________________________")
        print("Преобразовываю имя файла")
        list_file_name = convert_f_name(name, i, list_path[1], path)
        print(f"Имя файла без расширения - {name}")
        print("Преобразовывание завершено")
        print("_______________________________________________________")
        print("Конвертирую дату в части имени файла под нужный формат YYYY-MM-DD")
        list_file_name[0] = convert_data(list_file_name[0], i, list_path[1], path)
        print(f"Из имени файла - {list_file_name[0]}")
        print("_______________________________________________________")

        dict_to_json = {
            "fit": list_file_name[1],
            "date": str(list_file_name[0]),
            "dep": list_file_name[2],
            "prl": dict_csv
        }
        create_json(list_path[3], name, dict_to_json)
        print("_______________________________________________________")
        trans_dir(i, list_path[2], path)
        inserter(base, name, list_file_name)
        print("_______________________________________________________")


main()
