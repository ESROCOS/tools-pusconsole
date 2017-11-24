# Source files
set(SOURCES
	pus_binding.cpp
) # Duda he de poner aqui 


# Define the PUS library
pybind11_add_module(esrocos_pusbinding  ${SOURCES})
include_directories(esrocos_pusbinding ../../pus/include)
include_directories(esrocos_pusbinding ../../pus/debug/asn1/generated)
include_directories(esrocos_pusbinding ../../pus/debug/asn1/generated/asn1)
include_directories(esrocos_pusbinding ../../pus/debug/src)

set_target_properties(esrocos_pusbinding PROPERTIES LINKER_LANGUAGE CXX)
target_link_libraries(esrocos_pusbinding PRIVATE ../../pus/debug/src/libesrocos_pus.a
                                                   ../../pus/debug/asn1/libesrocos_pus_asn1.a
                                                   ../../pus/debug/asn1/libesrocos_pus_asn1common.a)



