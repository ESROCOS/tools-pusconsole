from PySide.QtCore import QObject, Signal, Slot
from PySide.QtCore import QThread, QWaitCondition, QMutex, QTimer
from . import PacketTranslator
import json, sys, os
lib_path = os.path.join('/home/esrocos/esrocos-ws-pus/tools-libpus/debug/pylib')
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
    def __init__(self, model):
        """
        This is the constructor of the class
        :param file: The json file where the packets are defined
        :param model: The model of the application
        """
        QThread.__init__(self)
        self.model = model
        self.signal = MySignal()
        self.signal.signal.connect(self.model.add)
        self.json_file = None
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_packets)
        self.json_file_loaded = QWaitCondition()
        self.mutex = QMutex()

    def run(self):
        """
        This method runs the thread reading from
        the json defined and making an sleep of T
        seconds between packet and packet according
        to the interval defined in the json file.
        """
        ACTIVITIES_TAG = "activities"
        INTERVAL_TAG = "interval"
        PACKET_TAG = "packet"

        self.timer.start(1000)

        while True:
            self.mutex.lock()
            self.json_file_loaded.wait(self.mutex)
            file = self.json_file
            self.mutex.unlock()

            pt = PacketTranslator()
            if file is not None:
                with open(file) as jfile:
                    activities = json.loads(jfile.read())[ACTIVITIES_TAG]
                    for activity in activities:
                        interval = activity[INTERVAL_TAG]
                        self.sleep(interval)
                        if PACKET_TAG in activity:
                            packet = pt.json2packet(activity[PACKET_TAG])
                            pb.pus_notify_sendPacket(packet)
                            self.signal.throw(packet)
            self.mutex.lock()
            self.json_file = None
            self.mutex.unlock()

    def update_packets(self):
        for _ in range(3):
            packet = pb.pusPacket_t()
            if pb.pusError_t.PUS_NO_ERROR == pb.pus_notify_readTm(packet):  # Comprobar si null
                self.signal.throw(packet)

    def load_test(self, json_file):
        self.mutex.lock()
        self.json_file = json_file
        if json_file is not None:
            self.json_file_loaded.wakeAll()
        self.mutex.unlock()

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
