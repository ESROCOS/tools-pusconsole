#include "po_hi_gqueue.h"
/* This file was generated automatically: DO NOT MODIFY IT ! */

#include "console_polyorb_interface.h"

#include "activity.h"
#include "types.h"
#include "po_hi_protected.h"

#include "po_hi_task.h"
#include "console_vm_if.h"

/*----------------------------------------------------
-- Protected Provided Interface "trigger"
----------------------------------------------------*/
void sync_console_trigger()
{
   extern process_package__taste_protected_object console_protected;
   __po_hi_protected_lock (console_protected.protected_id);
   console_trigger();
   __po_hi_protected_unlock (console_protected.protected_id);
}

/*----------------------------------------------------
-- Protected Provided Interface "tm"
----------------------------------------------------*/
void sync_console_tm(void *packet, size_t packet_len)
{
   extern process_package__taste_protected_object console_protected;
   __po_hi_protected_lock (console_protected.protected_id);
   console_tm(packet, packet_len);
   __po_hi_protected_unlock (console_protected.protected_id);
}

/* ------------------------------------------------------
--  Asynchronous Required Interface "tc"
------------------------------------------------------ */
void vm_async_console_tc(void *packet, size_t packet_len)
{
   switch(__po_hi_get_task_id()) {
      case x86_partition_vt_console_trigger_k: vm_async_vt_console_trigger_tc_vt(packet, packet_len); break;
      case x86_partition_vt_console_tm_k: vm_async_vt_console_tm_tc_vt(packet, packet_len); break;
      default: break;
   }
}

/* ------------------------------------------------------
--  Synchronous Required Interface "check_queue"
------------------------------------------------------ */
void vm_console_check_queue(void *res, size_t *res_len)
{
   sync_x86_partition_taste_api_console_has_pending_msg(res, res_len);
}

