import sqlite3
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from form import Ui_MainWindow
import db.db_update


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        name, ok_pressed = QtWidgets.QInputDialog.getText(self, 'Введите имя', 'Как вас зовут?')
        if ok_pressed:
            res = db.db_update.check_and_add_user(name)
            assert res
            self.user_id = res
        self.addEventBtn.clicked.connect(self.addEvent)
        # self.returnDateBtn.clicked.connect(self.returnDate)
        self.messageTimer = QtCore.QTimer(self)
        self.messageTimer.setInterval(2500)
        self.messageTimer.timeout.connect(self.hideBar)

    def addEvent(self):
        date_string = self.calendarWidget.selectedDate().toString(format=QtCore.Qt.ISODate)
        time_string = self.timeEdit.time().toString(format=QtCore.Qt.ISODate)
        dt = f'{date_string} {time_string}'
        res = db.db_update.add_event(self.user_id, self.lineEdit.text(), dt)
        assert res
        self.statusBar.showMessage('Ваше событие успешно добавлено')
        self.statusBar.setStyleSheet('background-color: #00ff00;')
        self.messageTimer.start()

    def hideBar(self):
        self.statusBar.showMessage('')
        self.statusBar.setStyleSheet('')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec())
