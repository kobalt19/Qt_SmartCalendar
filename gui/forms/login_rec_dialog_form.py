from PyQt5 import QtCore, QtWidgets


class Ui_LoginRecDialog(object):
    def setupUi(self, LoginRecDialog):
        LoginRecDialog.setObjectName("LoginRecDialog")
        LoginRecDialog.resize(390, 110)
        self.verticalLayout = QtWidgets.QVBoxLayout(LoginRecDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(LoginRecDialog)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.loginLine = QtWidgets.QLineEdit(LoginRecDialog)
        self.loginLine.setObjectName("loginLine")
        self.horizontalLayout.addWidget(self.loginLine)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.okBtn = QtWidgets.QPushButton(LoginRecDialog)
        self.okBtn.setObjectName("okBtn")
        self.verticalLayout.addWidget(self.okBtn)

        self.retranslateUi(LoginRecDialog)
        QtCore.QMetaObject.connectSlotsByName(LoginRecDialog)

    def retranslateUi(self, LoginRecDialog):
        _translate = QtCore.QCoreApplication.translate
        LoginRecDialog.setWindowTitle(_translate("LoginRecDialog", "Введите логин"))
        self.label.setText(_translate("LoginRecDialog", "Введите ваш логин:"))
        self.okBtn.setText(_translate("LoginRecDialog", "OK"))
