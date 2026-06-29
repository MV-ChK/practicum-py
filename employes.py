class Employee:
    vacation_days = 28

    def __init__(self, first_name, second_name, gender):
        self.first_name = first_name
        self.second_name = second_name
        self.gender = gender
        self.remaining_vacation_days = Employee.vacation_days

    def consume_vacation(self, days):
        self.remaining_vacation_days -= days

    def get_vacation_details(self):
        return f'Остаток отпускных дней: {self.remaining_vacation_days}.'


class FullTimeEmployee(Employee):

    def get_unpaid_vacation(self, date, count_days):
        return f"Начало неоплачиваемого отпуска: {date}, продолжительность: {count_days} дней."


class PartTimeEmployee(Employee):
    vacation_days = 14

    def __init__(self, first_name, second_name, gender):
        super().__init__(first_name, second_name, gender)
        self.remaining_vacation_days = PartTimeEmployee.vacation_days


full_time_employee = FullTimeEmployee('Роберт', 'Крузо', 'м')
print(full_time_employee.get_unpaid_vacation('2023-07-01', 5))
part_time_employee = PartTimeEmployee('Алёна', 'Пятницкая', 'ж')
print(part_time_employee.get_vacation_details())

# В ОднойБольшойИзвестнойКомпании, для которой вы разрабатываете систему учёта
# отпусков,
# есть сотрудники с полной и частичной занятостью — фултаймеры и парт-таймеры.
# И фултаймеры, и парт-таймеры могут взять оплачиваемый отпуск:
# оплачиваемый отпуск у фултаймера — 28 дней,
# оплачиваемый отпуск у парт-таймера — 14 дней.
# Фултаймеры, кроме оплачиваемого отпуска, могут взять также неоплачиваемый.
# Напишите программу, которая управляет данными о сотрудниках и их отпусках.
# Что нужно сделать:
# Опишите классы FullTimeEmployee и PartTimeEmployee, они должны наследоваться
# от Employee.
# Экземпляры этих классов должны хранить данные о сотрудниках (имя, пол и
# доступное для сотрудника количество дней отпуска).
# В класс FullTimeEmployee добавьте метод get_unpaid_vacation(). Этот метод
# должен:
# принимать два параметра: дату начала неоплачиваемого отпуска (строка) и
# необходимое количество дней (целое число);
# возвращать сообщение в формате: 'Начало неоплачиваемого отпуска: <дата>,
# продолжительность: <число> дней.'.
# В классе PartTimeEmployee переопределите атрибут vacation_days. Его значение
# по умолчанию должно быть 14.
# В конце прекода описаны экземпляры обоих классов. При желании перед
# отправкой кода на проверку запустите код и
# проверьте работу новых методов и атрибутов
