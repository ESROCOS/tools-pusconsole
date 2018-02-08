/* This file was generated automatically: DO NOT MODIFY IT ! */

#ifndef vt_console_tm_POLYORB_INTERFACE
#define vt_console_tm_POLYORB_INTERFACE
#include <stddef.h>

#include "types.h"
#include "deployment.h"
#include "po_hi_transport.h"
#include "../../console/console_polyorb_interface.h"
#include "../../x86_partition_taste_api/x86_partition_taste_api_polyorb_interface.h"
/*----------------------------------------------------
-- Asynchronous Provided Interface "artificial_tm"
----------------------------------------------------*/
void po_hi_c_vt_console_tm_artificial_tm(__po_hi_task_id, dataview__puspacket_buffer_impl);

/* ------------------------------------------------------
--  Synchronous Required Interface "tm"
------------------------------------------------------ */
void vm_vt_console_tm_tm(void *packet, size_t packet_len);
/* ------------------------------------------------------
--  Asynchronous Required Interface "tc_vt"
------------------------------------------------------ */
void vm_async_vt_console_tm_tc_vt(void *packet, size_t packet_len);
/* ------------------------------------------------------
--  Synchronous Required Interface "check_queue_vt"
------------------------------------------------------ */
void vm_vt_console_tm_check_queue_vt(void *, size_t *);
#endif
