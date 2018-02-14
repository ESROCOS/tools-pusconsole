# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddTCView.ui'
#
# Created: Wed Feb 14 10:56:34 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_AddTCView(object):
    def setupUi(self, AddTCView):
        AddTCView.setObjectName("AddTCView")
        AddTCView.resize(418, 727)
        self.buttonBox = QtGui.QDialogButtonBox(AddTCView)
        self.buttonBox.setGeometry(QtCore.QRect(70, 690, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.serviceComboBox = QtGui.QComboBox(AddTCView)
        self.serviceComboBox.setGeometry(QtCore.QRect(100, 70, 85, 27))
        self.serviceComboBox.setObjectName("serviceComboBox")
        self.label_4 = QtGui.QLabel(AddTCView)
        self.label_4.setGeometry(QtCore.QRect(10, 30, 401, 17))
        self.label_4.setObjectName("label_4")
        self.commandTextEdit = QtGui.QPlainTextEdit(AddTCView)
        self.commandTextEdit.setGeometry(QtCore.QRect(10, 150, 401, 521))
        self.commandTextEdit.setObjectName("commandTextEdit")
        self.label_2 = QtGui.QLabel(AddTCView)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 121, 17))
        self.label_2.setObjectName("label_2")
        self.label = QtGui.QLabel(AddTCView)
        self.label.setGeometry(QtCore.QRect(10, 10, 401, 17))
        self.label.setObjectName("label")
        self.addTCLabel = QtGui.QLabel(AddTCView)
        self.addTCLabel.setGeometry(QtCore.QRect(10, 120, 151, 17))
        self.addTCLabel.setObjectName("addTCLabel")
        self.label_3 = QtGui.QLabel(AddTCView)
        self.label_3.setGeometry(QtCore.QRect(200, 70, 121, 17))
        self.label_3.setObjectName("label_3")
        self.msgComboBox = QtGui.QComboBox(AddTCView)
        self.msgComboBox.setGeometry(QtCore.QRect(330, 70, 85, 27))
        self.msgComboBox.setObjectName("msgComboBox")

        self.retranslateUi(AddTCView)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), AddTCView.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), AddTCView.reject)
        QtCore.QMetaObject.connectSlotsByName(AddTCView)

    def retranslateUi(self, AddTCView):
        AddTCView.setWindowTitle(QtGui.QApplication.translate("AddTCView", "Add Telecommand", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("AddTCView", "st19 telecommand.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("AddTCView", "Service type", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("AddTCView", "Please create the telecommand that you want to add to ", None, QtGui.QApplication.UnicodeUTF8))
        self.addTCLabel.setText(QtGui.QApplication.translate("AddTCView", "Add Telecommand", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("AddTCView", "Message subtype", None, QtGui.QApplication.UnicodeUTF8))

