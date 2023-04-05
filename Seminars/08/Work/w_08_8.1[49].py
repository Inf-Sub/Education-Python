# №8.1[49]. Создать телефонный справочник с возможностью импорта и экспорта данных в формате .csv
# Информация о человеке:
# Фамилия, Имя, Телефон, Описание
# Корректность и уникальность данных не обязательны.
# Функционал программы
# 1) телефонный справочник хранится в памяти в процессе выполнения кода.
# Выберите наиболее удобную структуру данных для хранения справочника.
# 2) CRUD: Create, Read, Update, Delete
# Create: Создание новой записи в справочнике: ввод всех полей новой записи, занесение ее в справочник.
# Read: он же Select. Выбор записей, удовлетворяющих заданном фильтру: по первой части фамилии человека. Берем первое совпадение по фамилии.
# Update: Изменение полей выбранной записи. Выбор записи как и в Read, заполнение новыми значениями.
# Delete: Удаление записи из справочника. Выбор - как в Read.
# 3) экспорт данных в текстовый файл формата csv
# 4) импорт данных из текстового файла формата csv
# Используйте функции для реализации значимых действий в программе
# Усложнение.
# - Сделать тесты для функций
# - Разделить на model-view-controller

# import os

# fio = {'Иванов Иван': ['897097','работник'], 'Петров Петр': ['35346', 'не раб']}
# fio = [{'Иванов Иван': ['897097','работник']}, {'Петров Петр': ['35346', 'не раб']}]
# fio = [{1: ["Иванов", "Иван","89234145", "работник"]}]
fio = {1: {'surname': "Иванов", 'name': "Иван", 'number': "89234145", 'discription': "работник"}}
# fio = [{'surname': "Иванов", 'name': "Иван", 'number': "89234145", 'discription': "работник"}]


rn = f'\n'
line = f'{"="*30}'

phonebook = {}
phonebook_last_id = 0




def create(db: dict, id: int, surname: str, name: str, phone: str, discription: str) -> tuple:           #data_base
    db[id] = {"surname": surname, 'name': name, 'phone': phone, 'discription': discription}
    id += 1
    return db, id


# def print_record(db: dict, _id: int):
#     print(f'{"="*30}\n{db[_id]}\n{"="*30}\n')
    # alternative:
    # if _id is not None:
    #     print(f'{"="*30}\n{db[_id]}\n{"="*30}\n')
    # else:
    #     print(f'{"="*30}\nЗапись не найдена!\n{"="*30}\n')


def get_user_data() -> tuple:
    surname = input("Введите фамилию: ")
    name = input("Введите имя: ")
    phone = input("Введите номер: ")
    discription = input("Введите описание: ")
    return surname, name, phone, discription


def get_surname() -> str:
    surname = input("Введите искомую фамилию: ")
    return surname


def print_data(db: dict, db_id: int = None, full: bool = False) -> None:
    rn = f'\n'
    line = f'{"="*30}'

    print(f'{rn}{line}')

    # copy_db = {}
    # if db_id is not None:
    #     copy_db[db_id] = db[db_id]
    #     db = copy_db

    for _id, data in db.items():
        if (db_id is not None and db_id == _id) or (db_id is None and full == True):
            print(f"[{_id}: {data['surname']} | {data['name']} | {data['phone']} | {data['discription']}]")
        else:
            print(f'Запись не найдена!')
            break

    print(f'{line}{rn}')


# 3) экспорт данных в текстовый файл формата csv
def export_db(db: dict, filepath: str, delimeter: str = '#') -> None:
    with open(filepath, "w", encoding='utf-8') as file:
        for _id, data in db.items():
            file.write(f"{data['surname']}{delimeter}{data['name']}{delimeter}{data['phone']}{delimeter}{data['discription']}\n")


def get_file_name() -> str:
    return input("Введите имя файла: ") or 'PhoneDB.csv'


# 4) импорт данных из текстового файла формата csv
def import_db(db: dict, last_id: int, filepath: str, delimeter: str = '#') -> tuple:
    with open(filepath, "r", encoding='utf-8') as file:
        for line in file:
            # data['surname']},{data['name']},{data['phone']},{data['discription']}
            _data = line.strip().split(delimeter)
            db[last_id] = {"surname": _data[0], 'name': _data[1], 'phone': _data[2], 'discription': _data[3]}
            last_id += 1
    return db, last_id


# 5) Read: он же Select. Выбор записей, удовлетворяющих заданном фильтру: по первой части фамилии человека. Берем первое совпадение по фамилии.
def read(db: dict, surname_filter: str) -> int:
    for _id in db:
        if surname_filter.lower() in db[_id]['surname'].lower():
            return _id


# def create_menu(db: dict, last_id: int) -> None:
#     menu_dict = {}
#     menu_dict = {'id': 1, 'name': 'Создать запись (Create)', 'func': get_user_data}
#     menu_dict = {'id': 2, 'name': 'Найти контакт (Select)', 'func': read, 'attrib': {'db': db, 'surname_filter': get_surname()}}
#     menu_dict = {'id': 3, 'name': 'Вывести имеющиеся данные (Read)', 'func': print_data, 'attrib': {'db': db, 'full': True}}
#     menu_dict = {'id': 4, 'name': 'Экспортировть данные в файл csv', 'func': export_db, 'attrib': {'db': db, 'filepath': get_file_name()}}
#     menu_dict = {'id': 5, 'name': 'Импортировать данные из файла csv', 'func': import_db, 'attrib': {'db': db, 'last_id': last_id, 'filepath': get_file_name()}}

#     print(menu_dict)
#     raise NotImplementedError


def menu(db: dict, last_id: int) -> None:
    # create_menu(db, last_id)

    while True:#Create, Read, Update, Delete
        print(f"Возможные действия:")
        print(f"1. Создать запись (Create)")
        print(f"2. Вывести имеющиеся данные (Read)")
        print(f"3. Экспортировть данные в файл")
        print(f"4. Импортировать данные из файла")
        print(f"5. Найти контакт")
        print(f"6. Выход")
        user_input = input("Введите номер действия: ")
        if user_input == "1":
            record = get_user_data()
            db, last_id = create(db, last_id, *record)
        elif user_input == "2":
            print_data(db, full=True)
        elif user_input == "3":
            export_db(db, get_file_name())
        elif user_input == "4":
            try:
                db, last_id = import_db(db, last_id, get_file_name())
            except FileNotFoundError:
                print(f'{rn}{line}{rn}Файл не найден!{rn}{line}{rn}')
        elif user_input == "5":
            found_id = read(db, get_surname())
            # try:
                # print_record(db, found_id)
            print_data(db, found_id)
            # except KeyError:
            #     print(f'{rn}{line}{rn}Запись не найдена!{rn}{line}{rn}')

        else:
            break


menu(phonebook, phonebook_last_id)
