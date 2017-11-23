import json
from PySide import QtCore, QtGui
from Model import App
import sys

gui = QtGui.QApplication(sys.argv)
app = App()
args = sys.argv()

if args[1] == "-test":
    with open('tm1.json') as json_data:
        d = json.load(json_data)
        app.add(d)
    with open('tm2.json') as json_data:
        d = json.load(json_data)
        app.add(d)
sys.exit(gui.exec_())
