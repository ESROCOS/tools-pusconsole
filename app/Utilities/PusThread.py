from PySide.QtCore import QObject, Signal, Slot
from PySide.QtCore import QThread
from . import PacketTranslator
import json


class MySignal(QObject):
    signal = Signal(dict)

    def __init__(self):
        QObject.__init__(self)

    def throw(self, elem):
        self.signal.emit(elem)

class PusThread(QThread):
    def __init__(self, file, model):
        QThread.__init__(self)
        self.file = file
        self.model = model
        self.signal = MySignal()
        self.signal.signal.connect(self.add)

    def run(self):
        pt = PacketTranslator()
        with open(self.file, "r") as json_data:
            tcs = json.load(json_data)
            for elem in tcs["telecommands"]:
                self.sleep(elem["elapsed_time"])
                self.signal.throw(elem["packet"])

    @Slot(dict)
    def add(self, elem):
        pt = PacketTranslator()
        packet = pt.json2packet(elem)
        self.model.add(elem, packet)
