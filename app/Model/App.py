from Views import MainView
from Controller import MainViewController
from Utilities import PacketTranslator
from Utilities.MyTable import Table
from PySide.QtCore import Slot
import os, json, sys
dir_path = os.path.dirname(os.path.realpath(__file__))
lib_path = os.path.join(dir_path, '../../../pus/debug/pylib')
sys.path.append(lib_path)
import pusbinding as pb


class App(object):

    def __init__(self):
        self.table = Table()
        self.tc_apid = pb.pusApidInfo_t()
        self.currentFilter = None
        self.elem_count = 0

        with open('apid.json', 'r') as json_apid:
            apid_value = json.load(json_apid)['apid']
            pb.pus_initApidInfo_null(self.tc_apid, apid_value)

    def add(self, elem, packet):
        """
        This method adds a packet in its packet representation and json representation
        to the app packet table
        :param elem: json of packet
        """
        from datetime import datetime
        list_ = []
        type_ = int(elem["primary_header"]["pck_id"]["pck_type"])
        svc_type_id = int(elem["data"]["pck_sec_head"]["msg_type_id"]["service_type_id"])
        print(svc_type_id)
        msg_subtype_id = int(elem["data"]["pck_sec_head"]["msg_type_id"]["msg_subtype_id"])
        time_ = str(datetime.now().time().strftime("%H:%M:%S"))
        if type_ == 0:
            src = None
            dst = int(elem["data"]["pck_sec_head"]["dst_id"])
        else:
            src = int(elem["data"]["pck_sec_head"]["src_id"])
            dst = None
        pck_seq_ctrl = int(elem["primary_header"]["pck_seq_ctrl"]["pck_seq"])
        status = "OK" # Mirar
        information = self.__create_info_string__(elem)

        list_.append(self.elem_count)
        self.elem_count+=1
        list_.append("TM" if type_ == 0 else "TC")
        list_.append(svc_type_id)
        list_.append(msg_subtype_id)
        list_.append(time_)
        list_.append(src)
        list_.append(dst)
        list_.append(pck_seq_ctrl)
        list_.append(status)
        list_.append(information)
        list_.append(packet)
        list_.append(json.dumps(elem))
        self.table.append(list_)
        print([t[2] for t in self.table])

    def set_filter(self, filter_: dict):
        self.currentFilter = filter_
        return self.apply_filter()

    def apply_filter(self):
        if self.currentFilter is None:
            return [e[0] for e in self.table]

        table = []
        type_ = self.currentFilter["type"]
        svc = self.currentFilter["svc"]
        msg = self.currentFilter["msg"]
        for e in self.table:
            if self.check_filter(e):
                table.append(e[0])
        return table

    def check_filter(self, e):
        if self.currentFilter is not None:
            type_ = self.currentFilter["type"]
            svc = self.currentFilter["svc"]
            msg = self.currentFilter["msg"]

            aux = e
            if type_ != "":
                aux = e if e[1] == type_ else None
            if svc != 0 and aux is not None:
                aux = aux if aux[2] == svc else None
            if msg != 0 and aux is not None:
                aux = aux if aux[3] == msg else None
            return aux is not None
        return True

    @staticmethod
    def __create_info_string__(elem):
        info = ""
        svc = elem["data"]["pck_sec_head"]["msg_type_id"]["service_type_id"]
        msg = elem["data"]["pck_sec_head"]["msg_type_id"]["msg_subtype_id"]
        data = elem["data"]
        src_data = data["user_data"]["src_data"]
        # ack_flags = data["pck_sec_head"]["ack_flags"]

        info = "-"
        if (svc, msg) == (8, 1):
            info = "Function id = {}.".format(src_data["function_id"])
        elif (svc, msg) == (9, 1):
            info = "Rate = 2^{}".format(src_data["exp_rate"])
        elif svc == 12:
            if msg == 1 or msg == 2:
                info = "Param monitoring id = {}".format(src_data["pmon_id"])


        # ack_str = " acks: none"
        # for k, v in ack_flags.items():
        #     if v:
        #         if ack_str == "acks: none":
        #             ack_str = "acks: "
        #         ack_str += k.split('_')[-1] + ", "
        return info

    # @staticmethod
    # def __create_info_string__(elem):
    #     """
    #     This method format a packet represented in json to a string
    #     (This method is not used currently because we found a similar
    #      functionality in json.dumps method)
    #     :param elem: A packet represented in json
    #     :return: The json formatted in an string
    #     """
    #     services = {}
    #     with open("services.txt", "r") as serv:
    #         for line in serv:
    #             line = line.strip('\n').split("|")
    #             if line[0] not in services:
    #                 services[line[0]] = {}
    #             if line[1] not in services[line[0]]:
    #                 services[line[0]][line[1]] = line[2]
    #     type_ = elem["primary_header"]["pck_id"]["pck_type"]
    #     svc_type_id = str(elem["data"]["pck_sec_head"]["msg_type_id"]["service_type_id"])
    #     msg_subtype_id = str(elem["data"]["pck_sec_head"]["msg_type_id"]["msg_subtype_id"])
    #
    #     info = "Telemetry " if type_ == "TM" else "Telecommand " + "package."
    #     info += " " + services[svc_type_id][msg_subtype_id] + " ."
    #
    #     return info

