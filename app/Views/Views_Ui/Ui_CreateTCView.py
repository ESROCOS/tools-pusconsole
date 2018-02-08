# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CreateTCView.ui'
#
# Created: Thu Feb  8 12:49:46 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_CreateTCView(object):
    def setupUi(self, CreateTCView):
        CreateTCView.setObjectName("CreateTCView")
        CreateTCView.resize(422, 739)
        self.commandTextEdit = QtGui.QPlainTextEdit(CreateTCView)
        self.commandTextEdit.setGeometry(QtCore.QRect(10, 220, 401, 511))
        self.commandTextEdit.setObjectName("commandTextEdit")
        self.createTCLabel = QtGui.QLabel(CreateTCView)
        self.createTCLabel.setGeometry(QtCore.QRect(10, 190, 151, 17))
        self.createTCLabel.setObjectName("createTCLabel")
        self.historyList = QtGui.QListWidget(CreateTCView)
        self.historyList.setGeometry(QtCore.QRect(10, 30, 401, 101))
        self.historyList.setObjectName("historyList")
        QtGui.QListWidgetItem(self.historyList)
        QtGui.QListWidgetItem(self.historyList)
        QtGui.QListWidgetItem(self.historyList)
        QtGui.QListWidgetItem(self.historyList)
        self.label = QtGui.QLabel(CreateTCView)
        self.label.setGeometry(QtCore.QRect(10, 10, 111, 17))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(CreateTCView)
        self.label_2.setGeometry(QtCore.QRect(10, 140, 121, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtGui.QLabel(CreateTCView)
        self.label_3.setGeometry(QtCore.QRect(200, 140, 121, 17))
        self.label_3.setObjectName("label_3")
        self.serviceComboBox = QtGui.QComboBox(CreateTCView)
        self.serviceComboBox.setGeometry(QtCore.QRect(100, 140, 85, 27))
        self.serviceComboBox.setObjectName("serviceComboBox")
        self.msgComboBox = QtGui.QComboBox(CreateTCView)
        self.msgComboBox.setGeometry(QtCore.QRect(330, 140, 85, 27))
        self.msgComboBox.setObjectName("msgComboBox")
        self.sendButton = QtGui.QPushButton(CreateTCView)
        self.sendButton.setGeometry(QtCore.QRect(360, 185, 51, 27))
        self.sendButton.setObjectName("sendButton")
        self.addTcButton = QtGui.QPushButton(CreateTCView)
        self.addTcButton.setGeometry(QtCore.QRect(320, 185, 31, 27))
        self.addTcButton.setObjectName("addTcButton")

        self.retranslateUi(CreateTCView)
        QtCore.QMetaObject.connectSlotsByName(CreateTCView)

    def retranslateUi(self, CreateTCView):
        CreateTCView.setWindowTitle(QtGui.QApplication.translate("CreateTCView", "Create TC", None, QtGui.QApplication.UnicodeUTF8))
        self.createTCLabel.setText(QtGui.QApplication.translate("CreateTCView", "Create Telecommand", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.historyList.isSortingEnabled()
        self.historyList.setSortingEnabled(False)
        self.historyList.item(0).setText(QtGui.QApplication.translate("CreateTCView", "1 ....", None, QtGui.QApplication.UnicodeUTF8))
        self.historyList.item(1).setText(QtGui.QApplication.translate("CreateTCView", "2 ....", None, QtGui.QApplication.UnicodeUTF8))
        self.historyList.item(2).setText(QtGui.QApplication.translate("CreateTCView", "3 ....", None, QtGui.QApplication.UnicodeUTF8))
        self.historyList.item(3).setText(QtGui.QApplication.translate("CreateTCView", "4 ....", None, QtGui.QApplication.UnicodeUTF8))
        self.historyList.setSortingEnabled(__sortingEnabled)
        self.label.setText(QtGui.QApplication.translate("CreateTCView", "History", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("CreateTCView", "Service type", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("CreateTCView", "Message subtype", None, QtGui.QApplication.UnicodeUTF8))
        self.sendButton.setText(QtGui.QApplication.translate("CreateTCView", "Send", None, QtGui.QApplication.UnicodeUTF8))
        self.addTcButton.setText(QtGui.QApplication.translate("CreateTCView", "+", None, QtGui.QApplication.UnicodeUTF8))

