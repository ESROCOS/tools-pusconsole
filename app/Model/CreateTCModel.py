class CreateTCModel(object):

    def __init__(self, app_model):
        self.app_model = app_model
        self.apid_info = self.app_model.tc_apid
        self.telecommand = {}
        with open("services.txt", "r") as services:
            for line in services:
                line = line.strip('\n').split("|")
                if len(line) == 4 and line[3] == "tc":
                    if line[0] not in self.telecommand:
                        self.telecommand[line[0]] = [line[1]]
                    else:
                        self.telecommand[line[0]].append(line[1])

    def add_to_table(self, json_data, packet):
        self.app_model.add(json_data, packet)