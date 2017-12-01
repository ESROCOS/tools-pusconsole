import json, time, sys, collections
from PySide import QtCore, QtGui
from Model import App
from Utilities import PacketTranslator
import os, sys
dir_path = os.path.dirname(os.path.realpath(__file__))
lib_path = os.path.join(dir_path, '../../pus/debug/pylib')
sys.path.append(lib_path)
import pusbinding as pb

gui = QtGui.QApplication(sys.argv)
app = App()
args = sys.argv

if len(args) > 1:
    if args[1] == "-test":
        apid = pb.pusApidInfo_t()
        packet = pb.pusPacket_t()
        pb.pus_initApidInfo_(apid, 1)
        pb.pus_tm_17_2_createConnectionTestReport(packet, apid, 2)
        p = PacketTranslator()
        app.add(p.packet2json(packet))
sys.exit(gui.exec_())

