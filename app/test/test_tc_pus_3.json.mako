{ "activities": [
  {
    "interval": 0,
    "comment": "Disables parameter monitoring report",
    "packet": {
      ${macros.primary_header_defaults()},
      "data": {
        "pck_sec_head": {
          ${macros.tc_type(12, 16)},
          ${macros.acks()},
          "src_id": 1,
          "tc_packet_pus_version_number": 2
        },
        "user_data": {
          "src_data": {}
        }
      }
    }
  },
  {
    "interval": 1,
    "comment": "Sets HK_PARAM_REAL01 report",
    "packet": {
      ${macros.primary_header_defaults()},
      "data": {
        "pck_sec_head": {
          ${macros.tc_type(12, 1)},
          ${macros.acks()},
          "src_id": 1,
          "tc_packet_pus_version_number": 2
        },
        "user_data": {
          "src_data": {
            "pmon_id": ${HK_PARAM_REAL01}
          }
        }
      }
    }
  },
  {
    "interval": 5,
    "comment": "Disables parameter monitoring report",
    "packet": {
      ${macros.primary_header_defaults()},
      "data": {
        "pck_sec_head": {
          ${macros.tc_type(12, 16)},
          ${macros.acks()},
          "src_id": 1,
          "tc_packet_pus_version_number": 2
        },
        "user_data": {
          "src_data": {}
        }
      }
    }
  }
  {
    "interval": 5,
    "comment": "",
    "action": ${actions.save_database()}
  }
]}