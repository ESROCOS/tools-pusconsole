/* This file was generated automatically: DO NOT MODIFY IT ! */

#ifndef roberto_POLYORB_INTERFACE
#define roberto_POLYORB_INTERFACE
#include <stddef.h>

#include "types.h"
#include "deployment.h"
#include "po_hi_transport.h"
#include "../../x86_partition_taste_api/x86_partition_taste_api_polyorb_interface.h"
#include "../../vt_roberto_tc/vt_roberto_tc_polyorb_interface.h"
#include "../../vt_roberto_trigger/vt_roberto_trigger_polyorb_interface.h"
/*----------------------------------------------------
-- Protected Provided Interface "tc"
----------------------------------------------------*/
void sync_roberto_tc(void *, size_t);

/*----------------------------------------------------
-- Protected Provided Interface "trigger"
----------------------------------------------------*/
void sync_roberto_trigger();

/* ------------------------------------------------------
--  Asynchronous Required Interface "tm"
------------------------------------------------------ */
void vm_async_roberto_tm(void *packet, size_t packet_len);
/* ------------------------------------------------------
--  Synchronous Required Interface "check_queue"
------------------------------------------------------ */
void vm_roberto_check_queue(void *, size_t *);
#endif
