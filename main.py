import os
import sys
from SpecialSerializer import SpecialSerializer
from Organization import Organization


Filename = 'organization.txt'
org = Organization()


def remove_trash():
    keys = org.dict.copy().keys()
    for key in keys:
        if not org.dict[key]:
            org.dict.pop(key)


def exit_program():
    remove_trash()
    with open(Filename, 'w') as f:
        SpecialSerializer.write(org.dict, f)
    sys.exit()


def print_menu():
    print('1 - внести нового сотрудника в список\n'
          '2 - удалить сотрудника из списка\n'
          '3 - просмотреть данные о сотруднике\n'
          '4 - изменить данные о сотруднике\n'
          '5 - просмотреть весь список сотрудников\n'
          '6 - снова увидеть это меню\n'
          '7 - сохранить данные и прекратить выполнение программы\n')


commands = {'1': org.add_employee, '2': org.delete_employee,
            '3': org.get_employee_data, '4': org.change_employee,
            '5': org.print_employees, '6': print_menu, '7': exit_program}


def program():
    global org
    if os.path.getsize(Filename) > 0:
        with open(Filename, 'r') as f:
            org.dict = SpecialSerializer.load(f)

    print_menu()

    while 1:
        user_input = input()
        if not commands.__contains__(user_input):
            print('ОШИБКА: Неверная команда')
            continue

        commands[user_input]()


if __name__ == '__main__':
    program()
