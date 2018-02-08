/* This file was generated automatically: DO NOT MODIFY IT ! */

#ifdef __unix__
    #include <stdlib.h>
    #include <stdio.h>
#else
    typedef unsigned size_t;
#endif

#include "console_vm_if.h"

#include "console.h"

#include "C_ASN1_Types.h"

void init_console()
{
    static int init = 0;

    if (!init) {
        init = 1;
        console_startup();
        extern void init_x86_partition_taste_api();
        init_x86_partition_taste_api();
    }
}

void console_trigger ()
{
    /* Call to User-defined function */
    console_PI_trigger ();

}
void console_tm (void *pmy_packet, size_t size_my_packet)
{
    /* Decoded input variable(s): developer can use them */
    static asn1SccPusPacket IN_packet;

#ifdef __unix__
    asn1SccPusPacket_Initialize(&IN_packet);
#endif

    /* Decode each input parameter */
    if (0 != Decode_NATIVE_PusPacket (&IN_packet, pmy_packet, size_my_packet)) {
        #ifdef __unix__
            printf("\nError Decoding PusPacket\n");
        #endif
        return;
    }

    /* Call to User-defined function */
    console_PI_tm (&IN_packet);

}
