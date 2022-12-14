from PyQt5 import QtCore, QtWidgets


class Ui_RecDialog(object):
    def setupUi(self, RecDialog):
        RecDialog.setObjectName("RecDialog")
        RecDialog.resize(367, 95)
        self.verticalLayout = QtWidgets.QVBoxLayout(RecDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(RecDialog)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.passwdLine = QtWidgets.QLineEdit(RecDialog)
        self.passwdLine.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwdLine.setObjectName("passwdLine")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.passwdLine)
        self.label_2 = QtWidgets.QLabel(RecDialog)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.passwdRepLine = QtWidgets.QLineEdit(RecDialog)
        self.passwdRepLine.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwdRepLine.setObjectName("passwdRepLine")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.passwdRepLine)
        self.verticalLayout.addLayout(self.formLayout)
        self.doneBtn = QtWidgets.QPushButton(RecDialog)
        self.doneBtn.setObjectName("doneBtn")
        self.verticalLayout.addWidget(self.doneBtn)

        self.retranslateUi(RecDialog)
        QtCore.QMetaObject.connectSlotsByName(RecDialog)

    def retranslateUi(self, RecDialog):
        _translate = QtCore.QCoreApplication.translate
        RecDialog.setWindowTitle(_translate("RecDialog", "Смена пароля"))
        self.label.setText(_translate("RecDialog", "Пароль"))
        self.label_2.setText(_translate("RecDialog", "Повторите пароль"))
        self.doneBtn.setText(_translate("RecDialog", "Готово"))
