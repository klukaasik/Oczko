# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'betting.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3 as sql
import playUsers, board

class bettingForm(object):

    def __init__(self, language, playersNumber, computersNumber, betting, numberOfPlayer, gameLevel, computerOneLevel,
                 computerTwoLevel, computerThreeLevel, computerFourLevel):
        self.language = language
        self.playersNumber = playersNumber
        self.computersNumber = computersNumber
        self.betting = betting
        self.numberOfPlayer = numberOfPlayer
        self.gameLevel = gameLevel
        self.computerOneLevel = computerOneLevel
        self.computerTwoLevel = computerTwoLevel
        self.computerThreeLevel = computerThreeLevel
        self.computerFourLevel = computerFourLevel
        self.input = ""


    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(759, 571)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.backgroundDark = QtWidgets.QLabel(Form)
        self.backgroundDark.setGeometry(QtCore.QRect(90, 70, 581, 381))
        self.backgroundDark.setText("")
        self.backgroundDark.setAlignment(QtCore.Qt.AlignCenter)
        self.backgroundDark.setObjectName("backgroundDark")
        self.playButton = QtWidgets.QPushButton(Form)
        self.playButton.setGeometry(QtCore.QRect(340, 395, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.playButton.setFont(font)
        self.playButton.setStyleSheet("QPushButton#playButton{\n"
"    background-color: rgb(255, 170, 0);\n"
"    color: rgb(255, 104, 3);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton#playButton:pressed{\n"
"    padding-left:3px;\n"
"    padding-top:3px;\n"
"    background-color: rgb(255, 206, 12);\n"
"    background-position:calc(100%-10px)center;\n"
"}\n"
"\n"
"QPushButton#playButton:hover{\n"
"    background-color: rgb(255, 206, 12);\n"
"}\n"
"")
        self.playButton.setObjectName("playButton")
        self.betInput = QtWidgets.QLineEdit(Form)
        self.betInput.setGeometry(QtCore.QRect(310, 351, 141, 31))
        font = QtGui.QFont()
        font.setBold(True)
        self.betInput.setFont(font)
        self.betInput.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
"border:1px solid rgba(0, 0, 0, 0);\n"
"border-color: rgb(255, 170, 0);\n"
"padding-bottom: 7px;\n"
"color: rgb(255, 170, 0);")
        self.betInput.setAlignment(QtCore.Qt.AlignCenter)
        self.betInput.setObjectName("betInput")
        self.warningLabel = QtWidgets.QLabel(Form)
        self.warningLabel.setGeometry(QtCore.QRect(90, 320, 581, 20))
        self.warningLabel.setStyleSheet("color: rgb(255, 52, 1);")
        self.warningLabel.setText("")
        self.warningLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.warningLabel.setObjectName("warningLabel")
        self.playerOneNickname = QtWidgets.QLabel(Form)
        self.playerOneNickname.setGeometry(QtCore.QRect(190, 140, 191, 31))
        font = QtGui.QFont()
        font.setBold(True)
        self.playerOneNickname.setFont(font)
        self.playerOneNickname.setStyleSheet("color: rgb(255, 170, 0);")
        self.playerOneNickname.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.playerOneNickname.setObjectName("playerOneNickname")
        self.playerTwoNickname = QtWidgets.QLabel(Form)
        self.playerTwoNickname.setGeometry(QtCore.QRect(190, 170, 191, 31))
        font = QtGui.QFont()
        font.setBold(True)
        self.playerTwoNickname.setFont(font)
        self.playerTwoNickname.setStyleSheet("color: rgb(255, 170, 0);")
        self.playerTwoNickname.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.playerTwoNickname.setObjectName("playerTwoNickname")
        self.playerThreeNickname = QtWidgets.QLabel(Form)
        self.playerThreeNickname.setGeometry(QtCore.QRect(190, 200, 191, 31))
        font = QtGui.QFont()
        font.setBold(True)
        self.playerThreeNickname.setFont(font)
        self.playerThreeNickname.setStyleSheet("color: rgb(255, 170, 0);")
        self.playerThreeNickname.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.playerThreeNickname.setObjectName("playerThreeNickname")
        self.playerFourNickname = QtWidgets.QLabel(Form)
        self.playerFourNickname.setGeometry(QtCore.QRect(190, 230, 191, 31))
        font = QtGui.QFont()
        font.setBold(True)
        self.playerFourNickname.setFont(font)
        self.playerFourNickname.setStyleSheet("color: rgb(255, 170, 0);")
        self.playerFourNickname.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.playerFourNickname.setObjectName("playerFourNickname")
        self.playerOneWallet = QtWidgets.QLabel(Form)
        self.playerOneWallet.setGeometry(QtCore.QRect(390, 140, 191, 31))
        self.playerOneWallet.setStyleSheet("color: rgb(203, 82, 12);")
        self.playerOneWallet.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.playerOneWallet.setObjectName("playerOneWallet")
        self.playerTwoWallet = QtWidgets.QLabel(Form)
        self.playerTwoWallet.setGeometry(QtCore.QRect(390, 170, 191, 31))
        self.playerTwoWallet.setStyleSheet("color: rgb(203, 82, 12);")
        self.playerTwoWallet.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.playerTwoWallet.setObjectName("playerTwoWallet")
        self.playerThreeWallet = QtWidgets.QLabel(Form)
        self.playerThreeWallet.setGeometry(QtCore.QRect(390, 200, 191, 31))
        self.playerThreeWallet.setStyleSheet("color: rgb(203, 82, 12);")
        self.playerThreeWallet.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.playerThreeWallet.setObjectName("playerThreeWallet")
        self.playerFourWallet = QtWidgets.QLabel(Form)
        self.playerFourWallet.setGeometry(QtCore.QRect(390, 230, 191, 31))
        self.playerFourWallet.setStyleSheet("color: rgb(203, 82, 12);")
        self.playerFourWallet.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.playerFourWallet.setObjectName("playerFourWallet")

        # Obsługa języków
        if self.language == 1:
            self.backgroundDark.setStyleSheet("image: url(:/images/bettingBackground.png);")
        if self.language == 2:
            self.backgroundDark.setStyleSheet("image: url(:/images/bettingBackgroundPL.png);")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


        if (1 in self.numberOfPlayer) == True:
            self.playerOneNickname.setText(self.set_username(1))
            self.playerOneWallet.setText(str(self.set_wallet(1)))
        if (2 in self.numberOfPlayer) == True:
            self.playerTwoNickname.setText(self.set_username(2))
            self.playerTwoWallet.setText(str(self.set_wallet(2)))
        if (3 in self.numberOfPlayer) == True:
            self.playerThreeNickname.setText(self.set_username(3))
            self.playerThreeWallet.setText(str(self.set_wallet(3)))
        if (4 in self.numberOfPlayer) == True:
            self.playerFourNickname.setText(self.set_username(4))
            self.playerFourWallet.setText(str(self.set_wallet(4)))

        self.playButton.clicked.connect(self.play)


    def set_username(self,user_id):
        try:
            db = sql.connect('database.db')  # łączymy się do bazy
            c = db.cursor()  # dodajemy kursor

            query = "SELECT id, username, coins from logged_users where id = {}".format(user_id)
            c.execute(query)
            db.commit()
            result = c.fetchone()
            print(result[1])
            return result[1]

        except sql.Error as e:
            print("huj")

    def set_wallet(self,user_id):
        try:
            db = sql.connect('database.db')  # łączymy się do bazy
            c = db.cursor()  # dodajemy kursor

            query = "SELECT id, username, coins from logged_users where id = {}".format(user_id)
            c.execute(query)
            db.commit()
            result = c.fetchone()
            print(result[2])
            return result[2]

        except sql.Error as e:
            print("error")

    def play(self):
        try:
            self.input = int(self.betInput.text())

        # Poniższy "if" jest niepotrzebny, ponieważ gracz nie może grać sam na pieniądze. W razie późniejszych zmian tylko zakomentowany

        # if len(self.numberOfPlayer) == 1:
        #     if self.input > self.set_wallet(1):
        #         self.warningLabel.setText("kogo")
        #     else:
        #         self.openBoard()

            if len(self.numberOfPlayer) == 2:
                if self.input > self.set_wallet(1) or self.input > self.set_wallet(2) or self.input < 1:
                    self.warningLabel.setText("Invalid value")
                else:
                    self.openBoard()
            elif len(self.numberOfPlayer) == 3:
                if self.input > self.set_wallet(1) or self.input > self.set_wallet(2) \
                        or self.input > self.set_wallet(3) or self.input < 1:
                    self.warningLabel.setText("Invalid value")
                else:
                    self.openBoard()
            elif len(self.numberOfPlayer) == 4:
                if self.input > self.set_wallet(1) or self.input > self.set_wallet(2)\
                        or self.input > self.set_wallet(3) or self.input > self.set_wallet(4) or self.input < 1:
                    self.warningLabel.setText("Invalid value")
                else:
                    self.openBoard()
        except ValueError as e:
            self.warningLabel.setText("That's not a number!")



    def openBoard(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = board.boardForm(self.language, self.playersNumber, self.computersNumber, self.betting,
                                  self.numberOfPlayer, self.gameLevel, self.computerOneLevel, self.computerTwoLevel, self.computerThreeLevel, self.computerFourLevel, self.input)
        self.ui.setupUi(self.window)
        self.window.show()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        if self.language == 1:
            self.playButton.setText(_translate("Form", "PLAY!"))
        if self.language == 2:
            self.playButton.setText(_translate("Form", "GRAJ!"))
        Form.setWindowTitle(_translate("Form", "Betting"))


