/* This file was generated automatically: DO NOT MODIFY IT ! */

#ifdef __unix__
    #include <stdlib.h>
    #include <stdio.h>
#else
    typedef unsigned size_t;
#endif

#include "roberto_vm_if.h"

#include "roberto.h"

#include "C_ASN1_Types.h"

void init_roberto()
{
    static int init = 0;

    if (!init) {
        init = 1;
        roberto_startup();
        extern void init_x86_partition_taste_api();
        init_x86_partition_taste_api();
    }
}

void roberto_tc (void *pmy_packet, size_t size_my_packet)
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
    roberto_PI_tc (&IN_packet);

}
void roberto_trigger ()
{
    /* Call to User-defined function */
    roberto_PI_trigger ();

}
