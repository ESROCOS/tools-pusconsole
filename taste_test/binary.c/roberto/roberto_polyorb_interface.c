#include "po_hi_gqueue.h"
/* This file was generated automatically: DO NOT MODIFY IT ! */

#include "roberto_polyorb_interface.h"

#include "activity.h"
#include "types.h"
#include "po_hi_protected.h"

#include "po_hi_task.h"
#include "roberto_vm_if.h"

/*----------------------------------------------------
-- Protected Provided Interface "tc"
----------------------------------------------------*/
void sync_roberto_tc(void *packet, size_t packet_len)
{
   extern process_package__taste_protected_object roberto_protected;
   __po_hi_protected_lock (roberto_protected.protected_id);
   roberto_tc(packet, packet_len);
   __po_hi_protected_unlock (roberto_protected.protected_id);
}

/*----------------------------------------------------
-- Protected Provided Interface "trigger"
----------------------------------------------------*/
void sync_roberto_trigger()
{
   extern process_package__taste_protected_object roberto_protected;
   __po_hi_protected_lock (roberto_protected.protected_id);
   roberto_trigger();
   __po_hi_protected_unlock (roberto_protected.protected_id);
}

/* ------------------------------------------------------
--  Asynchronous Required Interface "tm"
------------------------------------------------------ */
void vm_async_roberto_tm(void *packet, size_t packet_len)
{
   switch(__po_hi_get_task_id()) {
      case x86_partition_vt_roberto_tc_k: vm_async_vt_roberto_tc_tm_vt(packet, packet_len); break;
      case x86_partition_vt_roberto_trigger_k: vm_async_vt_roberto_trigger_tm_vt(packet, packet_len); break;
      default: break;
   }
}

/* ------------------------------------------------------
--  Synchronous Required Interface "check_queue"
------------------------------------------------------ */
void vm_roberto_check_queue(void *res, size_t *res_len)
{
   sync_x86_partition_taste_api_roberto_has_pending_msg(res, res_len);
}

