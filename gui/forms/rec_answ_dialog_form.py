from PyQt5 import QtCore, QtWidgets


class Ui_RecAnswDialog(object):
    def setupUi(self, RecAnswDialog):
        RecAnswDialog.setObjectName("RecAnswDialog")
        RecAnswDialog.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(RecAnswDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(RecAnswDialog)
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(RecAnswDialog)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.answLine = QtWidgets.QLineEdit(RecAnswDialog)
        self.answLine.setObjectName("answLine")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.answLine)
        self.verticalLayout.addLayout(self.formLayout)
        self.answBtn = QtWidgets.QPushButton(RecAnswDialog)
        self.answBtn.setObjectName("answBtn")
        self.verticalLayout.addWidget(self.answBtn)

        self.retranslateUi(RecAnswDialog)
        QtCore.QMetaObject.connectSlotsByName(RecAnswDialog)

    def retranslateUi(self, RecAnswDialog):
        _translate = QtCore.QCoreApplication.translate
        RecAnswDialog.setWindowTitle(_translate("RecAnswDialog", "Dialog"))
        self.label_2.setText(_translate("RecAnswDialog", "Ответ:"))
        self.answBtn.setText(_translate("RecAnswDialog", "Ответить"))
