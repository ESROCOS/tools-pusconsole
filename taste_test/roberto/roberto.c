/* User code: This file will not be overwritten by TASTE. */

#include <stdio.h>
#include "roberto.h"
#include "pus_packet.h"

void roberto_startup()
{
    /* Write your initialization code here,
       but do not make any call to a required interface. */
       printf("Hello from startup roverTo! \n");
}

void roberto_PI_tc(const asn1SccPusPacket *IN_packet)
{
    /* Write your code here! */
    printf("Paquete recibido en roverTO\n");
    roberto_RI_tm(IN_packet);
}

void roberto_PI_trigger()
{
    /*pusPacket_t tm; 
    pus_tm_20_2_createParameterValueReport(&tm, 25, 15, 2, 1, 2);
    printf("Enviado!\n");
    roberto_RI_tm(&tm);*/
}
