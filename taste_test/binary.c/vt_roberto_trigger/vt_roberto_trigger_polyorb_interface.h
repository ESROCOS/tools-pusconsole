/* This file was generated automatically: DO NOT MODIFY IT ! */

#ifndef vt_roberto_trigger_POLYORB_INTERFACE
#define vt_roberto_trigger_POLYORB_INTERFACE
#include <stddef.h>

#include "types.h"
#include "deployment.h"
#include "po_hi_transport.h"
#include "../../roberto/roberto_polyorb_interface.h"
#include "../../x86_partition_taste_api/x86_partition_taste_api_polyorb_interface.h"
/*----------------------------------------------------
-- Asynchronous Provided Interface "artificial_trigger"
----------------------------------------------------*/
void po_hi_c_vt_roberto_trigger_artificial_trigger(__po_hi_task_id);

/* ------------------------------------------------------
--  Synchronous Required Interface "trigger"
------------------------------------------------------ */
void vm_vt_roberto_trigger_trigger();
/* ------------------------------------------------------
--  Asynchronous Required Interface "tm_vt"
------------------------------------------------------ */
void vm_async_vt_roberto_trigger_tm_vt(void *packet, size_t packet_len);
/* ------------------------------------------------------
--  Synchronous Required Interface "check_queue_vt"
------------------------------------------------------ */
void vm_vt_roberto_trigger_check_queue_vt(void *, size_t *);
#endif
