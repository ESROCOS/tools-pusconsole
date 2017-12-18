import sys, json


def convert(dic, tab):
    for k in dic:
        v = dic[k]
        print(' '*tab + "\"" + k + "\":{")
        if type(v) == dict:
            print(' '*(tab+2) + "\"type\":\"object\",")
            print(' '*(tab+2) + "\"properties\":{")
            convert(v, tab+4)
            print(' '*(tab+2), "},")
        elif type(v) == bool:
            print(' '*(tab+2) + "\"type\":\"boolean\",")
        elif type(v) == int:
            print(' '*(tab+2) + "\"type\":\"integer\",")
        elif type(v) == str:
            print(' '*(tab+2) + "\"type\":\"string\",")
        print(' '*tab + "}")


file = "jsonexample.json"
f = open(file, "r")
dic = json.load(f)
print("""{
  "$schema": "http://json-schema.org/schema#",
  "id": "https://github.com/esrocos/TBD",
  "type": "object",
  "properties": {""")
convert(dic, 4)
print("  }")
print("}")
