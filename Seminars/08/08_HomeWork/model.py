import os
from os.path import join
from typing import List, Any

import config


# TODO:
#  разобраться, либо это view, либо все же model. В данный момент вынесено
#  во view т.к. имеет отношение к отображению интерфейса пользователя
#
# import dict_menu_languages as dmt
#
#
# def get_menu(lang: str) -> dict:
#     return dmt.menu_text[lang]
#
#
# def change_language():
#     return {str(index + 1): key for index, key in enumerate(dmt.message_text)}
#
#
# def get_interface_messages(lang: str) -> dict:
#     return dmt.message_text[lang]


def get_full_file_path(path: str) -> str:
    return join(config.MAIN_DIR, path)


def file_exists(path: str) -> bool:
    return os.path.exists(path)


def create_db_file(path: str, data: list = None, delimiter: str = config.CSV_DELIMITER) -> None:
    rn = '\n'
    if data is None:
        data = []
    with open(path, "w", encoding='utf-8') as file:
        for row in data:
            if 'last_name' and 'first_name' and 'phone' and 'description' in row:
                file.write(
                    f"{row['last_name'].strip().replace(delimiter, '')}{delimiter}"
                    f"{row['first_name'].strip().replace(delimiter, '')}{delimiter}"
                    f"{row['phone'].strip().replace(delimiter, '')}{delimiter}"
                    f"{row['description'].strip().replace(delimiter, '')}{rn}"
                )


def get_data_from_file(path: str, delimiter: str = config.CSV_DELIMITER, create_file_db: bool = False) -> list:
    """
    Getting data from a file
    :param path: path to database file
    :param delimiter: separator in csv file
    :param create_file_db: create an empty database file
    :return: returns a list of dictionaries with data
    """
    if not file_exists(path):
        if create_file_db:
            create_db_file(path)
        return []
    with open(path, "r", encoding='utf-8') as file:
        data = [el.strip().split(delimiter) for el in file]
        db = [
            {'last_name': last_name, 'first_name': first_name, 'phone': phone, 'description': description}
            for last_name, first_name, phone, description in data
        ]
    return db


def db_length(db: list) -> int:
    return len(db)


def add_data_to_db(db: list, new_data: list) -> None:
    for row in new_data:
        db.append(row)


def get_search_in_db(db: list, search: str = None, where: str = None) -> list:
    if search is None or not search or where is None:
        return []
    search = search.lower()
    return [data for data in db if search in data[where].lower()]


def update_data_in_db(db: list):
    pass


def delete_data_from_db(db: list, str_number: str) -> bool:
    if not str_number.isdigit():
        return False
    str_number = int(str_number) - 1
    if not db[str_number]:
        return False
    db.remove(str_number)
    return True


def exit_program() -> None:
    exit()
