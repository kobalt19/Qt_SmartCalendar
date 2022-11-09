from PyQt5 import QtCore, QtGui, QtWidgets
from gui.forms.login_dialog_form import Ui_LoginDialog
from gui.tools.db_tools import *
from gui.tools.user import User

STEP = 17


class LoginDialog(QtWidgets.QDialog, Ui_LoginDialog):
    def __init__(self, mw):
        super().__init__()
        self.setupUi(self)
        self.mw = mw
        self.loginBtn.clicked.connect(self.login)
        self.regBtn.clicked.connect(self.register)
        self.recBtn.clicked.connect(self.recover)

    def login(self):
        username = self.loginLine.text()
        passwd = self.passwdLine.text()
        try:
            res = db_login(encrypt(username, STEP), encrypt(passwd, STEP))
            self.mw.login(User(encrypt(username, STEP), encrypt(passwd, STEP), res))
            self.reject()
        except (LoginNotFound, IncorrectPassword) as err:
            error_message = QtWidgets.QMessageBox(self)
            error_message.setWindowTitle('Ошибка!')
            error_message.setText(str(err))
            error_message.exec()

    def register(self):
        pass

    def recover(self):
        pass