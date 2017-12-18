import sys, json
from collections import OrderedDict


def convert(dic):
    mapa = OrderedDict()
    for k in dic:
        v = dic[k]
        mapa[k] = OrderedDict()
        if type(v) == dict:
            mapa[k]["type"] = "object"
            mapa[k]["properties"] = convert(v)
        elif type(v) == bool:
            mapa[k]["type"] = "boolean"
        elif type(v) == int:
            mapa[k]["type"] = "integer"
        elif type(v) == str:
            mapa[k]["type"] = "string"
    return mapa


file = "jsonexample.json"
f = open(file, "r")
dic = json.load(f)

mapa = OrderedDict()
mapa["$schema"] = "http://json-schema.org/schema#"
mapa["id"] = "https://github.com/esrocos/TBD"
mapa["type"] = "object"
mapa["properties"] = convert(dic)

print(json.dumps(mapa, indent=2))

