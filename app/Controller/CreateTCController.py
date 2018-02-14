from PySide import QtGui
from PySide.QtGui import QInputDialog
from Model import CreateTCModel
from Views import CreateTCView
from Views import AddTCView
from Utilities import PacketTranslator, ValidateJson, MakoTranslate, Database
from .AddTCController import AddTCController
from jsonschema.exceptions import ValidationError
import os
import sys
import json

# dir_path = os.path.dirname(os.path.realpath(__file__))
lib_path = os.path.join('/home/esrocos/esrocos-ws-pus/pus/debug/pylib')
sys.path.append(lib_path)
import pusbinding as pb


class CreateTCController(object):
    """
    This class controls CreateTCView
    """
    def __init__(self, model: CreateTCModel, view: CreateTCView):
        """
        Constructor of the class
        :param model: The model the controller references
        :param view: The view the controller references
        """
        self.model = model
        self.view = view
        self.command = ""
        self.command_packet = None

        self.HISTORY_DB = ".tc_history"

        self.__add_telecommand()
        self.set_callbacks()
        self.svc_combobox_changed_callback(self.view.window.serviceComboBox.currentIndex())
        self.show_history()

    def set_callbacks(self):
        """
        This method is used to set the callbacks to every action that the
        user triggers
        """
        self.view.window.serviceComboBox.currentIndexChanged.connect(lambda i: self.svc_combobox_changed_callback(i))
        self.view.window.msgComboBox.activated.connect(lambda i: self.msg_combobox_changed_callback(i))
        self.view.window.sendButton.clicked.connect(self.send_callback)
        self.view.window.addTcButton.clicked.connect(self.add_tc_callback)
        self.view.window.historyList.currentItemChanged.connect(self.history_click_callback)
        self.view.window.saveTcButton.clicked.connect(self.save_tc_history_callback)

    def __add_telecommand(self):
        """
        This method fills service id combobox
        """
        for elem in sorted(self.model.telecommand, key=int):
            self.view.add_item_svc_type_combo_box(elem)

    def svc_combobox_changed_callback(self, index):
        """
        This method is triggered when the selected index of the
        service id combobox changes. This method fills the message
        id combobox depending on the service id selected.
        :param index: The new selected index
        """
        svcComboBox = self.view.window.serviceComboBox
        svc = svcComboBox.itemText(index)
        self.view.clear_msg_type_combo_box()
        self.view.window.msgComboBox.addItem("", None)
        for msg in sorted(self.model.telecommand[svc], key=int):
            self.view.add_item_msg_type_combo_box(msg)

    def msg_combobox_changed_callback(self, index):
        """
        This method is triggered when the selected index of the
        message id combobox changes. This method creates a default
        packet of type (service id, message id)
        :param index: The new selected index
        """
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

    def history_click_callback(self, current, _):
        text = current.text()
        d = Database(self.HISTORY_DB)
        d.create_history_table()  # Create if not exists
        rowid = text[3]
        name = text.split(":")[1]
        query = "SELECT packets from history where rowid = ? and name = ?"
        tcs = d.query_db(query, (rowid, name))
        for tc in tcs:
            self.command = json.loads(tc[0])
            svc = self.command["data"]["pck_sec_head"]["msg_type_id"]["service_type_id"]
            msg = self.command["data"]["pck_sec_head"]["msg_type_id"]["msg_subtype_id"]
            svc_cbox = self.view.window.serviceComboBox
            msg_cbox = self.view.window.msgComboBox
            svc_index = svc_cbox.findData(svc)
            svc_cbox.setCurrentIndex(svc_index)
            #svc_combobox_changed_callback(svc_index)
            msg_index = msg_cbox.findData(msg)
            msg_cbox.setCurrentIndex(msg_index)
            self.view.set_tc_text(json.dumps(self.command["data"], indent=2))
            break

    def send_callback(self):
        """
        This method is triggered when the user hits the send button.
        This method creates a packet from the json and validates that
        every field on that json is correct
        """
        mt = MakoTranslate()
        pt = PacketTranslator()
        vj = ValidateJson()

        data_section = self.view.get_tc_text()
        data_section = json.loads(mt.replace(data_section))
        try:
            self.command["data"] = data_section
            vj.check(self.command)
            packet = pt.json2packet(self.command)
            pb.pus_notify_sendPacket(packet)
            self.model.add_to_table(packet)  # Packet is created from json
            self.view.window.addTcButton.hide()
            self.view.close()
        except ValidationError as err:
            msg_box = QtGui.QMessageBox()
            msg_box.setText('Some fields may be incorrect {}'.format(err))
            msg_box.setStandardButtons(QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel)
            msg_box.exec_()

    def add_tc_callback(self):
        """
        This method is triggered when the user creates a st19_1 or st11_4 telecommand
        and clicks the plus button to add an activity inside it. This method
        opens an addTcView window to create the telecommand to be embedded.
        """
        packet_translator = PacketTranslator()
        scndpacket = self.open_add_tc_window()
        if scndpacket is not None:
            now = pb.pusTime_t()
            pb.pus_now(now) # Revisar
            pb.pus_tc_11_4_setActivity(self.command_packet, scndpacket, now) # Revisar
            self.command = packet_translator.packet2json(self.command_packet)
            self.view.set_tc_text(json.dumps(self.command["data"], indent=2))

    def save_tc_history_callback(self):
        mt = MakoTranslate()

        d = Database(self.HISTORY_DB)
        d.create_history_table()

        widget_gui = QInputDialog()
        save_name, ok = QInputDialog.getText(widget_gui, "Save TC", "Name of TC to be saved:")

        if not ok:
            return

        data_section = json.loads(mt.replace(self.view.get_tc_text()))
        self.command["data"] = data_section
        d.insert_db("INSERT INTO history VALUES(?, ?)", [[save_name, json.dumps(self.command)]])
        self.show_history()

    def show_history(self):
        self.view.clear_history_list()
        d = Database(self.HISTORY_DB)
        d.create_history_table()
        query = "SELECT rowid, * FROM history"
        packets_list = d.query_db(query)
        for p in packets_list:
            name = p[1]
            dic = json.loads(p[2])
            svc = str(dic["data"]["pck_sec_head"]["msg_type_id"]["service_type_id"])
            msg = str(dic["data"]["pck_sec_head"]["msg_type_id"]["msg_subtype_id"])
            tc = "TC "+str(p[0])+":"
            if name is None:
                tc += "Type->"+svc+"_"+msg
            else:
                tc += name
            self.view.add_item_history_list(tc)

    def show_packet_json(self, svc, msg):
        """
        This method writes the packet with the service id and message id
        specified in json format in the textbox of the window.
        :param svc: Service id of the packet
        :param msg: Message id of the packet
        :return: The packet in json format
        """
        packet = pb.pusPacket_t()
        packet_translator = PacketTranslator()
        apid_info = self.model.apid_info
        apid = pb.pus_getInfoApid(apid_info)
        seq = pb.pus_getNextPacketCount(apid_info) # REVISAR parece que la secuencia no aumenta

        if (svc, msg) == (8, 1):
            pb.pus_tc_8_1_createPerformFuctionRequest(packet, apid, seq, 0)
        elif (svc, msg) == (9, 1):
            pb.pus_tc_9_1_createSetTimeReportRate(packet, apid, seq, 0)
        elif svc == 12:
            if msg == 1:
                pb.pus_tc_12_1_createEnableParameterMonitoringDefinitions(packet, apid, seq, 0)
            elif msg == 2:
                pb.pus_tc_12_2_createDisableParameterMonitoringDefinitions(packet, apid, seq, 0)
            elif msg == 15:
                pb.pus_tc_12_15_createEnableParameterMonitoring(packet, apid, seq)
            elif msg == 16:
                pb.pus_tc_12_16_createDisableParameterMonitoring(packet, apid, seq)
        elif svc == 11:
            if msg == 1:
                print(pb.pus_tc_11_1_createEnableTimeBasedSchedule(packet, apid, seq))
            elif msg == 2:
                pb.pus_tc_11_2_createDisableTimeBasedSchedule(packet, apid, seq)
            elif msg == 3:
                pb.pus_tc_11_3_createResetTimeBasedSchedule(packet, apid, seq)
            elif msg == 4:
                self.view.window.addTcButton.show()
                pb.pus_tc_11_4_createInsertActivityIntoSchedule(packet, apid, seq)
                scndpacket = self.open_add_tc_window()
                packet_translator.packet2json(scndpacket)
                if scndpacket is None:
                    self.view.window.msgComboBox.setCurrentIndex(0)
                    return None, None
                else:
                    now = pb.pusTime_t() # REVISAR: EL TIEMPO TIENE QUE SER ESPECIFICADO
                    pb.pus_now(now)
                    print(pb.pus_tc_11_4_setActivity(packet, scndpacket, now))
        elif (svc, msg) == (17, 1):
            pb.pus_tc_17_1_createConnectionTestRequest(packet, apid, seq)
        elif svc == 19:
            if msg == 1:
                scndpacket = self.open_add_tc_window()
                if scndpacket is None:
                    self.view.window.msgComboBox.setCurrentIndex(0)
                    return None, None
                else:
                    pb.pus_tc_19_1_createAddEventActionDefinitionsRequest(packet, apid, seq, 0, scndpacket)
            elif msg == 2:
                print(pb.pus_tc_19_2_createDeleteEventActionDefinitionsRequest(packet, apid, seq, 0))
            elif msg == 4:
                pb.pus_tc_19_4_createEnableEventActionDefinitions(packet, apid, seq, 0)
            elif msg == 5:
                pb.pus_tc_19_5_createDisableEventActionDefinitions(packet, apid, seq, 0)
        elif svc == 20:
            if msg == 1:
                pb.pus_tc_20_1_createParameterValueRequest(packet, apid, seq, 0)
            elif msg == 3:
                pb.pus_tc_20_3_createSetParameterValueRequest(packet, apid, seq, 0, 0)
        elif svc == 23:
            if msg == 1:
                pb.pus_tc_23_1_createCreateFileRequest(packet, apid, seq, "", "", 0)
            elif msg == 2:
                pb.pus_tc_23_2_createDeleteFileRequest(packet, apid, seq, "", "")
            elif msg == 3:
                pb.pus_tc_23_3_createReportFileAtributesRequest(packet, apid, seq, "", "")
            elif msg == 14:
                pb.pus_tc_23_14_createCopyFileRequest(packet, apid, seq, "", "", "", "")

        else:
            pass
        return packet_translator.packet2json(packet), packet

    def show(self):
        """
        This method calls the .show() method of the view
        """
        self.view.show()

    def open_add_tc_window(self):
        """
        This method opens a new window to create a telecommand that
        will be embedded in st11 or st19 telecommands
        :return: The inner telecommand
        """
        view = AddTCView()
        controller = AddTCController(self.model, view)
        return controller.show()
