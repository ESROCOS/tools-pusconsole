import json

from Views import MainView
from Controller import MainViewController
from Utilities.MyTable import Table


class App(object):

    def __init__(self):
        self.table = Table()

        main_window = MainView()
        self.c = MainViewController(self, main_window)
        self.c.set_callbacks()
        self.c.show()

    def add(self, elem: dict):
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

        list_.append("TM" if type_ == 0 else "TC")
        list_.append(svc_type_id)
        list_.append(msg_subtype_id)
        list_.append(time_)
        list_.append(src)
        list_.append(dst)
        list_.append(pck_seq_ctrl)
        list_.append(status)
        list_.append(information)
        list_.append(json.dumps(elem))
        self.table.append(list_)

    @staticmethod
    def __create_info_string__(elem):
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

