/* This file was generated automatically: DO NOT MODIFY IT ! */

#ifndef console_POLYORB_INTERFACE
#define console_POLYORB_INTERFACE
#include <stddef.h>

#include "types.h"
#include "deployment.h"
#include "po_hi_transport.h"
#include "../../x86_partition_taste_api/x86_partition_taste_api_polyorb_interface.h"
#include "../../vt_console_trigger/vt_console_trigger_polyorb_interface.h"
#include "../../vt_console_tm/vt_console_tm_polyorb_interface.h"
/*----------------------------------------------------
-- Protected Provided Interface "trigger"
----------------------------------------------------*/
void sync_console_trigger();

/*----------------------------------------------------
-- Protected Provided Interface "tm"
----------------------------------------------------*/
void sync_console_tm(void *, size_t);

/* ------------------------------------------------------
--  Asynchronous Required Interface "tc"
------------------------------------------------------ */
void vm_async_console_tc(void *packet, size_t packet_len);
/* ------------------------------------------------------
--  Synchronous Required Interface "check_queue"
------------------------------------------------------ */
void vm_console_check_queue(void *, size_t *);
#endif
