#include <Python.h>
#include <stdlib.h>
#include <pthread.h>

#include "pus_packet.h"
#include "pus_apid.h"
#include "pus_time.h"
#include "pus_st01_packets.h"
#include "pus_st03_packets.h"
#include "pus_st05_packets.h"
#include "pus_st08_packets.h"
#include "pus_st09_packets.h"
#include "pus_st11_packets.h"
#include "pus_st12_packets.h"
#include "pus_st17_packets.h"
#include "pus_st19_packets.h"
#include "pus_st20_packets.h"
#include "pus_events.h"
#include "pus_error.h"
#include "pus_threads.h"
#include "pus_notify.h"

//pusPacket_t receivedPacket;
//pusMutex_t receivedMutex;

extern pusError_t example_function()
{
	printf("  - Hello world! -  ");
	return PUS_NO_ERROR;
}

extern pusError_t example_function2()
{
	printf("Hello from function2\n");
	return PUS_NO_ERROR;
}

extern pusError_t example_function3()
{
	printf("Hello from function3\n");
	return PUS_NO_ERROR;
}

int ret_packets(pusPacket_t *tm, int i)
{
	pusPacket_t tc;
	//pusTime_t tv, now;
	pusApidInfo_t apid;

	pus_initApidInfo(&apid, 33, NULL);

	// Test TC
	pus_initTcPacket(&tc);
	pus_setTcSource(&tc, 11);
	pus_setSequenceCount(&tc, 22);

	// Test failures
	pusSt01FailureInfo_t info1, info2;
	pus_setSt01FailureInfo(&info1, 101, 102, 103);

	// TM[1,1]
	if (i==0) pus_tm_1_1_createAcceptanceReportSuccess(tm, apid.apid, i, &tc);


	// TM[1,2]
	else if (i==1) pus_tm_1_2_createAcceptanceReportFailure(tm, apid.apid, i, &tc, pus_ST01_ERROR_SERVICE_UNAVAILABLE, &info1);


	// TM[1,3]
	else if (i==2) pus_tm_1_3_createStartReportSuccess(tm, apid.apid, i, &tc);

	// TM[1,4]
	else if (i==3) pus_tm_1_4_createStartReportFailure(tm, apid.apid, i, &tc, pus_ST01_ERROR_WRONG_FORMAT, NULL);


	// TM[1,5]
	else if (i==4) pus_tm_1_5_createProgressReportSuccess(tm, apid.apid, i, &tc, 71);

	// TM[1,6]
	else if (i==5) pus_tm_1_6_createProgressReportFailure(tm, apid.apid, i, &tc, 72, pus_ST01_ERROR_SUBTYPE_UNAVAILABLE, NULL);


	// TM[1,7]
	else if (i==6) pus_tm_1_7_createCompletionReportSuccess(tm, apid.apid, i, &tc);


	// TM[1,8]
	else if (i==7) pus_tm_1_8_createCompletionReportFailure(tm, apid.apid, i, &tc, pus_ST01_ERROR_WRONG_FORMAT, NULL);

	else if (i == 8)
	{
		pus_tc_11_1_createEnableTimeBasedSchedule(tm, apid.apid, i);
	}
	else if (i == 9)
	{
		pus_tm_20_2_createParameterValueReport(tm, apid.apid, i, apid.apid, 1, 2);
	}

	return 0;


	// TC without header
	//CU_ASSERT_EQUAL(PUS_NO_ERROR, pus_initTcPacketNoHeader(&tc));
	//pus_tm_1_1_createAcceptanceReportSuccess(&tm, apid.apid, pus_getNextPacketCount(&apid), &tc);
	//CU_ASSERT_FALSE(pus_tm_1_X_getSecondaryHeaderFlag(&tm));

}

void *myThreadFun(void *vargp)
{
    pusPacket_t packet;
    int i = 0;
    while(i < 10)
    {
        printf("i: %d\n", i);
        sleep(1);
        ret_packets(&packet, i);
        pus_notify_writePacket(&packet);
        i++;
    }
}

int main(int argc, char *argv[])
{
    pus_notify_initialize();
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

    pus_notify_finalize();

    //FINALIZAMOS
    pthread_join(tid, NULL);
    exit(0);
}
