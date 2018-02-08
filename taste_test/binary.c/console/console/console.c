/* User code: This file will not be overwritten by TASTE. */

#include "console.h"
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <Python.h>

#include "pus_error.h"
#include "pus_notify.h"
#include "pus_packet.h"

pusError_t example_function()
{
	printf("  - Hello world! -  ");
	return PUS_NO_ERROR;
}

pusError_t example_function2()
{
	printf("Hello from function2\n");
	return PUS_NO_ERROR;
}

pusError_t example_function3()
{
	printf("Hello from function3\n");
	return PUS_NO_ERROR;
}

void *myThreadFun(void* arg)
{
    Py_Initialize();
    PyRun_SimpleString("import sys\n");
    PyRun_SimpleString("sys.path.insert(0, '/home/esrocos/esrocos-ws-pus/tools-pusconsole/app')\n");
    PyRun_SimpleString("import Main\n");
    PyRun_SimpleString("Main.main()\n");
    Py_Finalize();
}

void console_startup()
{
    /* Write your initialization code here,
       but do not make any call to a required interface. */
    printf("%d\n", pus_notify_initialize()); 

    //init thread
    pthread_t tid;
    pthread_create(&tid, NULL, myThreadFun, NULL);
    printf("Startup completed!\n");
}

void console_PI_trigger()
{
    pusPacket_t packet;
    while(PUS_NO_ERROR == pus_notify_readTc(&packet))
        console_RI_tc(&packet);    
}

void console_PI_tm(const asn1SccPusPacket *IN_packet)
{
    /* Write your code here! */
    pus_notify_writeTm(IN_packet);
    printf("Recibido\n");    
}

