# class Robot:
#     population = 0
#     def __init__(self, name):
#         self.name = name
#         print(f'Робот {self.name} был создан')
#         Robot.population += 1
#
#     def destroy(self):
#         Robot.population -= 1
#         print(f'Робот {self.name} был уничтожен')
#
#     def say_hello(self):
#         print(f'Робот {self.name} приветствует тебя, особь человеческого рода')
#
#     @classmethod
#     def how_many(cls):
#         print(f'{Robot.population}, вот сколько нас еще осталось')
#
# droid1 = Robot("R2-D2")
# assert droid1.name == 'R2-D2'
# assert Robot.population == 1
# droid1.say_hello()
# Robot.how_many()
# droid2 = Robot("C-3PO")
# assert droid2.name == 'C-3PO'
# assert Robot.population == 2
# droid2.say_hello()
# Robot.how_many()
# droid1.destroy()
# assert Robot.population == 1
# droid2.destroy()
# assert Robot.population == 0
# Robot.how_many()

# class User:
#     def __init__(self, name, role):
#         self.name = name
#         self.role = role
#
# class Access:
#     __access_list = ['admin', 'developer']
#
#     @staticmethod
#     def __check_access(role):
#         return role in Access.__access_list
#
#     @staticmethod
#     def get_access(ex):
#         if not isinstance(ex, User):
#             print("AccessTypeError")
#         else:
#             if Access.__check_access(ex.role) == True:
#                 print(f'User {ex.name}: success')
#             else:
#                 print(f'AccsessDenied')
#
# user1 = User('batya99', 'admin')
# Access.get_access(user1) # печатает "User batya99: success"
#
# zaya = User('milaya_zaya999', 'user')
# Access.get_access(zaya) # печатает AccessDenied
#
# Access.get_access(5) # печатает AccessTypeError

class BankAccount:
    bank_name = "Tinkoff Bank"
    address = "Москва, ул. 2-я Хуторская, д. 38А"

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    @classmethod
    def create_account(cls, name, summa):
        return BankAccount(name, summa)

    @classmethod
    def bank_info(cls):
        return (f'{BankAccount.bank_name} is located in {BankAccount.address}')

oleg = BankAccount.create_account("Олег Тинкофф", 1000)
assert isinstance(oleg, BankAccount)
assert oleg.name == 'Олег Тинкофф'
assert oleg.balance == 1000
assert BankAccount.bank_info() == 'Tinkoff Bank is located in Москва, ул. 2-я Хуторская, д. 38А'

ivan = BankAccount.create_account("Ivan Reon", 50)
assert isinstance(ivan, BankAccount)
assert ivan.name == 'Ivan Reon'
assert ivan.balance == 50
print('Good')