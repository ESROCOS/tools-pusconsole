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
        packet2 = pb.pusPacket_t()
        packet3 = pb.pusPacket_t()
        packet4 = pb.pusPacket_t()

        pb.pus_initApidInfo_(apid, 1)

        pb.pus_tc_17_1_createConnectionTestRequest(packet, apid)
        pb.pus_tm_1_1_createAcceptanceReportSuccess(packet2, apid, packet)
        pb.pus_hk_initialize_null()
        pb.pus_tm_3_25_createHousekeepingReportDefault(packet3, apid, 10)
        pb.pus_hk_finalize()
        event = pb.pus_events_init_struct(6, 12, 23)
        pb.pus_events_initialize_null()
        print(pb.pus_tm_5_4_createHighSeverityEventReport(packet4, apid, event, 3))
        pb.pus_events_finalize()

        p = PacketTranslator()
        app.add(p.packet2json(packet), packet)
        import time
        time.sleep(1)
        app.add(p.packet2json(packet2), packet2)
        time.sleep(1)
        app.add(p.packet2json(packet3), packet3)
        time.sleep(1)
        app.add(p.packet2json(packet4), packet4)
        time.sleep(1)
sys.exit(gui.exec_())

