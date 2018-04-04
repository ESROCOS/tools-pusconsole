{ "activities": [
  {
    "interval": 1,
    "packet": {
      ${macros.primary_header_defaults()},
      "data": {
        "user_data": {
          "src_data": {
           "function_id": 1
          }
        },
        "pck_sec_head": {
          ${macros.tc_type(8, 1)},
          "src_id": 1,
          ${macros.acks(1,0,1,0)},
          "tc_packet_pus_version_number": 2
        }
      }
    }
  },
  {
    "interval": 1,

    "packet": {
      ${macros.primary_header_defaults()},
      "data": {
        "user_data": {
          "src_data": {}
        },
        "pck_sec_head": {
          ${macros.tc_type(17, 1)},
          ${macros.acks()},
          "tc_packet_pus_version_number": 2
        }
      }
    }
  }
]}