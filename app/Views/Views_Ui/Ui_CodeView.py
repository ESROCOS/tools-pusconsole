# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CodeView.ui'
#
# Created: Tue Mar  6 14:04:59 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_CodeView(object):
    def setupUi(self, CodeView):
        CodeView.setObjectName("CodeView")
        CodeView.resize(412, 297)
        self.buttonBox = QtGui.QDialogButtonBox(CodeView)
        self.buttonBox.setGeometry(QtCore.QRect(50, 260, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.plainTextEdit = QtGui.QPlainTextEdit(CodeView)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 10, 391, 241))
        self.plainTextEdit.setObjectName("plainTextEdit")

        self.retranslateUi(CodeView)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), CodeView.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), CodeView.reject)
        QtCore.QMetaObject.connectSlotsByName(CodeView)

    def retranslateUi(self, CodeView):
        CodeView.setWindowTitle(QtGui.QApplication.translate("CodeView", "Code", None, QtGui.QApplication.UnicodeUTF8))

