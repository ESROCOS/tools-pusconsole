from PySide import QtGui, QtCore
from Views.Views_Ui.Ui_CodeView import Ui_CodeView


class DetailsView:
    """
    This class represents a window. It references the class
    Ui_DetailsView, that class is where the graphics
    are created
    """
    resizeFlag = False

    def __init__(self):
        """
        This is the constructor of the class
        """
        self.view = QtGui.QWidget()
        self.window = Ui_CodeView()
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
        self.view.setStyleSheet("background-color: white")

    def resize_elements(self, event):
        """
        This method defines all the instructions needed to make
        our DetailsView window responsive

        :param event: The event that triggers this method
        """
        padding = 20
        if self.resizeFlag:
            pass
        else:
            self.resizeFlag = True

    def getCode(self):
        return self.window.plainTextEdit.toPlainText()

    def show(self):
        """
        This method calls to the .show() method of the view referenced
        by this class
        """
        return self.view.exec_()
