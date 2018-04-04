import json


class Macros:
    @staticmethod
    def primary_header_defaults(seq=0):
        name = "\"primary_header\": "
        data = {
                "pck_data_len": 5736,
                "pck_seq_ctrl": {
                        "pck_seq": seq,
                        "pck_seq_flg": 3
                },
                "pck_id": {
                        "sec_head_flg": True,
                        "apid": 1,
                        "pck_type": 1
                },
                "pck_version": 0
        }

        return name + json.dumps(data, indent=8)

    @staticmethod
    def acks(start=0, acceptance=0, completion=0, progress=0):
        name = "\"ack_flags\": "
        data = {
            "ack_flag_start": bool(start),
            "ack_flag_acceptance": bool(acceptance),
            "ack_flag_completion": bool(completion),
            "ack_flag_progress": bool(progress)
          }

        return name + json.dumps(data, indent=8)


    @staticmethod
    def tc_type(svc, msg):
        name = "\"msg_type_id\": "
        data = {
            "service_type_id": svc,
            "msg_subtype_id": msg
        }

        return name + json.dumps(data, indent=8)

if __name__ == "__main__":
    print(Macros.primary_header_defaults(10))
    print(Macros.acks(1,0,1,0))