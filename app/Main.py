import json
from PySide import QtCore, QtGui
from Model import App
import sys

gui = QtGui.QApplication(sys.argv)
app = App()
sys.exit(gui.exec_())
