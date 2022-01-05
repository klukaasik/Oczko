# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'account.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

import menu


class accountForm(object):
    def __init__(self, language):
        self.language = language

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(918, 601)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.backgroundLabel = QtWidgets.QLabel(Form)
        self.backgroundLabel.setGeometry(QtCore.QRect(0, 0, 901, 601))
        self.backgroundLabel.setText("")
        self.backgroundLabel.setObjectName("backgroundLabel")
        self.closeButton = QtWidgets.QPushButton(Form)
        self.closeButton.setGeometry(QtCore.QRect(883, 3, 13, 17))
        self.closeButton.setStyleSheet("QPushButton { background-color: transparent; border: 0px };")
        self.closeButton.setText("")
        self.closeButton.setObjectName("closeButton")
        self.winsLabel = QtWidgets.QLabel(Form)
        self.winsLabel.setGeometry(QtCore.QRect(180, 100, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.winsLabel.setFont(font)
        self.winsLabel.setStyleSheet("color: rgb(255, 85, 0);")
        self.winsLabel.setObjectName("winsLabel")
        self.gamesLabel = QtWidgets.QLabel(Form)
        self.gamesLabel.setGeometry(QtCore.QRect(192, 230, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.gamesLabel.setFont(font)
        self.gamesLabel.setStyleSheet("color: rgb(255, 85, 0);")
        self.gamesLabel.setObjectName("gamesLabel")
        self.cardsLabel = QtWidgets.QLabel(Form)
        self.cardsLabel.setGeometry(QtCore.QRect(190, 353, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.cardsLabel.setFont(font)
        self.cardsLabel.setStyleSheet("color: rgb(255, 85, 0);")
        self.cardsLabel.setObjectName("cardsLabel")
        self.minutesLabel = QtWidgets.QLabel(Form)
        self.minutesLabel.setGeometry(QtCore.QRect(190, 480, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.minutesLabel.setFont(font)
        self.minutesLabel.setStyleSheet("color: rgb(255, 85, 0);")
        self.minutesLabel.setObjectName("minutesLabel")
        self.walletLabel = QtWidgets.QLabel(Form)
        self.walletLabel.setGeometry(QtCore.QRect(620, 415, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.walletLabel.setFont(font)
        self.walletLabel.setStyleSheet("color: rgb(255, 181, 7);")
        self.walletLabel.setObjectName("walletLabel")
        self.usernameLabel = QtWidgets.QLabel(Form)
        self.usernameLabel.setGeometry(QtCore.QRect(410, 320, 481, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.usernameLabel.setFont(font)
        self.usernameLabel.setStyleSheet("color: rgb(120, 170, 44);")
        self.usernameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.usernameLabel.setObjectName("usernameLabel")
        self.passwordButton = QtWidgets.QPushButton(Form)
        self.passwordButton.setGeometry(QtCore.QRect(590, 502, 131, 68))
        self.passwordButton.setStyleSheet("QPushButton { background-color: transparent; border: 0px };")
        self.passwordButton.setText("")
        self.passwordButton.setObjectName("passwordButton")
        self.closeButton.clicked.connect(self.returnToMenu)
        self.closeButton.clicked.connect(Form.close)

        if self.language == 1:
            self.backgroundLabel.setStyleSheet("image: url(:/images/accountBackground.png);")
        if self.language == 2:
            self.backgroundLabel.setStyleSheet("image: url(:/images/accountBackgroundPL.png);")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.winsLabel.setText(_translate("Form", "69%"))
        self.gamesLabel.setText(_translate("Form", "2"))
        self.cardsLabel.setText(_translate("Form", "12"))
        self.minutesLabel.setText(_translate("Form", "21"))
        self.walletLabel.setText(_translate("Form", "1241"))
        self.usernameLabel.setText(_translate("Form", "niknejm"))

    def returnToMenu(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = menu.menuForm(self.language)
        self.ui.setupUi(self.window)
        self.window.show()
