from PyQt5 import QtCore, QtGui, QtWidgets
from .forms.login_dialog_form import Ui_LoginDialog


class LoginDialog(QtWidgets.QDialog, Ui_LoginDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.loginBtn.clicked.connect(self.login)
        self.regBtn.clicked.connect(self.register)
        self.recBtn.clicked.connect(self.recover)

    def login(self):
        pass

    def register(self):
        pass

    def recover(self):
        pass
