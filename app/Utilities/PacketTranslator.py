import os, sys, collections, time, glob
dir_path = os.path.dirname(os.path.realpath(__file__))
lib_path = os.path.join(dir_path, '../../../pus/debug/pylib')
sys.path.append(lib_path)
import pusbinding as pb


class PacketTranslator(object):

    def packet2json(self, pack):
        jsn = collections.OrderedDict()
        jsn["primary_header"] = collections.OrderedDict()
        jsn["data"] = collections.OrderedDict()
        jsn["primary_header"]["pck_version"] = pb.pus_getPacketVersion(pack)
        jsn["primary_header"]["pck_id"] = collections.OrderedDict()
        type_ = jsn["primary_header"]["pck_id"]["pck_type"] = pb.pus_getPacketType(pack)
        jsn["primary_header"]["pck_id"]["sec_head_flg"] = pb.pus_getSecondaryHeaderFlag(pack)
        jsn["primary_header"]["pck_id"]["apid"] = pb.pus_getApid(pack)
        jsn["primary_header"]["pck_seq_ctrl"] = collections.OrderedDict()
        jsn["primary_header"]["pck_seq_ctrl"]["pck_seq_flg"] = pb.pus_getSequenceFlags(pack)
        jsn["primary_header"]["pck_seq_ctrl"]["pck_seq"] = pb.pus_getSequenceCount(pack)
        jsn["primary_header"]["pck_data_len"] = pb.pus_getPacketDataLength(pack)
        jsn["data"] = collections.OrderedDict()
        jsn["data"]["pck_sec_head"] = collections.OrderedDict()
        jsn["data"]["user_data"] = collections.OrderedDict()
        if type_ == 0:  # TM
            jsn["data"]["pck_sec_head"]["tm_packet_pus_version_number"] = pb.pus_getTmPusVersion(pack)
            jsn["data"]["pck_sec_head"]["spacecraft_time"] = pb.pus_getTmTimeReferenceStatus(pack)
            srvc_type_id = pb.pus_getTmService(pack)
            msg_type_id = pb.pus_getTmSubtype(pack)
            jsn["data"]["pck_sec_head"]["msg_type_counter"] = pb.pus_getTmMessageTypeCounter(pack)
            jsn["data"]["pck_sec_head"]["dst_id"] = pb.pus_getTmDestination(pack)
            jsn["data"]["pck_sec_head"]["time"] = time.strftime("%H:%M:%S", time.gmtime(pb.pus_getTmPacketTime(pack)))
        else:
            jsn["data"]["pck_sec_head"]["tc_packet_pus_version_number"] = pb.pus_getTcPusVersion(pack)
            jsn["data"]["pck_sec_head"]["ack_flags"] = collections.OrderedDict()
            jsn["data"]["pck_sec_head"]["ack_flags"]["ack_flag_acceptance"] = pb.pus_getTcAckFlagAcceptance(pack)
            jsn["data"]["pck_sec_head"]["ack_flags"]["ack_flag_start"] = pb.pus_getTcAckFlagStart(pack)
            jsn["data"]["pck_sec_head"]["ack_flags"]["ack_flag_progress"] = pb.pus_getTcAckFlagProgress(pack)
            jsn["data"]["pck_sec_head"]["ack_flags"]["ack_flag_completion"] = pb.pus_getTcAckFlagCompletion(pack)
            srvc_type_id = pb.pus_getTcService(pack)
            msg_type_id = pb.pus_getTcSubtype(pack)
            jsn["data"]["pck_sec_head"]["src_id"] = pb.pus_getTcSource(pack)

        jsn["data"]["pck_sec_head"]["msg_type_id"] = collections.OrderedDict()
        jsn["data"]["pck_sec_head"]["msg_type_id"]["service_type_id"] = srvc_type_id
        jsn["data"]["pck_sec_head"]["msg_type_id"]["msg_subtype_id"] = msg_type_id
        jsn["data"]["pck_sec_head"]["spare"] = 0

        jsn["data"]["user_data"] = {"src_data": {}, "spare": 0, "pack_error_ctrl": 0}

        if srvc_type_id == 1:  # If it's a request verification packet
            jsn["data"]["user_data"]["src_data"] = self.tm_1_x_data(pack)
        elif (srvc_type_id, msg_type_id) == (3, 25):
            jsn["data"]["user_data"]["src_data"] = self.tm_3_25_data(pack)
        elif (srvc_type_id, msg_type_id) == (8, 1):
            jsn["data"]["user_data"]["src_data"] = self.tc_8_1_data(pack)
        elif srvc_type_id == 12:
            jsn["data"]["user_data"]["src_data"] = self.tc_12_x_data(pack, msg_type_id)
        elif srvc_type_id == 19:
            if msg_type_id == 1:
                jsn["data"]["user_data"]["src_data"] = self.tc_19_1_data(pack)
            else:
                jsn["data"]["user_data"]["src_data"] = self.tc_19_2_4_5_data(pack)
        return jsn

    def json2packet(self, jsn):
        # Vamos a empezar parseando solos los campos de data
        type_ = jsn["primary_header"]["pck_id"]["pck_type"]
        if type_ == 0:  # TM
            tm_version = jsn["data"]["pck_sec_head"]["tm_packet_pus_version_number"]
            pb.pus_setTmPusVersion(pack, tm_version)

            time_ref = jsn["data"]["pck_sec_head"]["spacecraft_time"]
            pb.pus_setTmTimeReferenceStatus(pack, time_ref)

            srvc_type_id = jsn["data"]["pck_sec_head"]["msg_type_id"]["service_type_id"]
            pb.pus_setTmService(pack, srvc_type_id)

            msg_type_id = jsn["data"]["pck_sec_head"]["msg_type_id"]["msg_subtype_id"]
            pb.pus_setTmSubtype(pack, msg_type_id)

            msg_type_counter = jsn["data"]["pck_sec_head"]["msg_type_counter"]
            pb.pus_setTmMessageTypeCounter(pack, msg_type_counter)

            tm_dest = jsn["data"]["pck_sec_head"]["dst_id"]
            pb.pus_getTmDestination(pack, tm_dest)

            time = jsn["data"]["pck_sec_head"]["time"]  # Revisar, puede ser que esté en string
            pb.pus_setTmPacketTime(pack, time)
        else:
            srvc_type_id = jsn["data"]["pck_sec_head"]["msg_type_id"]["service_type_id"]
            pb.pus_setTcService(pack, srvc_type_id)

            msg_type_id = jsn["data"]["pck_sec_head"]["msg_type_id"]["msg_subtype_id"]
            pb.pus_setTcSubtype(pack, msg_type_id)

            tc_version = jsn["data"]["pck_sec_head"]["tc_packet_pus_version_number"]
            pb.pus_setTcPusVersion(pack, tc_version)
            ack_f_acceptance = jsn["data"]["pck_sec_head"]["ack_flags"]["ack_flag_acceptance"]
            ack_f_start = jsn["data"]["pck_sec_head"]["ack_flags"]["ack_flag_start"]
            ack_f_progress = jsn["data"]["pck_sec_head"]["ack_flags"]["ack_flag_progress"]
            ack_f_completion = jsn["data"]["pck_sec_head"]["ack_flags"]["ack_flag_completion"]
            pb.pusTcAckFlags(pack, ack_f_acceptance, ack_f_start, ack_f_progress, ack_f_completion)
            src_id = jsn["data"]["pck_sec_head"]["src_id"]
            pb.pus_setTcSource(pack, src_id)

        if srvc_type_id == 1:  # If it's a request verification packet
            jsn["data"]["user_data"]["src_data"] = self.tm_1_x_data(pack)
        elif (srvc_type_id, msg_type_id) == (3, 25):
            jsn["data"]["user_data"]["src_data"] = self.tm_3_25_data(pack)
        elif (srvc_type_id, msg_type_id) == (8, 1):
            jsn["data"]["user_data"]["src_data"] = self.tc_8_1_data(pack)
        elif srvc_type_id == 12:
            jsn["data"]["user_data"]["src_data"] = self.tc_12_x_data(pack, msg_type_id)
        elif srvc_type_id == 19:
            if msg_type_id == 1:
                jsn["data"]["user_data"]["src_data"] = self.tc_19_1_data(pack)
            else:
                jsn["data"]["user_data"]["src_data"] = self.tc_19_2_4_5_data(pack)
        return jsn

    @staticmethod
    def tm_1_x_data(packet):
        """
        This functions parses the st01 packet data field to json
        :param packet: The packet which data field we want to parse
        :return: A JSON object with all the parsed information
        """
        data = dict()
        data["request"] = dict()
        data["request"]["packet_version"] = pb.pus_tm_1_X_getReportPacketVersionNumber(packet)
        data["request"]["packet_type"] = pb.pus_tm_1_X_getReportPacketType(packet)
        data["request"]["sec_head_flag"] = pb.pus_tm_1_X_getReportSecondaryHeaderFlag(packet)
        data["request"]["apid"] = pb.pus_tm_1_X_getReportApid(packet)
        data["request"]["seq_flags"] = pb.pus_tm_1_X_getReportSequenceFlags(packet)
        data["request"]["seq_count"] = pb.pus_tm_1_X_getReportSequenceCount(packet)

        data["step"] = pb.pus_tm_1_X_getStep(packet)

        data["failure"] = dict()
        data["failure"]["code"] = pb.pus_tm_1_X_getFailureCode(packet)
        data["failure"]["info"] = dict()
        data["failure"]["info"]["subcode"] = pb.pus_getSt01FailureSubcode(packet)
        data["failure"]["info"]["data"] = pb.pus_getSt01FailureData(packet)
        data["failure"]["info"]["address"] = pb.pus_getSt01FailureAddress(packet)

        return data

    @staticmethod
    def tm_3_25_data(packet):
        data = dict()
        data["hk_param_report_id"] = pb.pus_tm_3_25_getReportId(packet)
        num_param = int()
        pb.pus_tm_3_25_getNumParameters(packet, num_param)
        for i in range(num_param):
            param = int()
            pb.pus_tm_3_25_getParameterValue(packet, i, param)
            data["param"+str(i+1)] = param
        return data

    @staticmethod
    def tm_5_x_data(packet):
        data = dict()
        event_id = int()
        pb.pus_tm_get_5_X_event_id(packet, event_id)
        data["event_id"] = event_id
        aux1 = int()
        pb.pus_tm_get_5_X_event_auxdata1(packet, aux1)
        aux2 = int()
        pb.pus_tm_get_5_X_event_auxdata2(packet, aux2)
        data["auxdata"] = {"data1": aux1, "data2": aux2}
        return data

    @staticmethod
    def tc_8_1_data(packet):
        data = dict()
        function_id = int()
        pb.pus_tc_8_1_getFunctionId(function_id, packet)
        data["function_id"] = function_id
        return data

    @staticmethod
    def tc_12_x_data(packet, msg_id):
        data = dict()

        if msg_id == 1 or msg_id == 2:
            pmon_id = int()
            pb.pus_tc_12_1_2_getPmonId(pmon_id, packet)
            data["pmon_id"] = pmon_id
        return data

    def tc_19_1_data(self, packet):
        data = dict()
        packet_reduced = pb.pusPacketReduced_t()
        pb.pus_tc_19_1_getAction(packet_reduced, packet)
        data_packet = pb.pusPacket_t()
        pb.pus_tc_19_X_createPacketFromPacketReduced(data_packet, packet_reduced)
        event_id = int()
        pb.pus_tc_19_X_getEventId(event_id, packet)
        data["event_id"] = event_id
        data["request"] = self.packet2json(data_packet)
        return data

    @staticmethod
    def tc_19_2_4_5_data(packet):
        data = dict()
        event_id = int()
        pb.pus_tc_19_X_getEventId(event_id, packet)
        data["event_id"] = event_id
        return data
