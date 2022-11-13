from PyQt5 import QtCore, QtWidgets


class Ui_LoginDialog(object):
    def setupUi(self, LoginDialog):
        LoginDialog.setObjectName("LoginDialog")
        LoginDialog.resize(383, 126)
        self.verticalLayout = QtWidgets.QVBoxLayout(LoginDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(LoginDialog)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.loginLine = QtWidgets.QLineEdit(LoginDialog)
        self.loginLine.setObjectName("loginLine")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.loginLine)
        self.label_2 = QtWidgets.QLabel(LoginDialog)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.passwdLine = QtWidgets.QLineEdit(LoginDialog)
        self.passwdLine.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwdLine.setObjectName("passwdLine")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.passwdLine)
        self.verticalLayout.addLayout(self.formLayout)
        self.loginBtn = QtWidgets.QPushButton(LoginDialog)
        self.loginBtn.setObjectName("loginBtn")
        self.verticalLayout.addWidget(self.loginBtn)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.regBtn = QtWidgets.QPushButton(LoginDialog)
        self.regBtn.setObjectName("regBtn")
        self.horizontalLayout.addWidget(self.regBtn)
        self.recBtn = QtWidgets.QPushButton(LoginDialog)
        self.recBtn.setObjectName("recBtn")
        self.horizontalLayout.addWidget(self.recBtn)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(LoginDialog)
        QtCore.QMetaObject.connectSlotsByName(LoginDialog)

    def retranslateUi(self, LoginDialog):
        _translate = QtCore.QCoreApplication.translate
        LoginDialog.setWindowTitle(_translate("LoginDialog", "Вход"))
        self.label.setText(_translate("LoginDialog", "Логин"))
        self.label_2.setText(_translate("LoginDialog", "Пароль"))
        self.loginBtn.setText(_translate("LoginDialog", "Вход"))
        self.regBtn.setText(_translate("LoginDialog", "Регистрация"))
        self.recBtn.setText(_translate("LoginDialog", "Забыли пароль?"))
