import dict_menu_languages as dmt


def get_menu(lang: str) -> dict:
    return dmt.menu_text[lang]


def change_language():
    return {str(index + 1): key for index, key in enumerate(dmt.message_text)}


def get_interface_messages(lang: str) -> dict:
    return dmt.message_text[lang]


def view_menu(menu: dict, title: str = '') -> None:
    indent = 4
    print(char_line())
    print(title)
    for num, descript in menu.items():
        print(f'{" " * indent}{num}. {descript}')


def get_user_response(request: str) -> str:
    return input(f'{request}: ')


def send_message(msg: str) -> None:
    print(f'{char_line()}{msg}')


def view_data_from_db(db: list) -> None:
    for index, row in enumerate(db):
        print(f"{index+1:4} | {row['last_name']:16} | {row['first_name']:16} | {row['phone']:16} | {row['description']:70}")


def char_line(char: str = '=', char_count: int = 30) -> str:
    rn = '\n'
    return f'{rn}{char * char_count}{rn}{rn}'


