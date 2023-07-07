# from string import ascii_letters
# from string import digits
# spisok = []
# with open("easy_passwords.txt", "r", encoding='utf-8') as file:
#     for elem in file:
#         spisok.append(elem.strip())
# file.close()
#
# class Registration:
#     def __init__(self, login, password):
#         self.login = login
#         self.password = password
#
#     @property
#     def login(self):
#         return self.__login
#
#     @login.setter
#     def login(self, value):
#         if not isinstance(value, str):
#             raise TypeError("Логин должен быть строкой")
#         elif value.count("@") == 0 or value.count("@") > 1:
#             raise ValueError("Должен быть один символ собаки")
#         elif "." not in value[value.rfind("@"): -1]:
#             raise ValueError("После символа @ должна быть точка")
#         else:
#             self.__login = value
#
#     @property
#     def password(self):
#         return self.__password
#
#     @staticmethod
#     def is_include_digit(password):
#         for digit in digits:
#             if digit in password:
#                 return True
#         return False
#
#     @staticmethod
#     def is_include_all_register(password):
#         for elem in password:
#             if elem.islower() or elem.isupper():
#                 return True
#         return False
#
#     @staticmethod
#     def is_include_only_latin(password):
#         for elem in password:
#             if elem in ascii_letters:
#                 return True
#         return False
#
#     @staticmethod
#     def check_password_dictionary(password):
#         for line in spisok:
#             if line == password:
#                 return True
#         return False
#
#     @password.setter
#     def password(self, value):
#         if not isinstance(value, str):
#             raise TypeError("Пароль должен быть строкой")
#         elif len(value) < 5 or len(value) > 11:
#             raise ValueError("Пароль должен быть длиннее 4 и меньше 12 символов")
#         elif not Registration.is_include_digit(value):
#             raise ValueError("Пароль должен содержать хотя бы одну цифру")
#         elif not Registration.is_include_all_register(value):
#             raise ValueError("Пароль должен содержать хотя бы один символ верхнего и нижнего регистра")
#         elif not Registration.is_include_only_latin(value):
#             raise ValueError("Пароль должен содержать только латинский алфавит")
#         elif Registration.check_password_dictionary(value):
#             raise ValueError("Ваш пароль содержится в списке самых легких")
#         else:
#             self.__password = value
#
# try:
#     s2 = Registration("fga", "asd12")
# except ValueError as e:
#     pass
# else:
#     raise ValueError("Registration('fga', 'asd12') как можно записать такой логин?")
#
# try:
#     s2 = Registration("fg@a", "asd12")
# except ValueError as e:
#     pass
# else:
#     raise ValueError("Registration('fg@a', 'asd12') как можно записать такой логин?")
#
# s2 = Registration("translate@gmail.com", "as1SNdf")
# try:
#     s2.login = "asdsa12asd."
# except ValueError as e:
#     pass
# else:
#     raise ValueError("asdsa12asd как можно записать такой логин?")
#
# try:
#     s2.login = "asdsa12@asd"
# except ValueError as e:
#     pass
# else:
#     raise ValueError("asdsa12@asd как можно записать такой логин?")
#
# assert Registration.check_password_dictionary('QwerTy123'), 'проверка на пароль в слове не работает'
#
# try:
#     s2.password = "QwerTy123"
# except ValueError as e:
#     pass
# else:
#     raise ValueError("QwerTy123 хранится в словаре паролей, как его можно было сохранить?")
#
#
# try:
#     s2.password = "KissasSAd1f"
# except ValueError as e:
#     pass
# else:
#     raise ValueError("KissasSAd1f хранится в словаре паролей, как его можно было сохранить?")
#
# try:
#     s2.password = "124244242"
# except ValueError as e:
#     pass
# else:
#     raise ValueError("124244242 пароль НЕОЧЕНЬ, как его можно было сохранить?")
#
# try:
#     s2.password = "RYIWUhjkdbfjfgdsffds"
# except ValueError as e:
#     pass
# else:
#     raise ValueError("RYIWUhjkdbfjfgdsffds пароль НЕОЧЕНЬ, как его можно было сохранить?")
#
# try:
#     s2.password = "CaT"
# except ValueError as e:
#     pass
# else:
#     raise ValueError("CaT пароль НЕОЧЕНЬ, как его можно было сохранить?")
#
# try:
#     s2.password = "monkey"
# except ValueError as e:
#     pass
# else:
#     raise ValueError("monkey пароль НЕОЧЕНЬ, как его можно было сохранить?")
#
# try:
#     s2.password = "QwerTy123"
# except ValueError as e:
#     pass
# else:
#     raise ValueError("QwerTy123 пароль есть в слове, нельзя его использовать")
#
# try:
#     s2.password = "HelloQEWq"
# except ValueError as e:
#     pass
# else:
#     raise ValueError("HelloQEWq пароль НЕОЧЕНЬ, как его можно было сохранить?")
#
# try:
#     s2.password = [4, 32]
# except TypeError as e:
#     pass
# else:
#     raise TypeError("Пароль должен быть строкой")
#
# try:
#     s2.password = 123456
# except TypeError as e:
#     pass
# else:
#     raise TypeError("Пароль должен быть строкой")
#
# print('U r hacked Pentagon')

class File:
    def __init__(self, name):
        self.name = name
        self.in_trash = False
        self.is_deleted = False

    def restore_from_trash(self):
        print(f'Файл {self.name} восстановлен из корзины')
        self.in_trash = False

    def remove(self):
        print(f'Файл {self.name} был удален')
        self.is_deleted = True

    def read(self):
        if self.is_deleted is True:
            print(f'ErrorReadFileDeleted({self.name})')
        elif self.in_trash is True:
            print(f'ErrorReadFileTrashed({self.name})')
        else:
            print(f'Прочитали все содержимое файла {self.name}')

    def write(self, content):
        if self.is_deleted is True:
            print(f'ErrorWriteFileDeleted({self.name})')
        elif self.in_trash is True:
            print(f'ErrorWriteFileTrashed({self.name})')
        else:
            print(f'Записали значение {content} в файл {self.name}')

class Trash:
    content = []

    @staticmethod
    def add(value):
        if not isinstance(value, File):
            print("В корзину добавлять можно только файл")
        else:
            Trash.content.append(value)
            value.in_trash = True


    @staticmethod
    def clear():
        print("Очищаем корзину")
        for elem in Trash.content:
            File.remove(elem)
        Trash.content.clear()
        print("Корзина пуста")

    @staticmethod
    def restore():
        print("Восстанавливаем файлы из корзины")
        for elem in Trash.content:
            File.restore_from_trash(elem)
        Trash.content.clear()
        print("Корзина пуста")







f1 = File('puppies.jpg')
assert f1.name == 'puppies.jpg'
assert f1.in_trash is False
assert f1.is_deleted is False

f1.read()  # Прочитали все содержимое файла puppies.jpg
f1.remove()  # Файл puppies.jpg был удален
assert f1.is_deleted is True
f1.read()  # ErrorReadFileDeleted(puppies.jpg)

passwords = File('pass.txt')
assert passwords.name == 'pass.txt'
assert passwords.in_trash is False
assert passwords.is_deleted is False

f3 = File('xxx.doc')

assert f3.__dict__ == {'name': 'xxx.doc', 'in_trash': False, 'is_deleted': False}
f3.read()
f3.remove()
assert f3.is_deleted is True
f3.read()
f3.in_trash = True
f3.is_deleted = False
f3.read()
f3.write('hello')
f3.restore_from_trash()
assert f3.in_trash is False
f3.write('hello')  # Записали значение «hello» в файл cat.jpg

f2 = File('cat.jpg')
f2.write('hello')  # Записали значение «hello» в файл cat.jpg
f2.write([1, 2, 3])  # Записали значение «hello» в файл cat.jpg
f2.remove()  # Файл cat.jpg был удален
f2.write('world')  # ErrorWriteFileDeleted(cat.jpg)
f1 = File('puppies.jpg')
f2 = File('cat.jpg')
f3 = File('xxx.doc')
passwords = File('pass.txt')

for file in [f1, f2, f3, passwords]:
    assert file.is_deleted is False
    assert file.in_trash is False

f3.read()
f3.remove()
assert f3.is_deleted is True
f3.read()
f3.write('hello')

assert Trash.content == []

Trash.add(f2)
Trash.add(passwords)
Trash.add(f3)

f1.read()
Trash.add(f1)
f1.read()

for file in [f1, f2, f3, passwords]:
    assert file.in_trash is True

for f in [f2, passwords, f3, f1]:
    assert f in Trash.content

Trash.restore()
assert Trash.content == [], 'После восстановления корзина должна была очиститься'

Trash.add(passwords)
Trash.add(f2)
Trash.add('hello')
Trash.add(f1)

for f in [passwords, f2, f1]:
    assert f in Trash.content


Trash.clear()

for file in [passwords, f2, f1]:
    assert file.is_deleted is True

assert Trash.content == [], 'После удаления файлов корзина должна была очиститься'

f1.read()









