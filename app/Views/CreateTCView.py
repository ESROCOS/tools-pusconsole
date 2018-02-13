from PySide import QtGui

from Views.Views_Ui.Ui_CreateTCView import Ui_CreateTCView
import json


class CreateTCView(object):
    """
    This class represents a window. It references the class
    Ui_CreateTCView, that class is where the graphical interface
    is created
    """
    resizeFlag = False

    def __init__(self):
        self.view = QtGui.QWidget()
        self.window = Ui_CreateTCView()
        self.window.setupUi(self.view)
        self.extra_customization()
        self.view.resizeEvent = self.resize_elements

    def get_window(self):
        """
        This method returns the view that this class references

        :return: A view. It could be a QWidget, QMainWindow, etc.
        """
        return self.view

    def extra_customization(self):
        """
        This method allow us to define an extra configuration for the
        view without having to touch the code generated by the QtDesigner
        giving us a extra level of abstraction
        """
        self.window.addTcButton.hide()

    def resize_elements(self, event):
        """
        This method defines all the instructions needed to make
        our CreateTCView window responsive

        :param event: The event that triggers this method
        """
        padding = 20
        cte_w = self.window.commandTextEdit.frameGeometry().width()
        cte_h = self.window.commandTextEdit.frameGeometry().height()
        cte_x = self.window.commandTextEdit.pos().x()
        cte_y = self.window.commandTextEdit.pos().y()

        hl_w = self.window.historyList.frameGeometry().width()
        hl_h = self.window.historyList.frameGeometry().height()
        hl_x = self.window.historyList.pos().x()
        hl_y = self.window.historyList.pos().y()

        ctl_w = self.window.createTCLabel.frameGeometry().width()
        ctl_h = self.window.createTCLabel.frameGeometry().height()
        ctl_x = self.window.createTCLabel.pos().x()
        ctl_y = self.window.createTCLabel.pos().y()

        if self.resizeFlag:
            self.window.commandTextEdit.resize(self.view.frameGeometry().width() - 2 * padding,
                                               self.view.frameGeometry().height() - 3 * padding + 4 - cte_y)

            self.window.historyList.resize(self.view.frameGeometry().width() - 2 * padding, hl_h)
        else:
            self.resizeFlag = True

    def add_item_svc_type_combo_box(self, item: str):
        """
        This method fills in the service id combobox.
        :param item: element to be added to the combobox
        """
        self.window.serviceComboBox.addItem(item, int(item))

    def add_item_msg_type_combo_box(self, item: str):
        """
        This method fills in the message id combobox, for each
        service in the service combobox, with the messages ids
        of that service.
        :param item: element to be added to the combobox
        """
        self.window.msgComboBox.addItem(item, int(item))

    def add_item_history_list(self, item):
        self.window.historyList.addItem(item)

    def clear_history_list(self):
        self.window.historyList.clear()

    def clear_msg_type_combo_box(self):
        """
        This method clears the message combobox
        """
        self.window.msgComboBox.clear()

    def show(self):
        """
        This method calls to the .show() method of the view referenced
        by this class
        """
        self.view.show()

    def set_tc_text(self, json):
        """
        This method prints in the text box a json template
        making the creation of telecommands easier

        :param json: String in json format with the TC template
        """
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setStyleHint(QtGui.QFont.Monospace)
        font.setFixedPitch(True)
        font.setPointSize(10)
        metrics = QtGui.QFontMetrics(font)
        self.window.commandTextEdit.setTabStopWidth(metrics.width(' '))
        self.window.commandTextEdit.setPlainText(json)

    def get_tc_text(self):
        """
        This method returns the json that appears in
        the window textbox
        :return: json with the packet
        """
        return self.window.commandTextEdit.toPlainText()

    def close(self):
        """
        This method closes the view
        """
        self.view.close()
