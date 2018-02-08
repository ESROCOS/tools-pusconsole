from Utilities.MyTable import Table
from Utilities import PacketTranslator
from PySide.QtCore import Slot
import os, json, sys
lib_path = os.path.join('/home/esrocos/esrocos-ws-pus/pus/debug/pylib')
sys.path.append(lib_path)
import pusbinding as pb


class App(object):
    """
    This class represents the model of the application. It saves an
    instance of the packet table, the current filter and the apid of the
    app.
    """
    def __init__(self):
        """
        Constructor of the class
        """
        self.table = Table()
        self.tc_apid = pb.pusApidInfo_t()
        self.currentFilter = None
        self.elem_count = 0

        with open('apid.json', 'r') as json_apid:
            apid_value = json.load(json_apid)['apid']
            pb.pus_initApidInfo_null(self.tc_apid, apid_value)

    @Slot(pb.pusPacket_t)
    def add(self, packet):
        """
        This method adds a packet in its packet representation and json representation
        to the app packet table
        :param elem: json of packet
        """
        pt = PacketTranslator()
        elem = pt.packet2json(packet)
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
        list_.append(json.dumps(elem))
        list_.append(packet)
        self.table.append(list_)

    def set_filter(self, filter_: dict):
        """
        This method sets a filter and applies it to the table
        :param filter_: The filter to be applied
        """
        self.currentFilter = filter_
        return self.apply_filter()

    def apply_filter(self):
        """
        This method applies a filter to the table
        :return: A matrix with all the elements to be shown
        """
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
        """
        This method checks if an element passed as an argument
        satisfies the current filter
        :param e: The element to be checked
        :return: True if the element satisfies the filter
        and false in other case
        """
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
        """
        This static method creates the information string for each
        telemetry or telecommand in the table
        :param elem: The telemetry or telecommand packet
        :return: The information string
        """
        info = ""
        svc = elem["data"]["pck_sec_head"]["msg_type_id"]["service_type_id"]
        msg = elem["data"]["pck_sec_head"]["msg_type_id"]["msg_subtype_id"]
        data = elem["data"]
        src_data = data["user_data"]["src_data"]
        # ack_flags = data["pck_sec_head"]["ack_flags"]

        info = "-"
        if svc == 1:
            failure = src_data["failure"]
            request = src_data["request"]
            info = "Req. Apid = {}. ".format(request["apid"])
            if msg == 5 or msg == 6:
                info += "Step = {}. ".format(src_data["step"])
            if msg == 1 or msg == 4 or msg == 6 or msg == 8:
                info += "Failure = {}".format(failure["code"])
                # info += "Failure = {}, Address = {}, Data = {}, Subcode = {}. ".format(failure["code"],
                #                                                                      failure["info"]["address"],
                #                                                                      failure["info"]["data"],
                #                                                                      failure["info"]["subcode"])
        elif (svc, msg) == (3, 25):
            info = "Report id: {}. Params: ".format(src_data["hk_param_report_id"])
            params = []
            for k in sorted(src_data.keys()):
                if k != "hk_param_report_id":
                    params.append(str(src_data[k]))
            info += ', '.join(params)
        elif svc == 5:
            info = "Event id: {}. Data1: {}. Data2: {}".format(src_data["event_id"], src_data["auxdata"]["data1"],
                                                               src_data["auxdata"]["data2"])
        elif (svc, msg) == (8, 1):
            info = "Function id = {}.".format(src_data["function_id"])
        elif (svc, msg) == (9, 1):
            info = "Rate = 2^{}".format(src_data["exp_rate"])
        elif (svc, msg) == (11, 4):
            info = ""
            for i, k in enumerate(sorted(src_data.keys())):
                activity_i_packet = src_data[k]["packet"]["data"]["pck_sec_head"]["msg_type_id"]
                time_i = src_data[k]["time"]
                src = activity_i_packet["service_type_id"]
                msg = activity_i_packet["msg_subtype_id"]
                info += "Act{}: Time: {}, Packet: ({}, {}). ".format(i+1, time_i, src, msg)

        elif svc == 12:
            if msg == 1 or msg == 2:
                info = "Param monitoring id = {}".format(src_data["pmon_id"])
        elif svc == 19:
            info = "Event id = {}. ".format(src_data["event_id"])
            if msg == 1:
                request_data = data["user_data"]["src_data"]["request"]["data"]
                sub_svc = request_data["pck_sec_head"]["msg_type_id"]["service_type_id"]
                sub_msg = request_data["pck_sec_head"]["msg_type_id"]["msg_subtype_id"]
                info += "Packet request: ({}, {}).".format(sub_svc, sub_msg)
        elif svc == 20:
            info = "Param id = {}".format(src_data["param_id"])
            if msg == 2 or msg == 3:
                info += " Value = {}".format(src_data["value"])

        # ANADIR INFOSTRING 12


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

