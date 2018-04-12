from mako.template import Template
from datetime import datetime
import json, os, sys, time
lib_path = os.path.join('/home/esrocos/esrocos-ws-pus/tools-libpus/debug/pylib')
sys.path.append(lib_path)
import pusbinding as pb


class MakoTranslate(object):
    def __init__(self):
        self.version = {"V0": 0, "V1": 1, "INVALID_VERSION": 15}
        self.st3_12_params = dict()
        self.st20_params = dict()
        self.st5_events = dict()
        param_id = 0
        read_value = " "
        while read_value is not None:
            read_value = pb.pus_st20_getOnBoardReportInfoName(param_id)
            if read_value is not None:
                self.st20_params[read_value] = param_id
            param_id += 1

        #  In the future library there can be more than one report id
        param_id = 0
        read_value = pb.pus_st03_getHkReportInfoName(0, param_id)
        while read_value is not None:
            self.st3_12_params[read_value] = param_id
            param_id += 1
            read_value = pb.pus_st03_getHkReportInfoName(0, param_id)

        param_id = 0
        read_value = pb.pus_st05_getEventName(param_id)
        while read_value is not None:
            self.st5_events[read_value] = param_id
            param_id += 1
            read_value = pb.pus_st05_getEventName(param_id)

        self.values = [self.version, self.st3_12_params, self.st20_params, self.st5_events]

        self.template_values = ""
        self.__create_value_string__()

    def __create_value_string__(self):
        for elem in self.values:
            for k, v in elem.items():
                self.template_values += "<%{} = {}%>".format(k, v)

    def replace(self, json_data):
        if type(json_data) is dict:
            data = json.dumps(json_data)
        else:
            data = json_data

        res = Template(self.template_values + data).render(macros=Macros())
        return res


class Macros:
    @staticmethod
    def primary_header_defaults(seq=0):
        name = "\"primary_header\": "
        data = {
                "pck_data_len": 5736,
                "pck_seq_ctrl": {
                        "pck_seq": seq,
                        "pck_seq_flg": 3
                },
                "pck_id": {
                        "sec_head_flg": True,
                        "apid": 1,
                        "pck_type": 1
                },
                "pck_version": 0
        }

        return name + json.dumps(data, indent=8)

    @staticmethod
    def acks(start=0, acceptance=0, completion=0, progress=0):
        name = "\"ack_flags\": "
        data = {
            "ack_flag_start": bool(start),
            "ack_flag_acceptance": bool(acceptance),
            "ack_flag_completion": bool(completion),
            "ack_flag_progress": bool(progress)
          }

        return name + json.dumps(data, indent=8)


    @staticmethod
    def tc_type(svc, msg):
        name = "\"msg_type_id\": "
        data = {
            "service_type_id": svc,
            "msg_subtype_id": msg
        }

        return name + json.dumps(data, indent=8)

    @staticmethod
    def datetime_to_int(s):
        d = datetime.strptime(s, "%d/%m/%Y %H:%M:%S")
        return int(time.mktime(d.timetuple()))
