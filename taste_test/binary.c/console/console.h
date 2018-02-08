/* This file was generated automatically: DO NOT MODIFY IT ! */

/* Declaration of the functions that have to be provided by the user */

#ifndef __USER_CODE_H_console__
#define __USER_CODE_H_console__

#include "C_ASN1_Types.h"

#ifdef __cplusplus
extern "C" {
#endif

void console_startup();

void console_PI_trigger();

void console_PI_tm(const asn1SccPusPacket *);

extern void console_RI_tc(const asn1SccPusPacket *);

#ifdef __cplusplus
}
#endif


#endif
