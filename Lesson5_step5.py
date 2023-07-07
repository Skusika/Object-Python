
class PasswordInvalidError(Exception):
    pass
class PasswordLengthError(PasswordInvalidError):
    def __str__(self):
        return f'Пароль должен быть не менее 8 символов'

class PasswordContainUpperError(PasswordInvalidError):
    def __str__(self):
        return f'Пароль должен содержать хотя бы одну заглавную букву'

class PasswordContainDigitError(PasswordInvalidError):
    def __str__(self):
        return f'Пароль должен содержать хотя бы одну цифру'

class User:
    def __init__(self, username, password=None):
        self.username = username
        self.password = password

    def set_password(self, s):
        counter = 0
        digits = 0
        for i in s:
            if i.isdigit():
                digits += 1
        for i in s:
            if i.isupper():
                counter += 1

        if len(s) >= 8:
            if counter > 0:
                if digits > 0:
                    self.password = s
                else:
                    raise PasswordContainDigitError
            else:
                raise PasswordContainUpperError
        else:
            raise PasswordLengthError

# Ниже код для проверки


assert issubclass(PasswordInvalidError, Exception)
assert issubclass(PasswordLengthError, PasswordInvalidError)
assert issubclass(PasswordContainUpperError, PasswordInvalidError)
assert issubclass(PasswordContainDigitError, PasswordInvalidError)

user = User("johndoe")

try:
    user.set_password("weakpwd")
except PasswordLengthError as e:
    print(e)

try:
    user.set_password("strongpassword8")
except PasswordContainUpperError as e:
    print(e)

try:
    user.set_password("Safepassword")
except PasswordContainDigitError as e:
    print(e)

user.set_password("SecurePass123")
assert user.password == 'SecurePass123'






