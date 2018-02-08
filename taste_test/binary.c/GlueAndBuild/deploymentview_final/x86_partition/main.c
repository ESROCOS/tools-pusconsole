#include <activity.h>
#include <po_hi_task.h>
#include <po_hi_main.h>
#include <types.h>
#include <po_hi_time.h>
/*****************************************************/
/*  This file was automatically generated by Ocarina */
/*  Do NOT hand-modify this file, as your            */
/*  changes will be lost when you re-run Ocarina     */
/*****************************************************/
extern void init_console (void);
extern void init_console (void);
extern void init_roberto (void);
extern void init_roberto (void);
process_package__taste_protected_object console_protected;
process_package__taste_protected_object roberto_protected;

/*!
 * \fn __PO_HI_MAIN_TYPE __PO_HI_MAIN_NAME (void)
 * \brief Main function executed by the system
 *
 * Full function name and return types are available  in the PolyORB-HI-C 
 * runtime header files.
 */
__PO_HI_MAIN_TYPE __PO_HI_MAIN_NAME (void)
{
  
/*!
 * \var period
 * \brief Variable for task period
 *
 * This variable is used to store the valueof the period of a task when we 
 * create it. The value put in the variable is set according to AADL model 
 * description
 */
  __po_hi_time_t period;

  __po_hi_initialize_early ();
  
/*!
 * Initialize the runtime
 */
  __po_hi_initialize ();
  init_console ();
  init_console ();
  init_roberto ();
  init_roberto ();
  console_protected.protected_id = 0;
  roberto_protected.protected_id = 1;
  
/*!
 * Store the period time for task vt_console_trigger
 */
  __po_hi_milliseconds (&(period), 2000);
  
/*!
 * \brief Making Periodic Task vt_console_trigger
 *
 * Make a periodic task according to AADL model requirements. The first 
 * parameter is the task identifier defined in deployment.h 
 * (x86_partition_vt_console_trigger_k) the second is the period defined in 
 * the AADL model. Third is the task priority ( 10), fourth is the stack 
 * size ( 50000 bytes) and last is the subprogram executed by the task
 */
  __po_hi_create_periodic_task (x86_partition_vt_console_trigger_k, &(period), 10, 50000, 0, vt_console_trigger_job);
  
/*!
 * Store the period time for task vt_console_tm
 */
  __po_hi_milliseconds (&(period), 1);
  
/*!
 * Making Sporadic task
 */
  __po_hi_create_sporadic_task (x86_partition_vt_console_tm_k, &(period), 1, 50000, 0, vt_console_tm_job);
  
/*!
 * Store the period time for task vt_roberto_tc
 */
  __po_hi_milliseconds (&(period), 1);
  
/*!
 * Making Sporadic task
 */
  __po_hi_create_sporadic_task (x86_partition_vt_roberto_tc_k, &(period), 1, 50000, 0, vt_roberto_tc_job);
  
/*!
 * Store the period time for task vt_roberto_trigger
 */
  __po_hi_milliseconds (&(period), 5000);
  
/*!
 * \brief Making Periodic Task vt_roberto_trigger
 *
 * Make a periodic task according to AADL model requirements. The first 
 * parameter is the task identifier defined in deployment.h 
 * (x86_partition_vt_roberto_trigger_k) the second is the period defined in 
 * the AADL model. Third is the task priority ( 10), fourth is the stack 
 * size ( 50000 bytes) and last is the subprogram executed by the task
 */
  __po_hi_create_periodic_task (x86_partition_vt_roberto_trigger_k, &(period), 10, 50000, 0, vt_roberto_trigger_job);
  
/*!
 * Waiting for other tasks initialization
 */
  __po_hi_wait_initialization ();
  
/*!
 * Used to switch the main task to sleep all the time
 */
  __po_hi_wait_for_tasks ();
  
/*!
 * Return Statement
 */
  return (__PO_HI_MAIN_RETURN);
}


