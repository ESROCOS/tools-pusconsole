import json
import pybind11
from PySide import QtCore, QtGui
from Model import App
import sys
sys.path.insert(0, '../../pus/debug/pylib')
import pusbinding as pb

def convert_json(pack):
    jsn = {"primary_header": {}, "data": {}}
    jsn["primary_header"]["pck_version"] = pb.pus_getPacketVersion(pack)
    jsn["primary_header"]["pck_id"] = {}
    type = jsn["primary_header"]["pck_id"]["pck_type"] = pb.pus_getPacketType(pack)
    jsn["primary_header"]["pck_id"]["sec_head_flg"] = pb.pus_getSecondaryHeaderFlag(pack)
    jsn["primary_header"]["pck_id"]["apid"] = pb.pus_getApid(pack)
    jsn["primary_header"]["pck_seq_ctrl"] = {}
    jsn["primary_header"]["pck_seq_ctrl"]["pck_seq_flg"] = pb.pus_getSequenceFlags(pack)
    jsn["primary_header"]["pck_seq_ctrl"]["pck_seq"] = pb.pus_getSequenceCount(pack)
    jsn["primary_header"]["pck_data_len"] = pb.pus_getPacketDataLength(pack)
    jsn["primary_header"]["data"] = {"pck_sec_head": {}, "user_data": {}}
    if type == 0: #TM
        jsn["primary_header"]["data"]["pck_sec_head"]["tm_packet_pus_version_number"] = pb.pus_getTmPusVersion(pack)
        jsn["primary_header"]["data"]["pck_sec_head"]["spacecraft_time"] = pb.pus_getTmTimeReferenceStatus(pack)
        srvc_type_id = pb.pus_getTmService(pack)
        msg_type_id = pb.pus_getTmSubtype(pack)
        jsn["primary_header"]["data"]["pck_sec_head"]["msg_type_counter"] = pb.pus_getTmMessageTypeCounter(pack)
        jsn["primary_header"]["data"]["pck_sec_head"]["dst_id"] = pb.pus_getTmDestination(pack)
        jsn["primary_header"]["data"]["pck_sec_head"]["time"] = pb.pus_getTmPacketTime(pack)
    else:
        jsn["primary_header"]["data"]["pck_sec_head"]["tc_packet_pus_version_number"] = pb.pus_getTcPusVersion(pack)
        jsn["primary_header"]["data"]["pck_sec_head"]["ack_flags"]["ack_flag_acceptance"] = pb.pus_getTcAckFlagAcceptance(pack)
        jsn["primary_header"]["data"]["pck_sec_head"]["ack_flags"]["ack_flag_start"] = pb.pus_getTcAckFlagStart(pack)
        jsn["primary_header"]["data"]["pck_sec_head"]["ack_flags"]["ack_flag_progress"] = pb.pus_getTcAckFlagProgress(pack)
        jsn["primary_header"]["data"]["pck_sec_head"]["ack_flags"]["ack_flag_completion"] = pb.pus_getTcAckFlagCompletion(pack)
        srvc_type_id = pb.pus_getTcService(pack)
        msg_type_id = pb.pus_getTcSubtype(pack)
        jsn["primary_header"]["data"]["pck_sec_head"]["source_id"] = pb.pus_getTcSource(pack)

    jsn["primary_header"]["data"]["pck_sec_head"]["msg_type_id"]["service_type_id"] = srvc_type_id
    jsn["primary_header"]["data"]["pck_sec_head"]["msg_type_id"]["msg_subtype_id"] = msg_type_id
    jsn["primary_header"]["data"]["pck_sec_head"]["spare"] = 0
    # Esto es solo para el paquete 17 REVISAR
    jsn["primary_header"]["data"]["user_data"] = {"src_data": {}, "spare": 0, "pack_error_ctrl": 0}
    return json.dumps(jsn)

gui = QtGui.QApplication(sys.argv)
app = App()
args = sys.argv

if len(args) > 1:
    if args[1] == "-test":
        apid = pb.pusApidInfo_t()
        packet = pb.pusPacket_t()
        pb.pus_initApidInfo_(apid, 1)
        pb.pus_tm_17_2_createConnectionTestRequest(packet, apid)
        print(packet)



sys.exit(gui.exec_())

