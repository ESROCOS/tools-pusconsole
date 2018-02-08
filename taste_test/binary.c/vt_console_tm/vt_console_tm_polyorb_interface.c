#include "po_hi_gqueue.h"
/* This file was generated automatically: DO NOT MODIFY IT ! */

#include "vt_console_tm_polyorb_interface.h"

#include "activity.h"
#include "types.h"
#include "po_hi_task.h"
/* ------------------------------------------------------
-- Asynchronous Provided Interface "artificial_tm"
------------------------------------------------------ */
void po_hi_c_vt_console_tm_artificial_tm(__po_hi_task_id e, dataview__puspacket_buffer_impl buf)
{
   sync_console_tm (buf.buffer, buf.length);
}

/* ------------------------------------------------------
--  Synchronous Required Interface "tm"
------------------------------------------------------ */
void vm_vt_console_tm_tm(void *packet, size_t packet_len)
{
   sync_console_tm(packet, packet_len);
}

/* ------------------------------------------------------
--  Asynchronous Required Interface "tc_vt"
------------------------------------------------------ */
void vm_async_vt_console_tm_tc_vt(void *packet, size_t packet_len)
{
   __po_hi_request_t request;

   __po_hi_copy_array(&(request.vars.vt_console_tm_global_outport_tc_vt.vt_console_tm_global_outport_tc_vt.buffer), packet, packet_len);
   request.vars.vt_console_tm_global_outport_tc_vt.vt_console_tm_global_outport_tc_vt.length = packet_len;
   request.port = vt_console_tm_global_outport_tc_vt;
   __po_hi_gqueue_store_out(x86_partition_vt_console_tm_k, vt_console_tm_local_outport_tc_vt, &request);
   __po_hi_send_output(x86_partition_vt_console_tm_k, vt_console_tm_global_outport_tc_vt);
}

/* ------------------------------------------------------
--  Synchronous Required Interface "check_queue_vt"
------------------------------------------------------ */
void vm_vt_console_tm_check_queue_vt(void *res, size_t *res_len)
{
   sync_x86_partition_taste_api_console_has_pending_msg(res, res_len);
}

