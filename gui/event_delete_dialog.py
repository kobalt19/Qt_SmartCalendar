from PyQt5 import QtCore, QtGui, QtWidgets
from .forms.event_delete_dialog_form import Ui_Dialog


class DeleteDialog(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, events):
        super(DeleteDialog, self).__init__()
        self.setupUi(self)
        self.to_delete = []
        for event in events:
            self.listWidget.addItem(event)
        self.pushButton.clicked.connect(self.deleteEvent)

    def deleteEvent(self):
        if not self.listWidget.selectedItems():
            self.showError()
        else:
            self.to_delete = (item.text() for item in self.listWidget.selectedItems())
            self.reject()

    def getEvents(self):
        return self.to_delete

    def showError(self):
        mb = QtWidgets.QMessageBox(self)
        mb.setWindowTitle('Ошибка!')
        mb.setText('Вы не выбрали событие, которое хотите удалить!')
        mb.exec()


