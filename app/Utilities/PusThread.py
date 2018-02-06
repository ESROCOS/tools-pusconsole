from PySide.QtCore import QObject, Signal, Slot
from PySide.QtCore import QThread
from . import PacketTranslator
import json, sys, os
lib_path = os.path.join('/home/esrocos/esrocos-ws-pus/pus/debug/pylib')
sys.path.append(lib_path)
import pusbinding as pb

class MySignal(QObject):
    """
    This class overrides a QObject to be
    able to emit custom signals
    """
    signal = Signal(dict)

    def __init__(self):
        QObject.__init__(self)

    def throw(self, elem):
        """
        This method emits the signal object defined
        inside the class
        :param elem: The element that will be emited with
        the signal
        """
        self.signal.emit(elem)


class PusThread(QThread):
    """
    This class overrides a QThread object to be able to
    define custom safe threads with custom signals. This
    class is used to be able to make a simulation of a connection
    with the robot where the packets arrives with an interval
    between them without blocking the rest of the functionality
    of the application. The simulation is done by reading the
    packets from a json file.

    """
    def __init__(self, file, model):
        """
        This is the constructor of the class
        :param file: The json file where the packets are defined
        :param model: The model of the application
        """
        QThread.__init__(self)
        self.file = file
        self.model = model
        self.signal = MySignal()
        self.signal.signal.connect(self.model.add)

    def run(self):
        """
        This method runs the thread reading from
        the json defined and making an sleep of T
        seconds between packet and packet according
        to the interval defined in the json file.
        """
        import time

        while True:
            time.sleep(1)
            for _ in range(3):
                packet = pb.pusPacket_t()
                if pb.pusError_t.PUS_NO_ERROR == pb.pus_notify_readTm(packet): # Comprobar si null
                    self.signal.throw(packet)

    # @Slot(pb.pusPacket_t)
    # def add(self, packet):
    #     """
    #     This method adds an element to the table model
    #     :param packet: The element to be added
    #     :return:
    #     """
    #     pt = PacketTranslator()
    #     elem = pt.packet2json(packet)
    #     self.model.add(elem, packet)
