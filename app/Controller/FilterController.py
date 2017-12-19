from PySide import QtCore, QtGui
from Views import FilterView
from Model import FilterModel


class FilterController(object):
    def __init__(self, model: FilterModel, view: FilterView):
        self.model = model
        self.view = view
        self.set_callbacks()

    def set_callbacks(self):
        self.view.window.okButton.clicked.connect(self.accept_callback)
        self.view.window.cancelButton.clicked.connect(self.reject_callback)

    def accept_callback(self):
        type_combo_box = self.view.window.typeComboBox
        type = type_combo_box.itemData(type_combo_box.currentIndex())

        try:
            svc_text = self.view.window.serviceIdLineEdit.text()
            if svc_text == "":
                svc = 0
            else:
                svc = int(svc_text)

            msg_text = self.view.window.msgIdLineEdit.text()
            if msg_text == "":
                msg = 0
            else:
                msg = int(msg_text)

            self.model.set_filter_options(type, svc, msg)
            self.view.view.accept()
        except ValueError as ve:
            msg_box = QtGui.QMessageBox()
            msg_box.setText('Some fields may be incorrect {}'.format(ve))
            msg_box.setStandardButtons(QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel)
            msg_box.exec_()

    def reject_callback(self):
        self.view.view.reject()

    def show(self):
        code = self.view.show()
        if code == 1:
            return self.model.get_filter_options()
        else:
            return None
