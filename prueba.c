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
    pusPacket_t packet;
    int i = 0;
    while(i < 3)
    {
        sleep(2);
        pus_tm_17_2_createConnectionTestReport(&packet, 25, 25, 25); //CREAMOS PAQUETE 17
        write_packet(&packet);
        i++;
    }
}

int main(int argc, char *argv[])
{
    init_mutex_cond();
    // LANZAMOS HILO QUE ENVIA TELEMETRIAS 17
    pthread_t tid;
    pthread_create(&tid, NULL, myThreadFun, NULL);

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
