from PyQt5 import QtWidgets, uic
from huffman_coding.HuffmanCoding import HuffmanCoding


def huffman_coding():
    path = "files/input.txt"
    h = HuffmanCoding(path)
    output_path = h.compress()
    h.decompress(output_path)


class Gui(QtWidgets.QMainWindow):
    @staticmethod
    def user_choose_file_name(title: str) -> str:
        file_name, _ = QtWidgets.QFileDialog.getOpenFileName(None, title, "", "All files (*)")
        return file_name

    def __init__(self):
        super(Gui, self).__init__()
        uic.loadUi('gui/gui.ui', self)

        # btnHello
        self.btnHello = self.findChild(QtWidgets.QPushButton, 'btnHello')
        self.btnHello.clicked.connect(self.btn_hello_pressed)

        # btnHello
        self.txtLabel = self.findChild(QtWidgets.QLabel, 'txtLabel')

        self.show()

    def btn_hello_pressed(self):
        input_file_name = self.user_choose_file_name("Select Input File")
        self.txtLabel.setText(input_file_name)
        print(input_file_name)


