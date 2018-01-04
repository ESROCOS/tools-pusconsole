from PySide import QtCore
from Model import CreateTCModel
from Views.AddTCView import AddTCView
from Utilities import PacketTranslator
import os, sys, json
dir_path = os.path.dirname(os.path.realpath(__file__))
lib_path = os.path.join(dir_path, '../../../pus/debug/pylib')
sys.path.append(lib_path)
import pusbinding as pb


class AddTCController(object):
    def __init__(self, model: CreateTCModel, view: AddTCView):
        self.model = model
        self.view = view
        self.command = ""

        self.__add_telecommand()
        self.set_callbacks()
        self.svc_combobox_changed_callback(self.view.window.serviceComboBox.currentIndex())

    def set_callbacks(self):
        self.view.window.serviceComboBox.currentIndexChanged.connect(lambda i: self.svc_combobox_changed_callback(i))
        self.view.window.msgComboBox.currentIndexChanged.connect(lambda i: self.msg_combobox_changed_callback(i))

    def __add_telecommand(self):
        excluded = ("19", "11")
        for elem in sorted(self.model.telecommand, key=int):
            if elem not in excluded:
                self.view.add_item_svc_type_combo_box(elem)

    def svc_combobox_changed_callback(self, index):
        svcComboBox = self.view.window.serviceComboBox
        svc = svcComboBox.itemText(index)
        self.view.window.msgComboBox.addItem("", None)
        for msg in sorted(self.model.telecommand[svc], key=int):
            self.view.add_item_msg_type_combo_box(msg)

    def msg_combobox_changed_callback(self, index):
        svcComboBox = self.view.window.serviceComboBox
        msgComboBox = self.view.window.msgComboBox

        svc_index = svcComboBox.currentIndex()

        svc_type = svcComboBox.itemData(svc_index)
        msg_type = msgComboBox.itemData(index)

        if msg_type is None:
            return

        self.command = self.show_packet_json(svc_type, msg_type)
        self.view.current_json = json.dumps(self.command)
        self.view.set_tc_text(json.dumps(self.command["data"], indent=2))

    def show_packet_json(self, svc, msg):
        packet = pb.pusPacket_t()
        packet_translator = PacketTranslator()

        apid_info = self.model.apid_info
        apid = pb.pus_getInfoApid(apid_info)
        seq = pb.pus_getNextPacketCount(apid_info)

        if (svc, msg) == (8, 1):
            pb.pus_tc_8_1_createPerformFuctionRequest(packet, apid, seq, 0)
        elif svc == 12:
            if msg == 1:
                pb.pus_tc_12_1_createEnableParameterMonitoringDefinitions(packet, apid, seq, 0)
            elif msg == 2:
                pb.pus_tc_12_2_createDisableParameterMonitoringDefinitions(packet, apid, seq, 0)
            elif msg == 15:
                pb.pus_tc_12_15_createEnableParameterMonitoring(packet, apid, seq)
            elif msg == 16:
                pb.pus_tc_12_16_createDisableParameterMonitoring(packet, apid, seq)
        elif (svc, msg) == (17, 1):
            pb.pus_tc_17_1_createConnectionTestRequest(packet, apid, seq)
        else:
            pass
        return packet_translator.packet2json(packet)

    def show(self):
        code = self.view.show()
        packet_translator = PacketTranslator()
        self.command["data"] = self.view.get_tc_text()
        print(self.command["data"])
        if code == 1:
            packet = packet_translator.json2packet(self.command)
            return packet
        else:
            return None
