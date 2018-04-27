import json

class CreateTCModel(object):
    """
    This class represents the model of a createTC view
    """
    def __init__(self, app_model):
        """
        This is the constructor of the class
        :param app_model: The model of the upper class, in this
        case this is the model of the application
        """
        self.telecommand = {}
        self.app_model = app_model
        self.apid_info = self.app_model.tc_apid
        self.telecommand = {}
        with open("config.json") as services:
            data = json.load(services)
            for svc, msg in data["tc"]:
                svc = str(svc)
                msg = str(msg)
                if svc not in self.telecommand:
                    self.telecommand[svc] = [msg]
                else:
                    self.telecommand[svc].append(msg)

    def add_to_table(self, packet):
        """
        This method adds a packet in json and packet format to the
        table model of the app
        :param json_data: The packet in json format
        :param packet: The packet
        """
        self.app_model.add(packet)
