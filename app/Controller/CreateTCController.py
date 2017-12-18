from PySide import QtGui
from Model import CreateTCModel
from Views import CreateTCView
from Views import AddTCView
from Utilities import PacketTranslator, ValidateJson
from Controller import AddTCController
import os
import sys
import json

dir_path = os.path.dirname(os.path.realpath(__file__))
lib_path = os.path.join(dir_path, '../../../pus/debug/pylib')
sys.path.append(lib_path)
import pusbinding as pb


class CreateTCController(object):
    def __init__(self, model: CreateTCModel, view: CreateTCView):
        self.model = model
        self.view = view
        self.command = ""
        self.command_packet = None

        self.__add_telecommand()
        self.set_callbacks()
        self.svc_combobox_changed_callback(self.view.window.serviceComboBox.currentIndex())

    def set_callbacks(self):
        self.view.window.serviceComboBox.currentIndexChanged.connect(lambda i: self.svc_combobox_changed_callback(i))
        self.view.window.msgComboBox.currentIndexChanged.connect(lambda i: self.msg_combobox_changed_callback(i))
        self.view.window.sendButton.clicked.connect(self.send_callback)

    def __add_telecommand(self):
        for elem in sorted(self.model.telecommand, key=int):
            self.view.add_item_svc_type_combo_box(elem)

    def svc_combobox_changed_callback(self, index):
        svcComboBox = self.view.window.serviceComboBox
        svc = svcComboBox.itemText(index)
        self.view.clear_msg_type_combo_box()
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
            self.view.set_tc_text("")
            return

        self.command, self.command_packet = self.show_packet_json(svc_type, msg_type)
        if self.command is not None:
            self.view.set_tc_text(json.dumps(self.command["data"], indent=2))
        else:
            self.view.set_tc_text("")

    def send_callback(self):
        pt = PacketTranslator()
        vj = ValidateJson()

        try:
            self.command["data"] = self.view.get_tc_text()
            vj.check(self.command)
            self.model.add_to_table(self.command, pt.json2packet(self.command))
            self.view.close()
        except Exception as err:
            msg_box = QtGui.QMessageBox()
            msg_box.setText('Some fields may be incorrect {}'.format(err))
            msg_box.setStandardButtons(QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel)
            msg_box.exec_()

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
        elif svc == 19:
            if msg == 1:
                scndpacket = self.open_add_tc_window()

                if scndpacket is None:
                    self.view.window.msgComboBox.setCurrentIndex(0)
                    return None, None
                else:
                    print(pb.pus_tc_19_1_createAddEventActionDefinitionsRequest(packet, apid, seq, 0, scndpacket))
                    print(pb.getError())
            elif msg == 2:
                pb.pus_tc_19_2_createDeleteEventActionDefinitionsRequest(packet, apid, seq, 0)
            elif msg == 4:
                pb.pus_tc_19_4_createEnableEventActionDefinitions(packet, apid, seq, 0)
            elif msg == 5:
                pb.pus_tc_19_5_createDisableEventActionDefinitions(packet, apid, seq, 0)
        else:
            pass
        return packet_translator.packet2json(packet), packet

    def show(self):
        self.view.show()

    def open_add_tc_window(self):
        """
        This method opens a new window to create a telecommand that
        will be embedded in st19 telecommand
        :return: The inner telecommand
        """
        view = AddTCView()
        controller = AddTCController(self.model, view)
        return controller.show()
