#include<pybind11/pybind11.h>
#include "/home/esrocos/esrocos-ws-pus/pus/include/pus_packet.h"
#include "/home/esrocos/esrocos-ws-pus/pus/include/pus_error.h"
#include "/home/esrocos/esrocos-ws-pus/pus/include/pus_types.h"

namespace py = pybind11;

PYBIND11_MODULE(pus_packet, m) {
	m.doc() = "pus_packet binding"
    py::enum_<pusError_t>(m, "pusError_t")
        .value("PUS_NO_ERROR",pusError_t::PUS_NO_ERROR)
        .value("PUS_ERROR_NULLPTR",pusError_t::PUS_ERROR_NULLPTR)
        .value("PUS_ERROR_COUNT_WRAP",pusError_t::PUS_ERROR_COUNT_WRAP)
        .value("PUS_ERROR_HEADER_MISMATCH",pusError_t::PUS_ERROR_HEADER_MISMATCH)
        .value("PUS_ERROR_PACKET_TYPE",pusError_t::PUS_ERROR_PACKET_TYPE)
        .value("PUS_ERROR_NOT_TM",pusError_t::PUS_ERROR_NOT_TM)
        .value("PUS_ERROR_NOT_TC",pusError_t::PUS_ERROR_NOT_TC)
        .value("PUS_ERROR_SYSTEM_TIME",pusError_t::PUS_ERROR_SYSTEM_TIME)
        .value("PUS_ERROR_LIMIT",pusError_t::PUS_ERROR_LIMIT)
        .value("PUS_ERROR_UNEXPECTED_PACKET_VERSION",pusError_t::PUS_ERROR_UNEXPECTED_PACKET_VERSION)
        .value("PUS_ERROR_UNEXPECTED_SEQUENCE_FLAGS",pusError_t::PUS_ERROR_UNEXPECTED_SEQUENCE_FLAGS)
        .value("PUS_ERROR_UNEXPECTED_PUS_VERSION",pusError_t::PUS_ERROR_UNEXPECTED_PUS_VERSION)
        .value("PUS_ERROR_NOT_IMPLEMENTED",pusError_t::PUS_ERROR_NOT_IMPLEMENTED)
        .value("PUS_ERROR_TM_KIND",pusError_t::PUS_ERROR_TM_KIND)
        .value("PUS_ERROR_TM_SERVICE",pusError_t::PUS_ERROR_TM_SERVICE)
        .value("PUS_ERROR_TM_SUBTYPE",pusError_t::PUS_ERROR_TM_SUBTYPE)
        .value("PUS_ERROR_TC_KIND",pusError_t::PUS_ERROR_TC_KIND)
        .value("PUS_ERROR_TC_SERVICE",pusError_t::PUS_ERROR_TC_SERVICE)
        .value("PUS_ERROR_TC_SUBTYPE",pusError_t::PUS_ERROR_TC_SUBTYPE)
        .value("PUS_ERROR_SUBTYPE_MISMATCH",pusError_t::PUS_ERROR_SUBTYPE_MISMATCH)
        .value("PUS_ERROR_THREADS",pusError_t::PUS_ERROR_THREADS)
        .value("PUS_ERROR_BEFORE",pusError_t::PUS_ERROR_BEFORE)
        .value("PUS_ERROR_ALREADY_INITIALIZED",pusError_t::PUS_ERROR_ALREADY_INITIALIZED)
        .value("PUS_ERROR_NOT_INITIALIZED",pusError_t::PUS_ERROR_NOT_INITIALIZED)
        .value("PUS_ERROR_INITIALIZATION",pusError_t::PUS_ERROR_INITIALIZATION)
        .value("PUS_ERROR_FINALIZATION",pusError_t::PUS_ERROR_FINALIZATION)
        .value("PUS_ERROR_INVALID_ID",pusError_t::PUS_ERROR_INVALID_ID)
        .value("PUS_ERROR_INVALID_TYPE",pusError_t::PUS_ERROR_INVALID_TYPE)
        .value("PUS_ERROR_THREADS_DISABLED",pusError_t::PUS_ERROR_THREADS_DISABLED)
        .value("PUS_ERROR_REPORT_ID_UNKNOWN",pusError_t::PUS_ERROR_REPORT_ID_UNKNOWN)
        .value("PUS_ERROR_REPORT_LENGTH",pusError_t::PUS_ERROR_REPORT_LENGTH)
        .value("PUS_LAST_ERROR",pusError_t::PUS_LAST_ERROR)
        .export_values();

	py::class_<pus_packet_t>(m, pus_packet_t)
		.def("pus_getPacketVersion", &pus_getPacketVersion, "Binding for pus_getPacketVersion"); //~
		.def("pus_setPacketVersion", &pus_setPacketVersion, "Binding for pus_setPacketVersion"); //~
		.def("pus_getPacketType", &pus_getPacketType, "Binding for pus_getPacketType"); //~
		.def("pus_setPacketType", &pus_setPacketType, "Binding for pus_setPacketType"); //~
		.def("pus_getApid", &pus_getApid, "Binding for pus_getApid"); //b ojo
		.def("pus_setApid", &pus_setApid, "Binding for pus_setApid"); //b ojo
		.def("pus_getSecondaryHeaderFlag", &pus_getSecondaryHeaderFlag, "Binding for pus_getSecondaryHeaderFlag"); //b
		.def("pus_setSecondaryHeaderFlag", &pus_setSecondaryHeaderFlag, "Binding for pus_setSecondaryHeaderFlag"); //b
		.def("pus_getSequenceFlags", &pus_getSequenceFlags, "Binding for pus_getSequenceFlags"); //~
		.def("pus_setSequenceFlags", &pus_setSequenceFlags, "Binding for pus_setSequenceFlags"); //~
		.def("pus_getSequenceCount", &pus_getSequenceCount, "Binding for pus_getSequenceCount"); //b ojo
		.def("pus_setSequenceCount", &pus_setSequenceCount, "Binding for pus_setSequenceCount"); //b ojo
		.def("pus_getPacketDataLength", &pus_getPacketDataLength, "Binding for pus_getPacketDataLength"); //b
		.def("pus_setPacketDataLength", &pus_setPacketDataLength, "Binding for pus_setPacketDataLength"); //b
		.def("pus_setPacketDataNone", &pus_setPacketDataNone, "Binding for pus_setPacketDataNone"); //b
		.def("pus_getTmPusVersion", &pus_getTmPusVersion, "Binding for pus_getTmPusVersion"); //~
		.def("pus_setTmPusVersion", &pus_setTmPusVersion, "Binding for pus_setTmPusVersion"); //~
		.def("pus_getTcPusVersion", &pus_getTcPusVersion, "Binding for pus_getTcPusVersion"); //~
		.def("pus_setTcPusVersion", &pus_setTcPusVersion, "Binding for pus_setTcPusVersion"); //~
		.def("pus_getTmService", &pus_getTmService, "Binding for pus_getTmService"); //b ojo -
		.def("pus_setTmService", &pus_setTmService, "Binding for pus_setTmService"); //b ojo -
		.def("pus_getTmSubtype", &pus_getTmSubtype, "Binding for pus_getTmSubtype"); //b ojo -
		.def("pus_setTmSubtype", &pus_setTmSubtype, "Binding for pus_setTmSubtype"); //b ojo -
		.def("pus_getTcService", &pus_getTcService, "Binding for pus_getTcService"); //b ojo -
		.def("pus_setTcService", &pus_setTcService, "Binding for pus_setTcService"); //b ojo -
		.def("pus_getTcSubtype", &pus_getTcSubtype, "Binding for pus_getTcSubtype"); //b ojo -
		.def("pus_setTcSubtype", &pus_setTcSubtype, "Binding for pus_setTcSubtype"); //b ojo -
		.def("pus_getTmTimeReferenceStatus", &pus_getTmTimeReferenceStatus, "Binding for pus_getTmTimeReferenceStatus"); //b ojo
		.def("pus_setTmTimeReferenceStatus", &pus_setTmTimeReferenceStatus, "Binding for pus_setTmTimeReferenceStatus"); //b ojo
		.def("pus_getTmMessageTypeCounter", &pus_getTmMessageTypeCounter, "Binding for pus_getTmMessageTypeCounter"); //b ojo
		.def("pus_setTmMessageTypeCounter", &pus_setTmMessageTypeCounter, "Binding for pus_setTmMessageTypeCounter"); //b ojo
		.def("pus_getTmDestination", &pus_getTmDestination, "Binding for pus_getTmDestination"); //b ojo
		.def("pus_setTmDestination", &pus_setTmDestination, "Binding for pus_setTmDestination"); //b ojo
		.def("pus_getTcSource", &pus_getTcSource, "Binding for pus_getTcSource"); //b ojo
		.def("pus_setTcSource", &pus_setTcSource, "Binding for pus_setTcSource"); //b ojo
		.def("pus_getTmPacketTime", &pus_getTmPacketTime, "Binding for pus_getTmPacketTime"); //~ -
		.def("pus_setTmPacketTime", &pus_setTmPacketTime, "Binding for pus_setTmPacketTime"); //~ -
		.def("pus_setTmPacketTimeNow", &pus_setTmPacketTimeNow, "Binding for pus_setTmPacketTimeNow"); //b
		.def("pus_getTcAckFlagAcceptance", &pus_getTcAckFlagAcceptance, "Binding for pus_getTcAckFlagAcceptance"); //b
		.def("pus_getTcAckFlagStart", &pus_getTcAckFlagStart, "Binding for pus_getTcAckFlagStart"); //b
		.def("pus_getTcAckFlagProgress", &pus_getTcAckFlagProgress, "Binding for pus_getTcAckFlagProgress"); //b
		.def("pus_getTcAckFlagCompletion", &pus_getTcAckFlagCompletion, "Binding for pus_getTcAckFlagCompletion"); //b
		.def("pus_setTcAckFlags", &pus_setTcAckFlags, "Binding for pus_setTcAckFlags"); //b
		.def("pus_getPacketDataKind", &pus_getPacketDataKind, "Binding for pus_getPacketDataKind"); //b ?
		.def("pus_setPacketDataKind", &pus_setPacketDataKind, "Binding for pus_setPacketDataKind"); //b ?
		.def("pus_getTmDataKind", &pus_getTmDataKind, "Binding for pus_getTmDataKind"); //b ?
		.def("pus_setTmDataKind", &pus_setTmDataKind, "Binding for pus_setTmDataKind"); //b ? -
		.def("pus_getTmNoHeaderDataKind", &pus_getTmNoHeaderDataKind, "Binding for pus_getTmNoHeaderDataKind"); //b
		.def("pus_setTmNoHeaderDataKind", &pus_setTmNoHeaderDataKind, "Binding for pus_setTmNoHeaderDataKind"); //b
		.def("pus_incrementSequenceCount", &pus_incrementSequenceCount, "Binding for pus_incrementSequenceCount"); //b
		.def("pus_setPacketTimeNow", &pus_setPacketTimeNow, "Binding for pus_setPacketTimeNow"); //b
		.def("pus_setPacketDefaults", &pus_setPacketDefaults, "Binding for pus_setPacketDefaults"); //~ v b
		.def("pus_initTmPacket", &pus_initTmPacket, "Binding for pus_initTmPacket"); //~
		.def("pus_initTcPacket", &pus_initTcPacket, "Binding for pus_initTcPacket"); //~
		.def("pus_initTmPacketNoHeader", &pus_initTmPacketNoHeader, "Binding for pus_initTmPacketNoHeader"); //~
		.def("pus_initTcPacketNoHeader", &pus_initTcPacketNoHeader, "Binding for pus_initTcPacketNoHeader"); //~
		.def("pus_verifyCcsdsHeaderDefaults", &pus_verifyCcsdsHeaderDefaults, "Binding for pus_verifyCcsdsHeaderDefaults"); //~
		.def("pus_verifyPacketDataKind", &pus_verifyPacketDataKind, "Binding for pus_verifyPacketDataKind"); //~
		.def("pus_verifyTmSecondaryHeaderDefaults", &pus_verifyTmSecondaryHeaderDefaults, "Binding for pus_verifyTmSecondaryHeaderDefaults"); //~
		.def("pus_checkTcSecondaryHeaderDefaults", &pus_checkTcSecondaryHeaderDefaults, "Binding for pus_checkTcSecondaryHeaderDefaults"); //~
		.def("pus_verifyTmHeaderDefaults", &pus_verifyTmHeaderDefaults, "Binding for pus_verifyTmHeaderDefaults"); //~
		.def("pus_verifyTcHeaderDefaults", &pus_verifyTcHeaderDefaults, "Binding for pus_verifyTcHeaderDefaults"); //~
		.def("pus_expectTm", &pus_expectTm, "Binding for pus_expectTm"); //~
		.def("pus_expectTmHeader", &pus_expectTmHeader, "Binding for pus_expectTmHeader"); //~
		.def("pus_expectTmNoHeader", &pus_expectTmNoHeader, "Binding for pus_expectTmNoHeader"); //~
		.def("pus_expectTc", &pus_expectTc, "Binding for pus_expectTc"); //~
		.def("pus_expectTcHeader", &pus_expectTcHeader, "Binding for pus_expectTcHeader");  //~
		.def("pus_expectTcNoHeader", &pus_expectTcNoHeader, "Binding for pus_expectTcNoHeader"); //~
}

