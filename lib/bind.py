import re
import sys


def bind_class(route, _file, _ofile):
    classes = []
    comment = False
    flag = False
    lines = f.readlines()
    regex_1 = "(\t)*typedef struct( )*({){0,1}"
    regex_3 = "(\t)*}( )*\w+;[\s\S]*(\n)*"

    with open(route + _file, "r") as f:
        for line in lines:
            if "/*" in line:
                comment = True
            if "*/" in line:
                comment = False
            if comment:
                continue
            if re.match(regex_1, line) and not flag:
                flag = True
            if re.match(regex_3, line) and flag:
                flag = False
                line = line.split('{')[1][:-1]
                classes.append(line)
    return classes


def bind_fun(route, _file, _ofile):
    with open(route + _file, "r") as f:
        lines = f.readlines()
        regex = "(\w)+ (\w)+\("
        _ofile.write("\tpy::class_<"+_file[:-2]+"_t>(m, "+_file[:-2]+"_t)\n")
        for line in lines:
            if re.match(regex, line):
                line = line.split(' ')
                line = line[1].split('(')
                name = line[0]
                _ofile.write("\t\t.def(\"" + name + "\", &" + name + ", \"Binding for " + name + "\");\n")


def bind_header(_route, _file, _ofile):
    _ofile.write("#include<pybind11/pybind11.h>\n")
    _ofile.write("#include \"" + _route + _file + "\"\n")
    _ofile.write("\nnamespace py = pybind11;\n\n")


def bind_module(route, _file, _ofile):
    _ofile.write("PYBIND11_MODULE(" + _file[:-2] + ", m) {\n")
    _ofile.write("\tm.doc() = \"" + _file[:-2] + " binding\"\n")
    # bind_class(route, _file, _ofile)
    bind_fun(route, _file, _ofile)
    _ofile.write("}\n\n")


if len(sys.argv) > 1:
    route_to_h = sys.argv[1] + "/"
else:
    route_to_h = ""

files = ["pus_packet.h","pus_apid.h", "pus_st01_packets.h", "pus_st03_packets.h", "pus_st05_packets.h"]
for file_ in files:
    with open(file_[:-2] + ".cpp", "w") as outfile:
        bind_header(route_to_h, file_, outfile)
        bind_module(route_to_h, file_, outfile)



