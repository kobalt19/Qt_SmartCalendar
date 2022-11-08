import sys
from PyQt5 import QtCore, QtWidgets
from .forms.main_window_form import Ui_MainWindow
from gui.event_delete_dialog import DeleteDialog
from .tools.db_update import *


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        name, ok_pressed = QtWidgets.QInputDialog.getText(self, 'Введите имя', 'Как вас зовут?')
        if ok_pressed:
            res = check_and_add_user(name)
            assert res
            self.user_id = res
        self.addEventBtn.clicked.connect(self.addEvent)
        # self.returnDateBtn.clicked.connect(self.returnDate)
        self.deleteEventBtn.clicked.connect(self.showDeleteDialog)
        self.messageTimer = QtCore.QTimer(self)
        self.messageTimer.setInterval(2500)
        self.messageTimer.timeout.connect(self.hideBar)
        self.events = []
        self.updateListWidget()

    def updateListWidget(self):
        self.listWidget.clear()
        for event in self.events:
            self.listWidget.addItem(event)

    def addEvent(self):
        date_string = self.calendarWidget.selectedDate().toString(format=QtCore.Qt.ISODate)
        time_string = self.timeEdit.time().toString(format=QtCore.Qt.ISODate)
        dt = f'{date_string} {time_string}'
        res = add_event(self.user_id, self.lineEdit.text(), dt)
        assert res
        self.statusBar.showMessage('Ваше событие успешно добавлено')
        self.statusBar.setStyleSheet('background-color: #00ff00;')
        self.messageTimer.start()
        self.events.append(f'{dt} - {self.lineEdit.text()}')
        self.updateListWidget()

    def showDeleteDialog(self):
        dialog = DeleteDialog(self.events)
        dialog.exec()
        to_delete = dialog.getEvents()
        for event in to_delete:
            self.events.remove(event)
        res = delete_event(to_delete)
        self.updateListWidget()

    def hideBar(self):
        self.statusBar.showMessage('')
        self.statusBar.setStyleSheet('')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec())
