#include <Python.h>
#include <stdlib.h>
#include <pthread.h>

#include "pus_packet.h"
#include "pus_st17_packets.h"
#include "pus_threads.h"
#include "pus_notify.h"

//pusPacket_t receivedPacket;
//pusMutex_t receivedMutex;

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

void *myThreadFun(void *vargp)
{
    pusPacket_t packet, *aux;
    pusMutex_t mutex;
    int i = 0;
    while(i < 30)
    {
        sleep(2);
        pus_tm_17_2_createConnectionTestReport(&packet, 25, 25, 25); //CREAMOS PAQUETE 17
        pus_notify_setPacket(&packet); //PONEMOS EL PAQUETE EN LA VARIABLE GLOBAL
        pus_notify_getPacket(aux);
        printf("Paquete global: %p\n", aux);
        pus_notify_getMutex(&mutex); //OBTENEMOS EL MUTEX GLOBAL
        pus_mutexUnlockOk(&mutex); //LO ABRIMOS
        printf("Enviado\n");
        i++;
    }
}

int main(int argc, char *argv[])
{
    //INICIALIZAMOS MUTEX Y LO BLOQUEAMOS
    pusMutex_t mutex;
    pus_notify_getMutex(&mutex);
    printf("Bool: %d\n", pus_mutexInitOk(&mutex));
    printf("Bool 2: %d\n", pus_mutexLockOk(&mutex));

    // LANZAMOS HILO QUE ENVIA TELEMETRIAS 17
    pthread_t tid;
    pthread_create(&tid, NULL, myThreadFun, NULL);
    sleep(5);

    // LANZAMOS APP
    Py_Initialize();
    PyRun_SimpleString("import sys\n");
    PyRun_SimpleString("sys.path.insert(0, '.')\n");
    PyRun_SimpleString("import Main\n");
    PyRun_SimpleString("Main.main()\n");
    Py_Finalize();

    //FINALIZAMOS
    pthread_join(tid, NULL);
    exit(0);
}
