# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CreateTCView.ui'
#
# Created: Tue Feb 27 14:03:07 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_CreateTCView(object):
    def setupUi(self, CreateTCView):
        CreateTCView.setObjectName("CreateTCView")
        CreateTCView.resize(420, 736)
        self.commandTextEdit = QtGui.QPlainTextEdit(CreateTCView)
        self.commandTextEdit.setGeometry(QtCore.QRect(10, 220, 401, 511))
        self.commandTextEdit.setObjectName("commandTextEdit")
        self.createTCLabel = QtGui.QLabel(CreateTCView)
        self.createTCLabel.setGeometry(QtCore.QRect(10, 190, 151, 17))
        self.createTCLabel.setObjectName("createTCLabel")
        self.historyList = QtGui.QListWidget(CreateTCView)
        self.historyList.setGeometry(QtCore.QRect(10, 40, 401, 101))
        self.historyList.setObjectName("historyList")
        self.label = QtGui.QLabel(CreateTCView)
        self.label.setGeometry(QtCore.QRect(10, 10, 111, 17))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(CreateTCView)
        self.label_2.setGeometry(QtCore.QRect(10, 150, 121, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtGui.QLabel(CreateTCView)
        self.label_3.setGeometry(QtCore.QRect(200, 150, 121, 17))
        self.label_3.setObjectName("label_3")
        self.serviceComboBox = QtGui.QComboBox(CreateTCView)
        self.serviceComboBox.setGeometry(QtCore.QRect(100, 150, 81, 27))
        self.serviceComboBox.setObjectName("serviceComboBox")
        self.msgComboBox = QtGui.QComboBox(CreateTCView)
        self.msgComboBox.setGeometry(QtCore.QRect(330, 150, 81, 27))
        self.msgComboBox.setObjectName("msgComboBox")
        self.sendButton = QtGui.QPushButton(CreateTCView)
        self.sendButton.setGeometry(QtCore.QRect(360, 185, 51, 27))
        self.sendButton.setObjectName("sendButton")
        self.addTcButton = QtGui.QPushButton(CreateTCView)
        self.addTcButton.setGeometry(QtCore.QRect(320, 185, 31, 27))
        self.addTcButton.setObjectName("addTcButton")
        self.saveTcButton = QtGui.QPushButton(CreateTCView)
        self.saveTcButton.setGeometry(QtCore.QRect(340, 10, 71, 27))
        self.saveTcButton.setObjectName("saveTcButton")

        self.retranslateUi(CreateTCView)
        QtCore.QMetaObject.connectSlotsByName(CreateTCView)

    def retranslateUi(self, CreateTCView):
        CreateTCView.setWindowTitle(QtGui.QApplication.translate("CreateTCView", "Create TC", None, QtGui.QApplication.UnicodeUTF8))
        self.createTCLabel.setText(QtGui.QApplication.translate("CreateTCView", "Create Telecommand", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("CreateTCView", "History", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("CreateTCView", "Service type", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("CreateTCView", "Message subtype", None, QtGui.QApplication.UnicodeUTF8))
        self.sendButton.setText(QtGui.QApplication.translate("CreateTCView", "Send", None, QtGui.QApplication.UnicodeUTF8))
        self.addTcButton.setText(QtGui.QApplication.translate("CreateTCView", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.saveTcButton.setText(QtGui.QApplication.translate("CreateTCView", "Save TC", None, QtGui.QApplication.UnicodeUTF8))

