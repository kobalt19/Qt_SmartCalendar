from PyQt5 import QtCore, QtGui, QtWidgets
from gui.tools.db_tools import *
from gui.tools.diff_tools import *
from gui.tools.exceptions import *
from gui.tools.user import User
from gui.forms.rec_answ_dialog_form import Ui_RecAnswDialog
from gui.login_rec_dialog import LoginRecDialog

STEP = 17


class RecAnswDialog(QtWidgets.QDialog, Ui_RecAnswDialog):
    def __init__(self, parent_):
        super().__init__(parent_)
        self.parent = parent_
        self.setupUi(self)
        self.user = None
        LoginRecDialog(self).exec()
        self.label.setText(decrypt(db_get_query(self.user.get_login()), STEP))
        self.answBtn.clicked.connect(self.answer)

    def setLogin(self, login, login_dialog):
        try:
            user_data = db_get_user_data(login)
            self.user = User(encrypt(login, STEP), *user_data)
            return True
        except LoginNotFound:
            login_dialog.clear()
            msg_box = QtWidgets.QMessageBox(self)
            msg_box.setWindowTitle('Ошибка!')
            msg_box.setText('Такой пользователь не зарегистрирован!')
            msg_box.exec()
            return False

    def answer(self):
        answ = self.answLine.text()
        res = db_check_answer(self.user.get_login(), encrypt(answ, STEP))
        if res:
            self.parent.setLogin(self.user.get_login())
            self.accept()
        else:
            msg_box = QtWidgets.QMessageBox(self)
            msg_box.setWindowTitle('Ошибка!')
            msg_box.setText('Вы неправильно ответили на контрольный вопрос!')
            msg_box.exec()
            self.answLine.clear()
