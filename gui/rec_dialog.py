from PyQt5 import QtCore, QtGui, QtWidgets
from gui.tools.db_tools import *
from gui.tools.diff_tools import *
from gui.forms.rec_dialog_form import Ui_RecDialog
from gui.rec_answ_dialog import RecAnswDialog


class RecDialog(QtWidgets.QDialog, Ui_RecDialog):
    def __init__(self, parent_):
        super().__init__(parent_)
        self.setupUi(self)
        self.login = None
        RecAnswDialog(self).exec()
        self.doneBtn.clicked.connect(self.recover)

    def recover(self):
        if self.passwdLine.text() != self.passwdLine.text():
            msg_box = QtWidgets.QMessageBox(self)
            msg_box.setWindowTitle('Ошибка!')
            msg_box.setText('Пароли не совпадают!')
            msg_box.exec()
            return
        passwd = self.passwdLine.text()
        try:
            passwd_check(passwd)
        except PasswordError as err:
            msg_box = QtWidgets.QMessageBox(self)
            msg_box.setWindowTitle('Ошибка!')
            msg_box.setText(err)
            msg_box.exec()
            return
        else:
            db_change_passwd(self.login, encrypt(passwd, STEP))
            msg_box = QtWidgets.QMessageBox(self)
            msg_box.setWindowTitle('Готово!')
            msg_box.setText('Вы успешно сменили пароль!')
            msg_box.exec()
            self.accept()

    def setLogin(self, login):
        self.login = login
