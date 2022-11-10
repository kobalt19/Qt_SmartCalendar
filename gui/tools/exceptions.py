class LoginNotFound(Exception):
    def __str__(self):
        return 'Такой пользователь не найден. Попробуйте зарегистрироваться'


class IncorrectPassword(Exception):
    def __str__(self):
        return 'Неправильный пароль. Попробуйте ещё раз'


class PasswordError(Exception):
    pass


class IncorrectChars(PasswordError):
    def __str__(self):
        return 'В пароле могут содержаться только латинские буквы (заглавные и строчные) ' \
               'и цифры!'


class NoASCII(PasswordError):
    def __str__(self):
        return 'В пароле должны содержаться латинские буквы (заглавные и строчные)!'


class OnlyUpper(PasswordError):
    def __str__(self):
        return 'В пароле должны быть строчные латинские буквы!'


class OnlyLower(PasswordError):
    def __str__(self):
        return 'В пароле должны быть заглавные латинские буквы!'


class NoDigits(PasswordError):
    def __str__(self):
        return 'В пароле должны содержаться цифры!'


class TooShort(PasswordError):
    def __str__(self):
        return 'Пароль слишком короткий, менее 8 символов!'
