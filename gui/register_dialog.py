from PyQt5 import QtCore, QtGui, QtWidgets
from gui.forms.register_dialog_form import Ui_RegisterDialog
from gui.tools.db_tools import *
from gui.tools.user import User


class RegisterDialog(QtWidgets.QDialog, Ui_RegisterDialog):
    def __init__(self, *args):
        super().__init__(*args)
        self.setupUi(self)
        self.loginBtn.clicked.connect(self.reject)
        self.regBtn.clicked.connect(self.register)

    def clear(self):
        for line in {self.loginLine, self.passwdLine,
                     self.passwdRepLine, self.queryLine, self.answLine}:
            line.clear()

    def register(self):
        username = self.loginLine.text()
        passwd = self.passwdLine.text()
        passwd_rep = self.passwdRepLine.text()
        query = self.queryLine.text()
        answ = self.answLine.text()
        if passwd != passwd_rep:
            error_message = QtWidgets.QMessageBox(self)
            error_message.setWindowTitle('Ошибка!')
            error_message.setText('Пароли не совпадают!')
            error_message.exec()
            self.clear()
        try:
            passwd_check(passwd)
        except PasswordError as err:
            error_message = QtWidgets.QMessageBox(self)
            error_message.setWindowTitle('Ошибка!')
            error_message.setText(f'Пароль не соответствует условиям. {err}')
            error_message.exec()
            self.clear()
        else:
            res = db_register(*(encrypt(line, STEP) for line in (username, passwd, query, answ)))
            if res:
                message = QtWidgets.QMessageBox(self)
                message.setWindowTitle('Поздравляем!')
                message.setText('Вы успешно зарегистрировались!')
                message.exec()
                self.accept()
            if not res:
                error_message = QtWidgets.QMessageBox(self)
                error_message.setWindowTitle('Ошибка!')
                error_message.setText('Пользователь с таким именем уже существует!')
                error_message.exec()
                self.clear()
