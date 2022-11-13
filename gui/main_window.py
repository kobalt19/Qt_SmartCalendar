import pymorphy2
from PyQt5 import QtCore, QtWidgets
from gui.login_dialog import LoginDialog
from gui.forms.main_window_form import Ui_MainWindow
from gui.tools.db_tools import *
from gui.tools.event import Event

morph = pymorphy2.MorphAnalyzer()
STEP = 17


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.users = set()
        self.events = []
        self.current_user = None
        LoginDialog(self).exec()
        self.addEventBtn.clicked.connect(self.addEvent)
        self.returnDateBtn.clicked.connect(self.returnDate)
        self.deleteEventBtn.clicked.connect(self.deleteEvents)
        self.userChangeBtn.clicked.connect(self.changeUser)
        self.messageTimer = QtCore.QTimer(self)
        self.setupMessageTimer()
        self.eventTimer = QtCore.QTimer(self)
        self.setupEventTimer()
        self.baseTimer = QtCore.QTimer(self)
        self.setupBaseTimer()
        self.refreshListWidgetTimer = QtCore.QTimer(self)
        self.setupRefreshListWidgetTimer()
        self.refresh()
        self.refreshListWidget()

    def returnDate(self):
        self.calendarWidget.setSelectedDate(QtCore.QDate.currentDate())

    def refresh(self):
        login = decrypt(self.current_user.get_login(), STEP)
        self.currentUserLabel.setText(f'Логин: {login}')

    def setupBaseTimer(self):
        self.baseTimer.setInterval(1000)
        self.baseTimer.timeout.connect(self.refresh)
        self.baseTimer.start()

    def setupMessageTimer(self):
        self.messageTimer.setInterval(2500)
        self.messageTimer.timeout.connect(self.hideBar)

    def setupEventTimer(self):
        self.eventTimer.setInterval(5000)
        self.eventTimer.timeout.connect(self.checkEvents)
        self.eventTimer.start()

    def setupRefreshListWidgetTimer(self):
        self.refreshListWidgetTimer.setInterval(30000)
        self.refreshListWidgetTimer.timeout.connect(self.refreshListWidget)
        self.refreshListWidgetTimer.start()

    def login(self, user):
        self.users.add(user)
        self.current_user = user
        self.events = db_get_events(self.current_user.get_id())

    def refreshListWidget(self):
        self.listWidget.clear()
        for event in self.events:
            self.listWidget.addItem(str(event))

    def changeUser(self):
        self.close()
        self.messageTimer.stop()
        self.eventTimer.stop()
        self.baseTimer.stop()
        self.refreshListWidgetTimer.stop()
        self.__init__()
        self.show()

    def addEvent(self):
        date_string = self.calendarWidget.selectedDate().toString(format=QtCore.Qt.ISODate)
        time_string = self.timeEdit.time().toString(format=QtCore.Qt.ISODate)
        dt = f'{date_string} {time_string}'
        if get_datetime(dt) < datetime.datetime.now():
            self.statusBar.showMessage('Можно добавлять только будущие события!')
            self.statusBar.setStyleSheet('background-color: #ff0000;')
            self.messageTimer.start()
            return
        text = self.lineEdit.text()
        if db_check_for_event(self.current_user.get_id(), dt, text):
            self.statusBar.showMessage('Нельзя добавлять одинаковые события!')
            self.statusBar.setStyleSheet('background-color: #ff0000;')
            self.messageTimer.start()
            return
        res = db_add_event(self.current_user.get_id(), text, dt)
        if not res:
            self.statusBar.showMessage('Ошибка!')
            self.statusBar.setStyleSheet('background-color: #ff0000;')
            self.messageTimer.start()
            return
        self.statusBar.showMessage(f'Событие успешно добавлено, его текст: {self.lineEdit.text()}')
        self.statusBar.setStyleSheet('background-color: #00ff00;')
        self.messageTimer.start()
        _id = db_search_event(self.current_user.get_id(), dt, text)
        self.events.append(Event(dt, text, _id, self.current_user.get_id()))
        self.refreshListWidget()

    def deleteEvents(self):
        res = db_delete_event((item.text() for item in self.listWidget.selectedItems()),
                              self.current_user.get_id())
        assert res, ''
        self.statusBar.showMessage('Событие успешно удалено')
        self.statusBar.setStyleSheet('background-color: #00ff00;')
        self.messageTimer.start()
        for event in self.events:
            if str(event) in (item.text() for item in self.listWidget.selectedItems()):
                self.events.remove(event)
        self.refreshListWidget()

    def hideBar(self):
        self.statusBar.showMessage('')
        self.statusBar.setStyleSheet('')
        self.messageTimer.stop()

    def eventNotification(self, td, text):
        hours = int(td.total_seconds() // 3600)
        hours_noun = morph.parse('час')[0].make_agree_with_number(hours).word
        minutes = int(td.total_seconds() // 60 % 60)
        minutes_noun = morph.parse('минута')[0].make_agree_with_number(minutes).word
        if hours:
            message_text = f'Через {hours} {hours_noun} {minutes} {minutes_noun} у вас состоится событие со ' \
                      f'следующим текстом: {text}.'
        else:
            message_text = f'Через {minutes} {minutes_noun} у вас состоится следующее событие : {text}.'
        message = QtWidgets.QMessageBox(self)
        message.setWindowTitle('Напоминание')
        message.setText(message_text)
        message.exec()

    def checkEvents(self):
        events = self.events
        current_time = datetime.datetime.now()
        for event in events:
            dt = event.get_datetime()
            timedelta = dt - current_time
            if timedelta.total_seconds() > 0 and timedelta < datetime.timedelta(hours=1) and not event.get_first():
                self.eventNotification(timedelta, event.get_text())
                event.set_first()
            if timedelta.total_seconds() > 0 and timedelta < datetime.timedelta(hours=24) and \
                    not event.get_first() and not event.get_second():
                self.eventNotification(timedelta, event.get_text())
                event.set_second()
        login = decrypt(self.current_user.get_login(), STEP)
        self.currentUserLabel.setText(login)
