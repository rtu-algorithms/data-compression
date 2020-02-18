import sys
from gui.Gui import Gui
from PyQt5 import QtWidgets


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    gui = Gui()
    app.exec_()
