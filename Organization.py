from EmployeeDATA import EmployeeDATA


class Organization:
    dict = {}

    @staticmethod
    def print_employee_data(empl):
        print('ФИО: ' + empl.fullname)
        print('Должность: ' + empl.post)
        print('Год рождения: ' + empl.birth_year)
        print('Зарплата: ' + empl.payment + '\n')

    def find_employee(self, fullname):
        organization = self.dict
        search = []
        for name in organization.keys():
            if name == fullname:
                search = organization[name]

        search_len = search.__len__()
        search_result = EmployeeDATA()
        if search_len == 0:
            print('Такого сотрудника не найдено.')
            return search_result
        elif search_len > 1:
            print('Найдено больше одного сотрудника с таким именем:')
            count = 1
            for empl in search:
                print(count)
                count += 1
                self.print_employee_data(empl)
            print('Выберите номер искомого сотрудника:')
            try:
                number = int(input())
            except ValueError:
                print('ОШИБКА: Неверный номер')
                return search_result
            try:
                search_result = search[number - 1]
            except IndexError:
                print('ОШИБКА: Неверный номер')
                return search_result
        else:
            search_result = search[0]

        return search_result

    def add_employee(self):
        print('ДОБАВИТЬ СОТРУДНИКА')
        organization = self.dict
        new_empl_data = EmployeeDATA()
        print('Введите фамилию, имя, отчество сотрудника через пробелы:')
        fullname = input()
        new_empl_data.fullname = fullname
        print('Введите должность сотрудника:')
        new_empl_data.post = input()
        print('Введите год рождения сотрудника:')
        new_empl_data.birth_year = input()
        print('Введите зарплату сотрудника:')
        new_empl_data.payment = input()

        if not organization.keys().__contains__(fullname):
            organization.update({fullname: [new_empl_data]})
        else:
            organization[fullname].append(new_empl_data)

        print('СОТРУДНИК ДОБАВЛЕН')

    def delete_employee(self):
        print('УДАЛИТЬ СОТРУДНИКА')
        organization = self.dict
        print('Введите фамилию, имя, отчество сотрудника через пробелы:')

        fullname = input()
        search_result = self.find_employee(fullname)
        for name in organization.keys():
            if name == search_result.fullname:
                organization[name].remove(search_result)
                print('СОТРУДНИК УДАЛЁН')

    def get_employee_data(self):
        print('ДАННЫЕ СОТРУДНИКА')
        organization = self.dict
        print('Введите фамилию, имя, отчество сотрудника через пробелы:')

        fullname = input()
        search = []

        for name in organization.keys():
            if name == fullname:
                search = organization[name]

        if search.__len__() >= 1:
            for empl in search:
                self.print_employee_data(empl)
        else:
            print('Такого сотрудника не найдено.')

    def change_employee(self):
        organization = self.dict
        print('Введите фамилию, имя, отчество сотрудника через пробелы:')

        fullname = input()
        search_result = self.find_employee(fullname)

        if not organization.keys().__contains__(search_result.fullname):
            return

        for empl in organization[search_result.fullname]:
            if empl == search_result:
                print('1 - изменить должность\n'
                      '2 - изменить год рождения\n'
                      '3 - изменить зарплату\n')
                user_choice = input()
                if user_choice == '1':
                    print('Введите новую должность:')
                    empl.post = input()
                elif user_choice == '2':
                    print('Введите новый год рождения:')
                    empl.birth_year = input()
                elif user_choice == '3':
                    print('Введите новую зарплату:')
                    empl.payment = input()
                else:
                    print('ОШИБКА: Неверная команда')
                    return

        print('ИЗМЕНЕНИЯ ВНЕСЕНЫ')

    def print_employees(self):
        organization = self.dict
        for name in organization.keys():
            for empl in organization[name]:
                self.print_employee_data(empl)

