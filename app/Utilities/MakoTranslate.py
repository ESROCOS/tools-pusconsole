from mako.template import Template
import json


class MakoTranslate(object):

    def __init__(self):
        self.version = {"pus_V0": 0, "pus_V1": 1, "pus_INVALID_VERSION": 15}
        self.template_values = ""
        self.__create_value_string__()

    def __create_value_string__(self):
        for k, v in self.version.items():
            self.template_values += "<%{} = {}%>".format(k, v)

    def replace(self, json_data):
        print("Hola")
        if type(json_data) is dict:
            data = json.dumps(json_data)
        else:
            data = json_data

        res = Template(self.template_values+data).render()
        print(res)
        return res
