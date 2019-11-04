# coding: utf8
import os
import sys
from special_serializer import SpecialSerializer
from organization import Organization


Filename = 'organization.txt'
Organization = Organization()


def remove_trash():
    keys = Organization.dict.copy().keys()
    for key in keys:
        if not Organization.dict[key]:
            Organization.dict.pop(key)


def exit_program():
    remove_trash()
    with open(Filename, 'w') as f:
        SpecialSerializer.write(Organization.dict, f)
    sys.exit()


def print_menu():
    print('1 - внести нового сотрудника в список\n'
          '2 - удалить сотрудника из списка\n'
          '3 - просмотреть данные о сотруднике\n'
          '4 - изменить данные о сотруднике\n'
          '5 - просмотреть весь список сотрудников\n'
          '6 - снова увидеть это меню\n'
          '7 - сохранить данные и прекратить выполнение программы\n')


Commands = {'1': Organization.add_employee, '2': Organization.delete_employee,
            '3': Organization.get_employee_data, '4': Organization.change_employee,
            '5': Organization.print_employees, '6': print_menu, '7': exit_program}


def program():
    global Organization
    if os.path.getsize(Filename) > 0:
        with open(Filename, 'r') as f:
            Organization.dict = SpecialSerializer.load(f)

    print_menu()

    while 1:
        user_input = input()
        if not Commands.__contains__(user_input):
            print('ОШИБКА: Неверная команда')
            continue

        Commands[user_input]()


if __name__ == '__main__':
    program()
