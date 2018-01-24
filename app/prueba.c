#include <Python.h>
#include <stdlib.h>
#include <pthread.h>

#include "pus_packet.h"
#include "pus_st17_packets.h"
#include "pus_threads.h"
#include "pus_notify.h"

void *myThreadFun(void *vargp)
{
  pusPacket_t packet;
  pusMutex_t mutex;
  while(1)
  {
    sleep(5);
    pus_tm_17_2_createConnectionTestReport(&packet, 25, 25, 25);
    pus_notify_setPacket(&packet);
    pus_notify_getMutex(&mutex);
    pus_mutexUnlockOk(&mutex);
    printf("Enviado\n");
 }
}

int main(int argc, char *argv[])
{
    pusMutex_t mutex;
    pus_notify_getMutex(&mutex);
    printf("Bool: %d\n", pus_mutexInitOk(&mutex));
    printf("Bool 2: %d\n", pus_mutexLockOk(&mutex));
    //printf("referencia: %p\n", mutex);
    pthread_t tid;
    pthread_create(&tid, NULL, myThreadFun, NULL);
    sleep(1);
    Py_Initialize();
    PyRun_SimpleString("import sys\n");
    PyRun_SimpleString("sys.path.insert(0, '.')\n");
    PyRun_SimpleString("import Main\n");
    PyRun_SimpleString("Main.main()\n");
    Py_Finalize();
    pthread_join(tid, NULL);
    exit(0);
}
