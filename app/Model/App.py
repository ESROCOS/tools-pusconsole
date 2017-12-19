from Views import MainView
from Controller import MainViewController
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

    @Slot(dict, pb.pusPacket_t)
    def add(self, elem, packet):
        """
        This method adds a packet in its packet representation and json representation
        to the app packet table
        :param elem: json of packet
        :param packet: packet object
        """
        from datetime import datetime
        list_ = []
        type_ = int(elem["primary_header"]["pck_id"]["pck_type"])
        svc_type_id = int(elem["data"]["pck_sec_head"]["msg_type_id"]["service_type_id"])
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

    def set_filter(self, filter_: dict):
        self.currentFilter = filter_
        return self.__apply_filter__()

    def __apply_filter__(self):
        if self.currentFilter is None:
            return [e[0] for e in self.table]

        table = []
        type_ = self.currentFilter["type"]
        svc = self.currentFilter["svc"]
        msg = self.currentFilter["msg"]
        for e in self.table:
            aux = e
            if type_ != "":
                aux = e if e[1] == type_ else None
            if svc != 0 and aux is not None:
                aux = aux if aux[2] == svc else None
            if msg != 0 and aux is not None:
                aux = aux if aux[3] == msg else None
            if aux is not None:
                table.append(aux[0])
        return table

    @staticmethod
    def __create_info_string__(elem):
        """
        This method format a packet represented in json to a string
        (This method is not used currently because we found a similar
         functionality in json.dumps method)
        :param elem: A packet represented in json
        :return: The json formatted in an string
        """
        services = {}
        with open("services.txt", "r") as serv:
            for line in serv:
                line = line.strip('\n').split("|")
                if line[0] not in services:
                    services[line[0]] = {}
                if line[1] not in services[line[0]]:
                    services[line[0]][line[1]] = line[2]
        type_ = elem["primary_header"]["pck_id"]["pck_type"]
        svc_type_id = str(elem["data"]["pck_sec_head"]["msg_type_id"]["service_type_id"])
        msg_subtype_id = str(elem["data"]["pck_sec_head"]["msg_type_id"]["msg_subtype_id"])

        info = "Telemetry " if type_ == "TM" else "Telecommand " + "package."
        info += " " + services[svc_type_id][msg_subtype_id] + " ."

        return info

