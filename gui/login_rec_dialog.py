from PyQt5 import QtWidgets
from gui.forms.login_rec_dialog_form import Ui_LoginRecDialog


class LoginRecDialog(QtWidgets.QDialog, Ui_LoginRecDialog):
    def __init__(self, parent_):
        super().__init__(parent_)
        self.setupUi(self)
        self.parent = parent_
        self.okBtn.clicked.connect(self.returnLogin)

    def returnLogin(self):
        self.parent.setLogin(self.loginLine.text(), self)
        self.accept()

    def clear(self):
        self.loginLine.clear()
