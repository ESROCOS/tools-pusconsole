/* This file was generated automatically: DO NOT MODIFY IT ! */

#ifndef VM_IF_console
#define VM_IF_console

#ifdef __cplusplus
extern "C" {
#endif

#include "C_ASN1_Types.h"

/*
 * Function initialization:
 * Calls all dependent user (or GUI) startup code - including sychronous RI
*/
void init_console();

void console_trigger ();
extern void console_PI_trigger ();
void console_tm (void *pmy_packet, size_t size_my_packet);
extern void console_PI_tm (const asn1SccPusPacket *);
#ifdef __cplusplus
}
#endif

#endif
