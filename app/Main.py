import json, time, sys, collections
from PySide import QtCore, QtGui
from PySide.QtCore import QThread
from Model import App
from Utilities import PacketTranslator
from Controller import MainViewController

from Views import MainView
import os, sys
dir_path = os.path.dirname(os.path.realpath(__file__))
lib_path = os.path.join(dir_path, '../../pus/debug/pylib')
sys.path.append(lib_path)
import pusbinding as pb
import threading, time

"""
def work(app_):
    pt = PacketTranslator()
    with open("test.json", "r") as json_data:
        tcs = json.load(json_data)
        for elem in tcs["telecommands"]:
            time.sleep(elem["elapsed_time"])
            app_.add(elem["packet"], pt.json2packet(elem["packet"]))
"""


gui = QtGui.QApplication(sys.argv)
app = App()
view = MainView()
controller = MainViewController(app, view)

args = sys.argv

if len(args) > 1:
    if args[1] == "-test":
        controller.show()


sys.exit(gui.exec_())











"""
if len(args) > 1:
    if args[1] == "-test":
        apid_info = pb.pusApidInfo_t()
        packet = pb.pusPacket_t()
        packet2 = pb.pusPacket_t()
        packet3 = pb.pusPacket_t()
        packet4 = pb.pusPacket_t()
        packet5 = pb.pusPacket_t()
        packet6 = pb.pusPacket_t()
        packet7 = pb.pusPacket_t()
        packet8 = pb.pusPacket_t()

        pb.pus_initApidInfo_null(apid_info, 1)

        apid = pb.pus_getInfoApid(apid_info)

        seq = pb.pus_getNextPacketCount(apid_info)
        pb.pus_tc_17_1_createConnectionTestRequest(packet, apid, seq)

        seq = pb.pus_getNextPacketCount(apid_info)
        pb.pus_tm_1_1_createAcceptanceReportSuccess(packet2, apid, seq, packet)

        pb.pus_hk_initialize_null()
        seq = pb.pus_getNextPacketCount(apid_info)
        pb.pus_tm_3_25_createHousekeepingReportDefault(packet3, apid, seq, 10)
        pb.pus_hk_finalize()

        event = pb.pus_events_init_struct(6, 12, 23)
        pb.pus_events_initialize_null()
        seq = pb.pus_getNextPacketCount(apid_info)
        pb.pus_tm_5_4_createHighSeverityEventReport(packet4, apid, seq, event, 3)
        pb.pus_events_finalize()

        p = PacketTranslator()
        print(json.dumps(p.packet2json(packet2), indent=2))
        app.add(p.packet2json(packet), packet)
        import time
        time.sleep(1)
        app.add(p.packet2json(packet2), packet2)
        time.sleep(1)
        app.add(p.packet2json(packet3), packet3)
        time.sleep(1)
        app.add(p.packet2json(packet4), packet4)
        time.sleep(1)
        
        thread = QThread()
        thread.emit
        thread.start(target=work, args=(app,))
        thread.start()
sys.exit(gui.exec_())
"""
