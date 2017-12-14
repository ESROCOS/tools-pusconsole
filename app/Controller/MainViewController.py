from Views.MainView import MainView
from Views.CreateTCView import CreateTCView
from Views.NewConnectionView import NewConnectionView
from Views.DetailsView import DetailsView
from Views.FilterView import FilterView
from Utilities.Database import Database
from Utilities import PacketTranslator
from Model.CreateTCModel import CreateTCModel
from Model import App
from Controller.CreateTCController import CreateTCController
from PySide import QtGui, QtCore
import json
import collections


class MainViewController(object):
    """Controller of MainView view"""

    def __init__(self, model: App, view: MainView):
        """
        The constructor instantiates a MainViewController object


        :param model: The model of the application
        :param view: The view that will be controlled by this class.
                     In this case it will be an instance of the MainView
                     class
        """
        self.model = model
        self.view = view


    def set_callbacks(self):
        """
        This method connects all the callbacks defined in this class with
        every event in the Main View
        """
        self.view.window.actionCreate_TC.triggered.connect(self.open_create_tc_callback)
        self.view.window.actionAbout_GMV.triggered.connect(self.open_about_callback)
        self.view.window.actionNew_connection.triggered.connect(self.open_new_connection_callback)
        self.view.window.packagesTable.clicked.connect(self.open_more_details_window_callback)
        self.view.window.actionCreate_filter.triggered.connect(self.open_filter_callback)
        self.view.window.actionSave_as.triggered.connect(self.open_savefile_window_callback)
        self.view.window.actionLoad.triggered.connect(self.open_openfile_window_callback)
        self.model.table.onClear = self.clear_qtable_callback
        self.model.table.onChange = self.add_elem

    def open_create_tc_callback(self):
        """
        This method opens the Create Telecommand Window
        """
        self.__is_not_used__()
        create_tc_view = CreateTCView()
        create_tc_model = CreateTCModel(self.model)
        create_tc_controller = CreateTCController(create_tc_model, create_tc_view)

        create_tc_controller.show()

    def open_filter_callback(self):
        """
        This method opens the Create Telecommand Window
        """
        self.__is_not_used__()
        filter_view = FilterView()
        filter_view.show()

    def open_about_callback(self):
        """
        This method opens the GMV's about website
        """
        import webbrowser
        self.__is_not_used__()
        webbrowser.open("https://www.gmv.com/en/Company/AboutGMV/")

    def open_new_connection_callback(self):
        """
        This method opens the connection definition window
        """
        self.__is_not_used__()
        new_connection_view = NewConnectionView()
        new_connection_view.show()

    def open_more_details_window_callback(self, clicked_index):
        """
        This method opens and writes all the information
        of the package selected in the window
        """
        row = clicked_index.row()
        pt = PacketTranslator()
        index = int(self.view.window.packagesTable.item(row, 0).text())
        details_view = DetailsView()
        details_view.write_information(json.dumps(pt.packet2json(self.model.table[index][-2]), indent=8))
        details_view.show()

    def open_savefile_window_callback(self):
        file = QtGui.QFileDialog.getSaveFileName()
        d = Database(file[0])
        packages = [tuple(e) for e in self.model.table]

        d.insert_db("INSERT INTO packages VALUES(?,?,?,?,?,?,?,?,?,?)", packages)

        self.__is_not_used__()

    def open_openfile_window_callback(self):
        file = QtGui.QFileDialog.getOpenFileName()
        d = Database(file[0])

        elems = d.query_db("SELECT * FROM packages")
        self.model.table.clear()
        for elem in elems:
            self.model.table.append(list(elem))

        self.__is_not_used__()

    def __convert_dict(self, elem: collections.OrderedDict, tab_count: int = 0):
        """
        Intern function to convert a dictionary to str
        :param elem: The dictionary to convert
        :param tab_count: Number of tab for indenting elements of dict
        :return: A string representing the dict
        """
        result = """"""
        boolean = True if tab_count == 0 else False
        for k in sorted(elem.keys(), reverse=boolean):
            result += "\t" * tab_count + str(k) + ": "
            if type(elem[k]) == dict:
                result += "\n" + self.__convert_dict(elem[k], tab_count + 1) + "\n"
            else:
                result += str(elem[k]) + "\n"

        return result

    def add_elem(self, row, elem: list):
        """
        This method is called whenever a new package arrives or is sended
        :param row: place where the new package will be shown
        :param elem: json of the package to add to the table
        """
        column_type = [QtGui.QTableWidgetItem, IntegerTableWidgetItem, IntegerTableWidgetItem,
                       TimeTableWidgetItem, QtGui.QTableWidgetItem, QtGui.QTableWidgetItem,
                       IntegerTableWidgetItem, QtGui.QTableWidgetItem, QtGui.QTableWidgetItem]

        self.view.window.packagesTable.setSortingEnabled(False)
        row_count = self.view.window.packagesTable.rowCount()
        if row == row_count - 1:
            self.view.window.packagesTable.insertRow(row_count)

        self.view.window.packagesTable.setItem(row, 0, QtGui.QTableWidgetItem(str(row)))
        for i, e in enumerate(elem[:-2]):
            itm = column_type[i](str(e))
            self.view.window.packagesTable.setItem(row, i+1, itm)
            self.view.window.packagesTable.item(row, i+1).setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        self.view.window.packagesTable.setSortingEnabled(True)

    def clear_qtable_callback(self):
        self.view.window.packagesTable.clearContents()
        self.view.window.packagesTable.setRowCount(1)
        self.__is_not_used__()

    def show(self):
        self.view.get_window().show()

    @staticmethod
    def __is_not_used__():
        pass


class IntegerTableWidgetItem(QtGui.QTableWidgetItem):
    def __lt__(self, other):
        if isinstance(other, QtGui.QTableWidgetItem):
            my_value = int(self.data(QtCore.Qt.EditRole))
            other_value = int(other.data(QtCore.Qt.EditRole))

            return my_value < other_value

        return super().__lt__(other)


class TimeTableWidgetItem(QtGui.QTableWidgetItem):
    def __lt__(self, other):
        if isinstance(other, QtGui.QTableWidgetItem):
            import datetime
            my_value = datetime.datetime.strptime(self.data(QtCore.Qt.EditRole), '%H:%M:%S').time()
            other_value = datetime.datetime.strptime(other.data(QtCore.Qt.EditRole), '%H:%M:%S').time()

            return my_value < other_value

        return super().__lt__(other)

