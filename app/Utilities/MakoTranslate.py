from mako.template import Template
import json
import os


class MakoTranslate(object):
    def __init__(self):
        self.version = {"V0": 0, "V1": 1, "INVALID_VERSION": 15}

        st3_st12_params_data = open(os.path.join("../../tools-libpus/mission/test_01", "st03_st12_config.json"))
        st3_st12_params_json = json.load(st3_st12_params_data)
        self.st3_12_params = dict()
        for i, e in enumerate(st3_st12_params_json["parameters"]):
            self.st3_12_params[e["label"]] = i

        st20_params_data = open(os.path.join("../../tools-libpus/mission/test_01", "st20_config.json"))
        st20_params_json = json.load(st20_params_data)
        self.st20_params = dict()
        for i, e in enumerate(st20_params_json["parameters"]):
            self.st20_params[e["label"]] = i

        self.values = [self.version, self.st3_12_params, self.st20_params]

        self.template_values = ""
        self.__create_value_string__()

    def __create_value_string__(self):
        for elem in self.values:
            for k, v in elem.items():
                self.template_values += "<%{} = {}%>".format(k, v)

    def replace(self, json_data):
        if type(json_data) is dict:
            data = json.dumps(json_data)
        else:
            data = json_data

        res = Template(self.template_values+data).render()
        return res
