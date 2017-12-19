from PySide import QtCore
from PySide.QtCore import QThread
from . import PacketTranslator
import json


class PusThread(QThread):
    def __init__(self, file):
        self.file = file
        super().__init__()

    def run(self):
        pt = PacketTranslator()
        with open(self.file, "r") as json_data:
            tcs = json.load(json_data)
            for elem in tcs["telecommands"]:
                self.sleep(elem["elapsed_time"])
                self.emit(QtCore.SIGNAL("add(pack"), elem["packet"])
