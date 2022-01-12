# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import menu
import sqlite3 as sql


class settingsForm(object):
    def __init__(self, language):
        self.language = language
        self.cardSkin = 1
        self.decksNumber = 1

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(371, 361)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.backgroundLabel = QtWidgets.QLabel(Form)
        self.backgroundLabel.setGeometry(QtCore.QRect(0, 0, 371, 361))
        self.backgroundLabel.setText("")
        self.backgroundLabel.setObjectName("backgroundLabel")
        self.twoDecksButton = QtWidgets.QPushButton(Form)
        self.twoDecksButton.setGeometry(QtCore.QRect(160, 135, 51, 51))
        self.twoDecksButton.setStyleSheet("image: url(:/images/two.png);")
        self.twoDecksButton.setText("")
        self.twoDecksButton.setObjectName("twoDecksButton")
        self.threeDecksButton = QtWidgets.QPushButton(Form)
        self.threeDecksButton.setGeometry(QtCore.QRect(230, 135, 51, 51))
        self.threeDecksButton.setStyleSheet("image: url(:/images/three.png);")
        self.threeDecksButton.setText("")
        self.threeDecksButton.setObjectName("threeDecksButton")
        self.oneDeckButton = QtWidgets.QPushButton(Form)
        self.oneDeckButton.setGeometry(QtCore.QRect(90, 135, 51, 51))
        self.oneDeckButton.setStyleSheet("image: url(:/images/one.png);")
        self.oneDeckButton.setText("")
        self.oneDeckButton.setObjectName("oneDeckButton")
        self.classicSkinIcon = QtWidgets.QLabel(Form)
        self.classicSkinIcon.setGeometry(QtCore.QRect(117, 240, 61, 81))
        self.classicSkinIcon.setStyleSheet("image: url(:/images/cardBackOne.png);")
        self.classicSkinIcon.setText("")
        self.classicSkinIcon.setObjectName("classicSkinIcon")
        self.fancySkinIcon = QtWidgets.QLabel(Form)
        self.fancySkinIcon.setGeometry(QtCore.QRect(187, 240, 61, 81))
        self.fancySkinIcon.setStyleSheet("image: url(:/images/cardBackTwo.png);")
        self.fancySkinIcon.setText("")
        self.fancySkinIcon.setObjectName("fancySkinIcon")
        self.classicSkinButton = QtWidgets.QPushButton(Form)
        self.classicSkinButton.setGeometry(QtCore.QRect(120, 240, 55, 81))
        self.classicSkinButton.setStyleSheet("QPushButton { background-color: transparent; border: 0px };")
        self.classicSkinButton.setText("")
        self.classicSkinButton.setObjectName("classicSkinButton")
        self.fancySkinButton = QtWidgets.QPushButton(Form)
        self.fancySkinButton.setGeometry(QtCore.QRect(190, 240, 57, 81))
        self.fancySkinButton.setStyleSheet("QPushButton { background-color: transparent; border: 0px };")
        self.fancySkinButton.setText("")
        self.fancySkinButton.setObjectName("fancySkinButton")
        self.closeButton = QtWidgets.QPushButton(Form)
        self.closeButton.setGeometry(QtCore.QRect(346, 5, 14, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.closeButton.setFont(font)
        self.closeButton.setStyleSheet("QPushButton { background-color: transparent; border: 0px };")
        self.closeButton.setText("")
        self.closeButton.setObjectName("closeButton")

        if self.check_deck() == 1:
            self.oneDeck()
        elif self.check_deck() == 2:
            self.twoDecks()
        elif self.check_deck() == 3:
            self.threeDecks()
        if self.check_skin() == 1:
            self.classicSkin()
        if self.check_skin() == 2:
            self.fancySkin()

        # Obsługa przycisków
        self.oneDeckButton.clicked.connect(self.oneDeck)
        self.twoDecksButton.clicked.connect(self.twoDecks)
        self.threeDecksButton.clicked.connect(self.threeDecks)
        self.classicSkinButton.clicked.connect(self.classicSkin)
        self.fancySkinButton.clicked.connect(self.fancySkin)
        self.closeButton.clicked.connect(self.returnToMenu)
        self.closeButton.clicked.connect(Form.close)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # Obsługa języków
        if self.language == 1:
            self.backgroundLabel.setStyleSheet("image: url(:/images/settingsEng.png);")
        if self.language == 2:
            self.backgroundLabel.setStyleSheet("image: url(:/images/settingsPL.png);")

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Settings"))

    def oneDeck(self):
        self.decksNumber = 1
        self.set_decks(1)
        self.oneDeckButton.setStyleSheet("image: url(:/images/one.png);")
        self.twoDecksButton.setStyleSheet("image: url(:/images/twoInactive.png);")
        self.threeDecksButton.setStyleSheet("image: url(:/images/threeInactive.png);")

    def twoDecks(self):
        self.decksNumber = 2
        self.set_decks(2)
        self.oneDeckButton.setStyleSheet("image: url(:/images/oneInactive.png);")
        self.twoDecksButton.setStyleSheet("image: url(:/images/two.png);")
        self.threeDecksButton.setStyleSheet("image: url(:/images/threeInactive.png);")

    def threeDecks(self):
        self.decksNumber = 3
        self.set_decks(3)
        self.oneDeckButton.setStyleSheet("image: url(:/images/oneInactive.png);")
        self.twoDecksButton.setStyleSheet("image: url(:/images/twoInactive.png);")
        self.threeDecksButton.setStyleSheet("image: url(:/images/three.png);")

    def classicSkin(self):
        self.cardSkin = 1
        self.set_skin(1)
        self.classicSkinIcon.setStyleSheet("image: url(:/images/cardBackOne.png);")
        self.fancySkinIcon.setStyleSheet("image: url(:/images/cardBackTwoInactive.png);")

    def fancySkin(self):
        self.cardSkin = 2
        self.set_skin(2)
        self.classicSkinIcon.setStyleSheet("image: url(:/images/cardBackOneInactive.png);")
        self.fancySkinIcon.setStyleSheet("image: url(:/images/cardBackTwo.png);")

    def set_decks(self, decks):
        try:
            db = sql.connect('database.db')  # łączymy się do bazy
            c = db.cursor()  # dodajemy kursor

            # c.execute("""CREATE TABLE settings (
            #                 number_of_decks integer,
            #                 path text
            #                 )""")

            # # NAJPIERW RESETUJEMY POPRZEDNI WYBÓR
            # query = "DELETE FROM settings"
            # c.execute(query)
            # db.commit()

            # c.execute("INSERT INTO settings (number_of_decks, path) VALUES (?,?)", (number_of_decks, path))
            c.execute("UPDATE settings SET decks = {}".format(decks))
            db.commit()


        except sql.Error as e:
            print("error")

    def set_skin(self, skin):
        try:
            db = sql.connect('database.db')  # łączymy się do bazy
            c = db.cursor()  # dodajemy kursor

            # c.execute("""CREATE TABLE settings (
            #                 number_of_decks integer,
            #                 path text
            #                 )""")

            # NAJPIERW RESETUJEMY POPRZEDNI WYBÓR
            # query = "DELETE FROM settings"
            # c.execute(query)
            # db.commit()

            # c.execute("INSERT INTO settings (number_of_decks, path) VALUES (?,?)", (number_of_decks, path))
            c.execute("UPDATE settings SET skin = {}".format(skin))
            db.commit()


        except sql.Error as e:
            print("error")

    def check_deck(self):
        try:
            db = sql.connect('database.db')  # łączymy się do bazy
            c = db.cursor()  # dodajemy kursor

            query = "SELECT decks from settings"
            c.execute(query)
            db.commit()
            result = c.fetchone()
            print(result)
            return result[0]


        except sql.Error as e:
            print("error")

    def check_skin(self):
        try:
            db = sql.connect('database.db')  # łączymy się do bazy
            c = db.cursor()  # dodajemy kursor

            query = "SELECT skin from settings"
            c.execute(query)
            db.commit()
            result = c.fetchone()
            print(result)
            return result[0]


        except sql.Error as e:
            print("error")

    def returnToMenu(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = menu.menuForm(self.language)
        self.ui.setupUi(self.window)
        self.window.show()
