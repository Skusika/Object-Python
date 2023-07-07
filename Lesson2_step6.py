# class BankAccount:
#     def __init__(self, account_number, balance):
#         self._account_number = account_number
#         self._balance = balance
#
#     def get_account_number(self):
#         return self._account_number
#
#     def get_balance(self):
#         return self._balance
#
#     def set_balance(self, count):
#         self._balance = count
#
# # Ниже код для проверки методов класса BankAccount
# account = BankAccount("1234567890", 1000)
# assert account._balance == 1000
# assert account._account_number == "1234567890"
# assert account.get_account_number() == "1234567890"
# assert account.get_balance() == 1000
# account.set_balance(1500)
# assert account.get_balance() == 1500
#
# print('Good')


class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    def __get_salary(self):
        return self.__salary

    def __get_name(self):
        return self.__name

    def __set_salary(self, number):
        if isinstance(number, (float, int)) and number > 0:
            self.__salary = number
        else:
            print(f"ErrorValue:{number}")

    title = property(fget=__get_name)
    reward = property(fget=__get_salary, fset=__set_salary)
