#ifndef __OCARINA_GENERATED_TYPES_H_
#define __OCARINA_GENERATED_TYPES_H_ 
#include <po_hi_types.h>
#include <po_hi_protected.h>
/*****************************************************/

/*  This file was automatically generated by Ocarina */

/*  Do NOT hand-modify this file, as your            */

/*  changes will be lost when you re-run Ocarina     */

/*****************************************************/

typedef struct
{
  __po_hi_protected_t protected_id;

} process_package__taste_protected_object;

typedef char dataview__stream_element_buffer;

typedef dataview__stream_element_buffer dataview__puspacket_buffer_max_impl[5784];

typedef __po_hi_uint32_t base_types__unsigned_32;

typedef struct
{
  dataview__puspacket_buffer_max_impl buffer;

  base_types__unsigned_32 length;

} dataview__puspacket_buffer_impl;

#endif
