import sys
from PyQt5 import QtCore, QtWidgets
from gui.login_dialog import LoginDialog
from gui.forms.main_window_form import Ui_MainWindow
from gui.tools.db_tools import *
from gui.tools.event import Event
from gui.tools.exceptions import *
from gui.tools.user import User


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.users = set()
        self.current_user = None
        self.loginDialog = LoginDialog(self)
        self.loginDialog.exec()
        self.addEventBtn.clicked.connect(self.addEvent)
        # self.returnDateBtn.clicked.connect(self.returnDate)
        self.deleteEventBtn.clicked.connect(self.deleteEvents)
        self.messageTimer = QtCore.QTimer(self)
        self.messageTimer.setInterval(2500)
        self.messageTimer.timeout.connect(self.hideBar)
        self.events = []
        self.updateListWidget()

    def login(self, user):
        self.users.add(user)
        self.current_user = user
        self.events = db_get_events(self.current_user.get_id())

    def updateListWidget(self):
        self.listWidget.clear()
        for event in self.events:
            self.listWidget.addItem(str(event))

    def addEvent(self):
        date_string = self.calendarWidget.selectedDate().toString(format=QtCore.Qt.ISODate)
        time_string = self.timeEdit.time().toString(format=QtCore.Qt.ISODate)
        dt = f'{date_string} {time_string}'
        text = self.lineEdit.text()
        short_note = f'{dt} - {text}'
        if short_note in map(str, self.events):
            self.statusBar.showMessage('Нельзя добавлять одинаковые события!')
            self.statusBar.setStyleSheet('background-color: #ff0000;')
            self.messageTimer.start()
            return
        res = db_add_event(self.current_user.get_id(), text, dt)
        assert res, ''
        self.statusBar.showMessage(f'Событие успешно добавлено, его текст: {self.lineEdit.text()}')
        self.statusBar.setStyleSheet('background-color: #00ff00;')
        self.messageTimer.start()
        _id = db_search_event(self.current_user.get_id(), dt, text)
        self.events.append(Event(dt, text, _id, self.current_user.get_id()))
        self.updateListWidget()

    def deleteEvents(self):
        res = db_delete_event(self.listWidget.selectedItems())
        assert res, ''
        self.statusBar.showMessage('Событие успешно удалено')
        self.statusBar.setStyleSheet('background-color: #00ff00;')
        self.messageTimer.start()
        for event in self.events:
            if str(event) in self.listWidget.selectedItems():
                self.events.remove(event)
        self.updateListWidget()

    def hideBar(self):
        self.statusBar.showMessage('')
        self.statusBar.setStyleSheet('')

    def error(self):
        pass


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec())
