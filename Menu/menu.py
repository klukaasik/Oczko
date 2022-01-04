# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys, register, res

import account
import playOptions
import rules, login
import settings


class menuForm(object):
    def __init__(self, language):
        # Ustawienia języka, 1 - angielski, 2 - polski
        self.language = language

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(901, 616)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(0, 0, 901, 601))
        self.widget.setObjectName("widget")
        self.backgroundPicture = QtWidgets.QLabel(self.widget)
        self.backgroundPicture.setGeometry(QtCore.QRect(-10, 0, 441, 611))
        self.backgroundPicture.setStyleSheet("border-image: url(:/images/background.jpg);\n"
                                             "")
        self.backgroundPicture.setText("")
        self.backgroundPicture.setObjectName("backgroundPicture")
        self.backgroundSolid = QtWidgets.QLabel(self.widget)
        self.backgroundSolid.setGeometry(QtCore.QRect(410, 0, 511, 611))
        self.backgroundSolid.setStyleSheet("background-color: rgb(24, 47, 38);")
        self.backgroundSolid.setText("")
        self.backgroundSolid.setObjectName("backgroundSolid")
        self.rankLabel = QtWidgets.QLabel(self.widget)
        self.rankLabel.setGeometry(QtCore.QRect(510, 420, 121, 111))
        self.rankLabel.setStyleSheet("background-color:rgba(0, 0, 0, 100);\n"
                                     "border-radius:50px;\n"
                                     "")
        self.rankLabel.setText("")
        self.rankLabel.setObjectName("rankLabel")
        self.rankIcon = QtWidgets.QLabel(self.widget)
        self.rankIcon.setGeometry(QtCore.QRect(520, 430, 101, 101))
        self.rankIcon.setStyleSheet("border-image: url(:/images/rank.png);")
        self.rankIcon.setText("")
        self.rankIcon.setObjectName("rankIcon")
        self.rankLabel = QtWidgets.QLabel(self.widget)
        self.rankLabel.setGeometry(QtCore.QRect(460, 420, 101, 101))
        self.rankLabel.setStyleSheet("background-color:rgba(0, 0, 0, 100);\n"
                                     "border-radius:50px;\n"
                                     "")
        self.rankLabel.setText("")
        self.rankLabel.setObjectName("rankLabel")
        self.rankIcon = QtWidgets.QLabel(self.widget)
        self.rankIcon.setGeometry(QtCore.QRect(466, 420, 91, 91))
        self.rankIcon.setStyleSheet("border-image: url(:/images/rank.png);")
        self.rankIcon.setText("")
        self.rankIcon.setObjectName("rankIcon")
        self.registerIcon = QtWidgets.QLabel(self.widget)
        self.registerIcon.setGeometry(QtCore.QRect(761, 433, 71, 71))
        self.registerIcon.setStyleSheet("border-image: url(:/images/register.png);")
        self.registerIcon.setText("")
        self.registerIcon.setObjectName("registerIcon")
        self.registerLabel = QtWidgets.QLabel(self.widget)
        self.registerLabel.setGeometry(QtCore.QRect(745, 420, 101, 101))
        self.registerLabel.setStyleSheet("background-color:rgba(0, 0, 0, 100);\n"
                                         "border-radius:50px;\n"
                                         "")
        self.registerLabel.setText("")
        self.registerLabel.setObjectName("registerLabel")
        self.playIcon = QtWidgets.QLabel(self.widget)
        self.playIcon.setGeometry(QtCore.QRect(530, 150, 251, 241))
        self.playIcon.setStyleSheet("border-image: url(:/images/play.png);")
        self.playIcon.setText("")
        self.playIcon.setObjectName("playIcon")
        self.logo = QtWidgets.QLabel(self.widget)
        self.logo.setGeometry(QtCore.QRect(470, 60, 391, 81))
        self.logo.setStyleSheet("border-image: url(:/images/logo.png);")
        self.logo.setText("")
        self.logo.setObjectName("logo")
        self.rankButton = QtWidgets.QPushButton(self.widget)
        self.rankButton.setGeometry(QtCore.QRect(460, 420, 101, 101))
        self.rankButton.setStyleSheet("QPushButton { background-color: transparent; border: 0px };")
        self.rankButton.setText("")
        self.rankButton.setObjectName("rankButton")
        self.registerButton = QtWidgets.QPushButton(self.widget)
        self.registerButton.setGeometry(QtCore.QRect(752, 420, 91, 101))
        self.registerButton.setStyleSheet("QPushButton { background-color: transparent; border: 0px };")
        self.registerButton.setText("")
        self.registerButton.setObjectName("registerButton")

        self.playButton = QtWidgets.QPushButton(self.widget)
        self.playButton.setGeometry(QtCore.QRect(540, 160, 231, 221))
        self.playButton.setStyleSheet("QPushButton { background-color: transparent; border: 0px };")
        self.playButton.setText("")
        self.playButton.setObjectName("playButton")

        self.englishIcon = QtWidgets.QLabel(self.widget)
        self.englishIcon.setGeometry(QtCore.QRect(36, 560, 61, 31))
        self.englishIcon.setStyleSheet("image: url(:/images/english.png);")
        self.englishIcon.setText("")
        self.englishIcon.setObjectName("englishIcon")
        self.polishIcon = QtWidgets.QLabel(self.widget)
        self.polishIcon.setGeometry(QtCore.QRect(1, 560, 51, 31))
        self.polishIcon.setStyleSheet("image: url(:/images/polish.png);")
        self.polishIcon.setText("")
        self.polishIcon.setObjectName("polishIcon")
        self.polishButton = QtWidgets.QPushButton(self.widget)
        self.polishButton.setGeometry(QtCore.QRect(10, 566, 31, 21))
        self.polishButton.setStyleSheet("QPushButton { background-color: transparent; border: 0px };")
        self.polishButton.setText("")
        self.polishButton.setObjectName("polishButton")
        self.englishButton = QtWidgets.QPushButton(self.widget)
        self.englishButton.setGeometry(QtCore.QRect(51, 567, 31, 21))
        self.englishButton.setStyleSheet("QPushButton { background-color: transparent; border: 0px };")
        self.englishButton.setText("")
        self.englishButton.setObjectName("englishButton")
        self.closeLabel = QtWidgets.QLabel(self.widget)
        self.closeLabel.setGeometry(QtCore.QRect(880, 0, 21, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(15)
        font.setBold(True)
        self.closeLabel.setFont(font)
        self.closeLabel.setStyleSheet("color: rgb(255, 170, 0);")
        self.closeLabel.setObjectName("closeLabel")
        self.closeButton = QtWidgets.QPushButton(self.widget)
        self.closeButton.setGeometry(QtCore.QRect(880, 0, 21, 31))
        self.closeButton.setStyleSheet("QPushButton { background-color: transparent; border: 0px };")
        self.closeButton.setText("")
        self.closeButton.setObjectName("closeButton")

        self.rulesIcon = QtWidgets.QLabel(self.widget)
        self.rulesIcon.setGeometry(QtCore.QRect(850, 550, 41, 41))
        self.rulesIcon.setStyleSheet("border-image: url(:/images/rules.png);")
        self.rulesIcon.setText("")
        self.rulesIcon.setObjectName("rulesIcon")
        self.rulesButton = QtWidgets.QPushButton(self.widget)
        self.rulesButton.setGeometry(QtCore.QRect(850, 550, 41, 41))
        self.rulesButton.setStyleSheet("QPushButton { background-color: transparent; border: 0px };")
        self.rulesButton.setText("")
        self.rulesButton.setObjectName("rulesButton")

        self.settingsIcon = QtWidgets.QLabel(self.widget)
        self.settingsIcon.setGeometry(QtCore.QRect(420, 550, 41, 41))
        self.settingsIcon.setStyleSheet("border-image: url(:/images/settings.png);")
        self.settingsIcon.setText("")
        self.settingsIcon.setObjectName("settingsIcon")
        self.historyIcon = QtWidgets.QLabel(self.widget)
        self.historyIcon.setGeometry(QtCore.QRect(800, 550, 41, 41))
        self.historyIcon.setStyleSheet("border-image: url(:/images/history.png);")
        self.historyIcon.setText("")
        self.historyIcon.setObjectName("historyIcon")
        self.historyButton = QtWidgets.QPushButton(self.widget)
        self.historyButton.setGeometry(QtCore.QRect(800, 550, 41, 41))
        self.historyButton.setStyleSheet("QPushButton { background-color: transparent; border: 0px };")
        self.historyButton.setText("")
        self.historyButton.setObjectName("historyButton")
        self.settingsButton = QtWidgets.QPushButton(self.widget)
        self.settingsButton.setGeometry(QtCore.QRect(420, 550, 41, 41))
        self.settingsButton.setStyleSheet("QPushButton { background-color: transparent; border: 0px };")
        self.settingsButton.setText("")
        self.settingsButton.setObjectName("settingsButton")
        self.closeButton.setObjectName("closeButton")
        self.accountLabel = QtWidgets.QLabel(self.widget)
        self.accountLabel.setGeometry(QtCore.QRect(602, 420, 101, 101))
        self.accountLabel.setStyleSheet("background-color:rgba(0, 0, 0, 100);\n"
                                        "border-radius:50px;\n"
                                        "")
        self.accountLabel.setText("")
        self.accountLabel.setObjectName("accountLabel")
        self.accountButton = QtWidgets.QPushButton(self.widget)
        self.accountButton.setGeometry(QtCore.QRect(600, 420, 101, 101))
        self.accountButton.setStyleSheet("QPushButton { background-color: transparent; border: 0px };")
        self.accountButton.setText("")
        self.accountButton.setObjectName("accountButton")
        self.accountIcon = QtWidgets.QLabel(self.widget)
        self.accountIcon.setGeometry(QtCore.QRect(628, 442, 51, 51))
        self.accountIcon.setStyleSheet("border-image: url(:/images/userIcon.png);")
        self.accountIcon.setText("")
        self.accountIcon.setObjectName("accountIcon")

        if self.language == 1:
            self.playIcon.setStyleSheet("border-image: url(:/images/play.png);")
            self.logo.setStyleSheet("border-image: url(:/images/logo.png);")
            self.logo.setGeometry(QtCore.QRect(470, 60, 391, 81))
        elif self.language == 2:
            self.logo.setStyleSheet("border-image: url(:/images/logoPL.png);")
            self.logo.setGeometry(QtCore.QRect(530, 60, 281, 81))
            self.playIcon.setStyleSheet("border-image: url(:/images/playPL.png);")

        self.backgroundPicture.raise_()
        self.backgroundSolid.raise_()
        self.rankLabel.raise_()
        self.rankIcon.raise_()
        self.registerLabel.raise_()
        self.registerIcon.raise_()
        self.playIcon.raise_()
        self.logo.raise_()
        self.rankButton.raise_()
        self.registerButton.raise_()
        self.playButton.raise_()
        self.englishIcon.raise_()
        self.polishIcon.raise_()
        self.polishButton.raise_()
        self.englishButton.raise_()
        self.closeLabel.raise_()
        self.closeButton.raise_()
        self.rulesIcon.raise_()
        self.rulesButton.raise_()
        self.settingsIcon.raise_()
        self.historyIcon.raise_()
        self.historyButton.raise_()
        self.settingsButton.raise_()
        self.accountLabel.raise_()
        self.accountIcon.raise_()
        self.accountButton.raise_()


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # Obsługa przycisków
        self.playButton.clicked.connect(self.play)
        self.registerButton.clicked.connect(self.register)
        self.registerButton.clicked.connect(Form.close)
        self.playButton.clicked.connect(Form.close)
        self.closeButton.clicked.connect(Form.close)
        self.rulesButton.clicked.connect(self.rules)
        self.rulesButton.clicked.connect(Form.close)
        self.settingsButton.clicked.connect(self.settings)
        self.settingsButton.clicked.connect(Form.close)
        self.englishButton.clicked.connect(self.english)
        self.polishButton.clicked.connect(self.polish)
        self.accountButton.clicked.connect(Form.close)
        self.accountButton.clicked.connect(self.show_login)
        # self.accountButton.clicked.connect(self.account)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.closeLabel.setText(_translate("Form", "X"))

    def english(self):
        self.language = 1
        self.playIcon.setStyleSheet("border-image: url(:/images/play.png);")
        self.logo.setStyleSheet("border-image: url(:/images/logo.png);")
        self.logo.setGeometry(QtCore.QRect(470, 60, 391, 81))

    def polish(self):
        self.language = 2
        self.logo.setStyleSheet("border-image: url(:/images/logoPL.png);")
        self.logo.setGeometry(QtCore.QRect(530, 60, 281, 81))
        self.playIcon.setStyleSheet("border-image: url(:/images/playPL.png);")

    def rules(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = rules.rulesForm(self.language)
        self.ui.setupUi(self.window)
        self.window.show()

    def register(self):
        self.registerWindow = QtWidgets.QMainWindow()
        self.ui = register.registerForm(self.language, [], 0, 0, 3)
        self.ui.setupUi(self.registerWindow)
        self.registerWindow.show()

    def settings(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = settings.settingsForm(self.language)
        self.ui.setupUi(self.window)
        self.window.show()

    def rank(self):
        print('ranking')

    def play(self):
        self.playWindow = QtWidgets.QMainWindow()
        self.ui = playOptions.playOptionsForm(self.language)
        self.ui.setupUi(self.playWindow)
        self.playWindow.show()

    def show_login(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = login.loginForm(self.language, [], 0, 0, 3)
        self.ui.setupUi(self.window)
        self.window.show()