from PySide import QtCore
from Model import CreateTCModel
from Views.CreateTCView import CreateTCView
from Utilities import PacketTranslator
import os


class CreateTCController(object):
    def __init__(self, model: CreateTCModel, view: CreateTCView):
        self.model = model
        self.view = view

        self.__add_telecommand()
        self.set_callbacks()
        self.svc_combobox_changed(self.view.window.serviceComboBox.currentIndex())

        with open("tc-template.json") as tc_json:
            tc = "".join(tc_json.readlines())
            self.view.set_tc_text(tc)

    def set_callbacks(self):
        self.view.window.serviceComboBox.currentIndexChanged.connect(lambda i: self.svc_combobox_changed(i))
        self.view.window.msgComboBox.currentIndexChanged.connect(lambda i: self.msg_combobox_changed(i))

    def __add_telecommand(self):
        for elem in sorted(self.model.telecommand):
            self.view.add_item_svc_type_combo_box(elem)

    def svc_combobox_changed(self, index):
        svcComboBox = self.view.window.serviceComboBox
        svc = svcComboBox.itemText(index)
        self.view.clear_msg_type_combo_box()
        for msg in self.model.telecommand[svc]:
            self.view.add_item_msg_type_combo_box(msg)

    def msg_combobox_changed(self, index):
        svcComboBox = self.view.window.serviceComboBox
        msgComboBox = self.view.window.msgComboBox

        svc_index = svcComboBox.currentIndex()

        svc_type = svcComboBox.itemData(svc_index)
        msg_type = msgComboBox.itemData(index)

        if msg_type is None:
            return

        self.show_packet_json(svc_type, msg_type)

    def show_packet_json(self, svc, msg):
        packet = pb.pusPacket_t()
        apid = pb.pusApidInfo_t()
        pb.pus_initApidInfo_(apid, os.getpid())
        packetTranslator = PacketTranslator()
        if (svc, msg) == (17, 1):
            pb.pus_tc_17_1_createConnectionTestRequest(packet, apid)
            print(packetTranslator.packet2json(packet))
            return 0
        else:
            pass



    def show(self):
        self.view.show()


