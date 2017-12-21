import jsonschema
import json


class ValidateJson(object):
    def check(self, file: dict):
        dir = "schemas/"
        svc = file["data"]["pck_sec_head"]["msg_type_id"]["service_type_id"]
        msg = file["data"]["pck_sec_head"]["msg_type_id"]["msg_subtype_id"]

        try:
            if (svc, msg) == (8, 1):
                self.__validate__(file, dir + "st08_1_schema.json")
            elif svc == 12:
                if msg == 1 or msg == 2:
                    self.__validate__(file, dir + "st12_1_2_schema.json")
                else:
                    self.__validate__(file, dir + "st12_15_16_schema.json")
            elif svc == 17:
                self.__validate__(file, dir + "st17_1_schema.json")
            elif svc == 19:
                if msg == 1:
                    pass
                else:
                    self.__validate__(file, dir + "st19_2_4_5_schema.json")
        except Exception:
            raise

    @staticmethod
    def __validate__(file: dict, schema: str):
        with open(schema, "r") as sch_file:
            schema = json.load(sch_file)
        try:
            jsonschema.validate(file, schema)
        except Exception:
            raise
