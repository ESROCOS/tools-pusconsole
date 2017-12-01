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
        type = jsn["primary_header"]["pck_id"]["pck_type"] = pb.pus_getPacketType(pack)
        jsn["primary_header"]["pck_id"]["sec_head_flg"] = pb.pus_getSecondaryHeaderFlag(pack)
        jsn["primary_header"]["pck_id"]["apid"] = pb.pus_getApid(pack)
        jsn["primary_header"]["pck_seq_ctrl"] = collections.OrderedDict()
        jsn["primary_header"]["pck_seq_ctrl"]["pck_seq_flg"] = pb.pus_getSequenceFlags(pack)
        jsn["primary_header"]["pck_seq_ctrl"]["pck_seq"] = pb.pus_getSequenceCount(pack)
        jsn["primary_header"]["pck_data_len"] = pb.pus_getPacketDataLength(pack)
        jsn["data"] = collections.OrderedDict()
        jsn["data"]["pck_sec_head"] = collections.OrderedDict()
        jsn["data"]["user_data"] = collections.OrderedDict()
        if type == 0:  # TM
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
            jsn["data"]["pck_sec_head"]["source_id"] = pb.pus_getTcSource(pack)

        jsn["data"]["pck_sec_head"]["msg_type_id"] = collections.OrderedDict()
        jsn["data"]["pck_sec_head"]["msg_type_id"]["service_type_id"] = srvc_type_id
        jsn["data"]["pck_sec_head"]["msg_type_id"]["msg_subtype_id"] = msg_type_id
        jsn["data"]["pck_sec_head"]["spare"] = 0
        # Esto es solo para el paquete 17 REVISAR
        jsn["data"]["user_data"] = {"src_data": {}, "spare": 0, "pack_error_ctrl": 0}
        return jsn

    def json2packet(self, json_data):
        # Ver si en un futuro tengo que anadir los campos de la primary header
        pass
