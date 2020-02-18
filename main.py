import sys
from gui import gui
from PyQt5 import QtWidgets


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    gui = gui.Gui()
    app.exec_()
