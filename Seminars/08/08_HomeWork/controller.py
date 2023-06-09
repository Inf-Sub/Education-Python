import config
import model
import view


def controller(DEBUG: bool = False) -> None:
    """
    Program operation controller.
    :param DEBUG: True | False debug mode
    :return: None
    """
    is_change_data = False

    db_file = model.get_full_file_path(config.DATABASE)
    db = model.get_data_from_file(path=db_file, delimiter=config.CSV_DELIMITER, create_file_db=True)

    lang = config.DEFAULT_LANGUAGE
    messages = view.get_interface_messages(lang)
    if DEBUG:
        view.send_message(f"{messages['load_db_from_file']}{config.DATABASE}")

    while True:
        view.view_menu(menu=view.get_menu(lang), title=messages['title_menu'])

        selected = view.get_user_response(messages['enter_select_menu'])
        if DEBUG:
            view.send_message(f"{messages['menu_item_selected']}{selected}")
        # func_name = model.select_func_from_menu(selected)
        # # if func_name:
        # if callable(func_name):
        #     func_name(db)

        match selected:
            # 'Create'
            case "1":
                new_data = view.get_multiple_responses(
                    last_name=messages['enter_last_name'], first_name=messages['enter_first_name'],
                    phone=messages['enter_phone'], description=messages['enter_description']
                )
                if new_data['last_name'] or new_data['first_name'] or new_data['phone']:
                    model.add_data_to_db(db=db, new_data=[new_data])
                    is_change_data = True

            # 'Read'
            case "2":
                search = view.get_user_response(messages['search_last_name'])
                search_user = model.get_search_in_db(db=db, search=search, where='last_name')
                view.view_data_from_db(search_user)

            # 'Update'
            case "3":
                view.view_data_from_db(db)
                str_number = view.get_user_response(messages['enter_record_number_to_update'])
                new_data = view.get_multiple_responses(
                    last_name=messages['enter_last_name'], first_name=messages['enter_first_name'],
                    phone=messages['enter_phone'], description=messages['enter_description']
                )
                update_result = model.update_data_in_db(db=db, str_number=str_number, new_data=new_data)
                if update_result:
                    view.send_message(messages['entry_updated'])
                    is_change_data = True
                else:
                    view.send_message(messages['entry_not_updated'])

            # 'Delete'
            case "4":
                view.view_data_from_db(db)
                str_number = view.get_user_response(messages['enter_record_number_to_delete'])
                deletion_result = model.delete_data_from_db(db=db, str_number=str_number)
                if deletion_result:
                    view.send_message(messages['entry_removed'])
                    is_change_data = True
                else:
                    view.send_message(messages['entry_not_removed'])



            # 'View DB'
            case "5":
                view.view_data_from_db(db)
                view.send_message(f"{messages['total_rec_in_db']}{model.db_length(db)}")

            # 'Import from file'
            case "6":
                import_db_file = view.get_user_response(messages['import_data_file_name'])
                import_db_file = model.get_full_file_path(import_db_file)

                import_db_delimiter = view.get_user_response(messages['import_data_file_delimiter'])
                import_db_delimiter = import_db_delimiter if import_db_delimiter else config.CSV_DELIMITER

                new_data = model.get_data_from_file(path=import_db_file, delimiter=import_db_delimiter)
                model.add_data_to_db(db=db, new_data=new_data)

                is_change_data = True

            # 'Export to file'
            case "7":
                export_db_file = view.get_user_response(messages['export_data_file_name'])
                export_db_file = model.get_full_file_path(export_db_file)

                export_db_delimiter = view.get_user_response(messages['export_data_file_delimiter'])
                export_db_delimiter = export_db_delimiter if export_db_delimiter else config.CSV_DELIMITER

                model.create_db_file(path=export_db_file, data=db, delimiter=export_db_delimiter)

            # 'Language'
            case "8":
                dict_lang = view.get_language()
                view.view_menu(menu=dict_lang, title=messages['title_menu_language'])
                selected_lang = view.get_user_response(messages['enter_select_menu'])
                if selected_lang in dict_lang:
                    lang = dict_lang[selected_lang]

            # 'Exit'
            case "0":
                while is_change_data:
                    save = view.get_user_response(messages['save_data'])
                    if save.lower() in 'yнnт':
                        is_change_data = False
                    if save.lower() in 'yн':
                        model.create_db_file(path=db_file, data=db, delimiter=config.CSV_DELIMITER)
                        view.send_message(messages['save_data_complete'])

                view.send_message(messages['goodbye'])
                model.exit_program()

            case _:
                view.send_message(messages['input_incorrect'])


if __name__ == "__main__":
    pass
