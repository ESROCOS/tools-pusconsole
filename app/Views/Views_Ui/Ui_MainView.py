# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainView.ui'
#
# Created: Tue Apr  3 11:38:39 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainView(object):
    def setupUi(self, MainView):
        MainView.setObjectName("MainView")
        MainView.resize(1201, 596)
        self.centralwidget = QtGui.QWidget(MainView)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(1140, 0, 51, 31))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 1181, 531))
        self.tabWidget.setObjectName("tabWidget")
        self.packetTab = QtGui.QWidget()
        self.packetTab.setObjectName("packetTab")
        self.gridLayout = QtGui.QGridLayout(self.packetTab)
        self.gridLayout.setObjectName("gridLayout")
        self.packagesTable = QtGui.QTableWidget(self.packetTab)
        self.packagesTable.setObjectName("packagesTable")
        self.packagesTable.setColumnCount(10)
        self.packagesTable.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.packagesTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.packagesTable.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.packagesTable.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.packagesTable.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.packagesTable.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.packagesTable.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.packagesTable.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.packagesTable.setHorizontalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.packagesTable.setHorizontalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        self.packagesTable.setHorizontalHeaderItem(9, item)
        self.gridLayout.addWidget(self.packagesTable, 0, 0, 1, 1)
        self.tabWidget.addTab(self.packetTab, "")
        self.statusTab = QtGui.QWidget()
        self.statusTab.setObjectName("statusTab")
        self.hkParamList = QtGui.QListWidget(self.statusTab)
        self.hkParamList.setGeometry(QtCore.QRect(10, 60, 361, 431))
        self.hkParamList.setObjectName("hkParamList")
        self.spacecraftTimeLbl = QtGui.QLabel(self.statusTab)
        self.spacecraftTimeLbl.setGeometry(QtCore.QRect(10, 10, 121, 17))
        self.spacecraftTimeLbl.setObjectName("spacecraftTimeLbl")
        self.hkParamsLbl = QtGui.QLabel(self.statusTab)
        self.hkParamsLbl.setGeometry(QtCore.QRect(10, 40, 191, 17))
        self.hkParamsLbl.setObjectName("hkParamsLbl")
        self.sysParamsLabel = QtGui.QLabel(self.statusTab)
        self.sysParamsLabel.setGeometry(QtCore.QRect(390, 40, 141, 17))
        self.sysParamsLabel.setObjectName("sysParamsLabel")
        self.sysParamsList = QtGui.QListWidget(self.statusTab)
        self.sysParamsList.setGeometry(QtCore.QRect(390, 60, 361, 431))
        self.sysParamsList.setObjectName("sysParamsList")
        self.tabWidget.addTab(self.statusTab, "")
        MainView.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainView)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1201, 25))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuFilter = QtGui.QMenu(self.menubar)
        self.menuFilter.setObjectName("menuFilter")
        MainView.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainView)
        self.statusbar.setObjectName("statusbar")
        MainView.setStatusBar(self.statusbar)
        self.actionNew_connection = QtGui.QAction(MainView)
        self.actionNew_connection.setObjectName("actionNew_connection")
        self.actionSave_as = QtGui.QAction(MainView)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionLoad = QtGui.QAction(MainView)
        self.actionLoad.setObjectName("actionLoad")
        self.actionAbout_GMV = QtGui.QAction(MainView)
        self.actionAbout_GMV.setObjectName("actionAbout_GMV")
        self.actionCreate_TC = QtGui.QAction(MainView)
        self.actionCreate_TC.setObjectName("actionCreate_TC")
        self.actionCreate_filter = QtGui.QAction(MainView)
        self.actionCreate_filter.setObjectName("actionCreate_filter")
        self.actionDelete_filter = QtGui.QAction(MainView)
        self.actionDelete_filter.setObjectName("actionDelete_filter")
        self.actionLoad_TCs = QtGui.QAction(MainView)
        self.actionLoad_TCs.setObjectName("actionLoad_TCs")
        self.menuFile.addAction(self.actionSave_as)
        self.menuFile.addAction(self.actionLoad)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionCreate_TC)
        self.menuFile.addAction(self.actionLoad_TCs)
        self.menuHelp.addAction(self.actionAbout_GMV)
        self.menuFilter.addAction(self.actionCreate_filter)
        self.menuFilter.addAction(self.actionDelete_filter)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuFilter.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainView)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainView)

    def retranslateUi(self, MainView):
        MainView.setWindowTitle(QtGui.QApplication.translate("MainView", "Pus Console", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainView", "<html><head/><body><p><img src=\"Views/Views_Ui/images/logo_gmv.svg\" width=\"125\" height=\"70\"/></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.packagesTable.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("MainView", "Type", None, QtGui.QApplication.UnicodeUTF8))
        self.packagesTable.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("MainView", "Service ID", None, QtGui.QApplication.UnicodeUTF8))
        self.packagesTable.horizontalHeaderItem(3).setText(QtGui.QApplication.translate("MainView", "Message ID", None, QtGui.QApplication.UnicodeUTF8))
        self.packagesTable.horizontalHeaderItem(4).setText(QtGui.QApplication.translate("MainView", "Time", None, QtGui.QApplication.UnicodeUTF8))
        self.packagesTable.horizontalHeaderItem(5).setText(QtGui.QApplication.translate("MainView", "Source", None, QtGui.QApplication.UnicodeUTF8))
        self.packagesTable.horizontalHeaderItem(6).setText(QtGui.QApplication.translate("MainView", "Destination", None, QtGui.QApplication.UnicodeUTF8))
        self.packagesTable.horizontalHeaderItem(7).setText(QtGui.QApplication.translate("MainView", "Sequence", None, QtGui.QApplication.UnicodeUTF8))
        self.packagesTable.horizontalHeaderItem(8).setText(QtGui.QApplication.translate("MainView", "Status", None, QtGui.QApplication.UnicodeUTF8))
        self.packagesTable.horizontalHeaderItem(9).setText(QtGui.QApplication.translate("MainView", "Information", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.packetTab), QtGui.QApplication.translate("MainView", "Packets", None, QtGui.QApplication.UnicodeUTF8))
        self.spacecraftTimeLbl.setText(QtGui.QApplication.translate("MainView", "SpacecraftTime:", None, QtGui.QApplication.UnicodeUTF8))
        self.hkParamsLbl.setText(QtGui.QApplication.translate("MainView", "Housekeeping parameters", None, QtGui.QApplication.UnicodeUTF8))
        self.sysParamsLabel.setText(QtGui.QApplication.translate("MainView", "System parameters", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.statusTab), QtGui.QApplication.translate("MainView", "System status", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainView", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainView", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFilter.setTitle(QtGui.QApplication.translate("MainView", "Filter", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew_connection.setText(QtGui.QApplication.translate("MainView", "New connection", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_as.setText(QtGui.QApplication.translate("MainView", "Save as ...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoad.setText(QtGui.QApplication.translate("MainView", "Load", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout_GMV.setText(QtGui.QApplication.translate("MainView", "About GMV", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCreate_TC.setText(QtGui.QApplication.translate("MainView", "Create TC", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCreate_filter.setText(QtGui.QApplication.translate("MainView", "Create filter", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDelete_filter.setText(QtGui.QApplication.translate("MainView", "Delete filter", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoad_TCs.setText(QtGui.QApplication.translate("MainView", "Load TCs", None, QtGui.QApplication.UnicodeUTF8))
