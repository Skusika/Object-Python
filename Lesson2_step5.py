# class Library:
#     def __init__(self, book: list):
#         self.__books = book
#
#
#     def __check_availability(self, name):
#         if name in self.__books:
#             return True
#         else:
#             return False
#
#     def search_book(self, tra):
#         return self.__check_availability(tra)
#
#     def return_book(self, mas):
#         self.__books.append(mas)
#
#     def _checkout_book(self, kniga):
#         if kniga in self.__books:
#             self.__books.remove(kniga)
#             return True
#         else:
# #             return False


class Employee:
    def __init__(self,name, position, hours_worked, hourly_rate):
        self.name = name
        self.__position = position
        self.__hours_worked = hours_worked
        self.__hourly_rate = hourly_rate

    def __calculate_salary(self):
        self.salary = int(self.__hours_worked * self.__hourly_rate)
        return self.salary

    def _set_position(self, posit):
        self.__position = posit

    def get_position(self):
        return self.__position

    def get_salary(self):
        return self.__calculate_salary()

    def get_employee_details(self):
        return (f'Name: {self.name}, Position: {self.__position}, Salary: {self.get_salary()}')

employee = Employee("Джеки Чан", 'manager', 20, 40)
assert employee.name == 'Джеки Чан'
assert employee._Employee__hours_worked == 20
assert employee._Employee__hourly_rate == 40
assert employee._Employee__position == 'manager'
assert employee.get_position() == 'manager'
assert employee.get_salary() == 800
assert employee._Employee__calculate_salary() == 800
assert employee.get_employee_details() == 'Name: Джеки Чан, Position: manager, Salary: 800'
employee._set_position('Director')
assert employee.get_employee_details() == 'Name: Джеки Чан, Position: Director, Salary: 800'

employee_2 = Employee("Пирс Броснан", 'actor', 35, 30)
assert employee_2._Employee__calculate_salary() == 1050
assert employee_2.get_employee_details() == 'Name: Пирс Броснан, Position: actor, Salary: 1050'

print('Good')