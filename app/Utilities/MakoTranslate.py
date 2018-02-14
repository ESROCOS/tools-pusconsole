from mako.template import Template
import json


class MakoTranslate(object):

    def __init__(self):
        self.version = {"V0": 0, "V1": 1, "INVALID_VERSION": 15}
        self.template_values = ""
        self.__create_value_string__()

    def __create_value_string__(self):
        for k, v in self.version.items():
            self.template_values += "<%{} = {}%>".format(k, v)

    def replace(self, json_data):
        if type(json_data) is dict:
            data = json.dumps(json_data)
        else:
            data = json_data

        res = Template(self.template_values+data).render()
        return res
