#include "po_hi_gqueue.h"
/* This file was generated automatically: DO NOT MODIFY IT ! */

#include "vt_roberto_trigger_polyorb_interface.h"

#include "activity.h"
#include "types.h"
#include "po_hi_task.h"
/* ------------------------------------------------------
-- Asynchronous Provided Interface "artificial_trigger"
------------------------------------------------------ */
void po_hi_c_vt_roberto_trigger_artificial_trigger(__po_hi_task_id e)
{
   sync_roberto_trigger ();
}

/* ------------------------------------------------------
--  Synchronous Required Interface "trigger"
------------------------------------------------------ */
void vm_vt_roberto_trigger_trigger()
{
   sync_roberto_trigger();
}

/* ------------------------------------------------------
--  Asynchronous Required Interface "tm_vt"
------------------------------------------------------ */
void vm_async_vt_roberto_trigger_tm_vt(void *packet, size_t packet_len)
{
   __po_hi_request_t request;

   __po_hi_copy_array(&(request.vars.vt_roberto_trigger_global_outport_tm_vt.vt_roberto_trigger_global_outport_tm_vt.buffer), packet, packet_len);
   request.vars.vt_roberto_trigger_global_outport_tm_vt.vt_roberto_trigger_global_outport_tm_vt.length = packet_len;
   request.port = vt_roberto_trigger_global_outport_tm_vt;
   __po_hi_gqueue_store_out(x86_partition_vt_roberto_trigger_k, vt_roberto_trigger_local_outport_tm_vt, &request);
   __po_hi_send_output(x86_partition_vt_roberto_trigger_k, vt_roberto_trigger_global_outport_tm_vt);
}

/* ------------------------------------------------------
--  Synchronous Required Interface "check_queue_vt"
------------------------------------------------------ */
void vm_vt_roberto_trigger_check_queue_vt(void *res, size_t *res_len)
{
   sync_x86_partition_taste_api_roberto_has_pending_msg(res, res_len);
}

