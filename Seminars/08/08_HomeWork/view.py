# TODO:
#  разобраться, либо get_menu(), get_language(), get_interface_messages() это view, либо все же model.
#  В данный момент вынесено во view т.к. имеет отношение к отображению интерфейса пользователя.

import dict_menu_languages as dmt


def get_menu(lang: str) -> dict:
    """
    Get menu localization.
    :param lang: language
    :return: dictionary with menu
    """
    return dmt.menu_text[lang]


def get_language() -> dict:
    """
    Get a dict of languages.
    :return: return a dictionary with the numbers and names of the available languages
    """
    return {str(index + 1): key for index, key in enumerate(dmt.message_text)}


def get_interface_messages(lang: str) -> dict:
    """
    Get a dictionary with the localization of program messages.
    :param lang: language
    :return: dictionary with the localization of program messages
    """
    return dmt.message_text[lang]


def view_menu(menu: dict, title: str = '') -> None:
    indent = 4
    char_space = ' '
    print(char_line())
    print(title)
    for num, descript in menu.items():
        print(f"{char_space * indent}{num}. {descript}")
    print()


def get_user_response(request: str) -> str:
    return input(f'{request}: ').strip()


def get_multiple_responses(**args: dict) -> dict:
    return {key: get_user_response(str(request)) for key, request in args.items()}


def send_message(msg: str) -> None:
    print(f'{char_line()}{msg}')


def view_data_from_db(db: list) -> None:
    char_line()
    for index, row in enumerate(db):
        print(f"{index + 1:4} | {row['last_name']:16} | {row['first_name']:16} | {row['phone']:16} | {row['description']:70}")
    print()


def char_line(char: str = '=', char_count: int = 30) -> str:
    rn = '\n'
    return f'{rn}{char * char_count}{rn}{rn}'


