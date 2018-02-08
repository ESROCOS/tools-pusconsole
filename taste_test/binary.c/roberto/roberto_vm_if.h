/* This file was generated automatically: DO NOT MODIFY IT ! */

#ifndef VM_IF_roberto
#define VM_IF_roberto

#ifdef __cplusplus
extern "C" {
#endif

#include "C_ASN1_Types.h"

/*
 * Function initialization:
 * Calls all dependent user (or GUI) startup code - including sychronous RI
*/
void init_roberto();

void roberto_tc (void *pmy_packet, size_t size_my_packet);
extern void roberto_PI_tc (const asn1SccPusPacket *);
void roberto_trigger ();
extern void roberto_PI_trigger ();
#ifdef __cplusplus
}
#endif

#endif
