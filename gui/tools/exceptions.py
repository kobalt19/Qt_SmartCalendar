class LoginNotFound(Exception):
    def __str__(self):
        return 'Такой пользователь не найден. Попробуйте зарегистрироваться'


class IncorrectPassword(Exception):
    def __str__(self):
        return 'Неправильный пароль. Попробуйте ещё раз'
