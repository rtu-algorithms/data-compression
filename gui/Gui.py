from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QRadioButton, QPushButton
from .utils import user_choose_file_name
from coding.CodingAlgorithms import CodingAlgorithms
from coding.CodingMethods import CodingMethods
from coding.coding import compress, decompress
from .ErrorMessage import show_error_message


class Gui(QMainWindow):
    def __init__(self):
        super(Gui, self).__init__()
        uic.loadUi('gui/gui.ui', self)

        # GUI: inputs
        self.input_input_file_path = self.findChild(QLineEdit, 'input_input_file_path')
        self.input_output_file_name = self.findChild(QLineEdit, 'input_output_file_name')
        self.input_secret_file_path = self.findChild(QLineEdit, 'input_secret_file_path')

        # GUI: radio buttons
        self.radio_btn_huffman_coding = self.findChild(QRadioButton, 'radio_btn_huffman_coding')
        self.radio_btn_arithmetic_coding = self.findChild(QRadioButton, 'radio_btn_arithmetic_coding')
        self.radio_btn_compress = self.findChild(QRadioButton, 'radio_btn_compress')
        self.radio_btn_decompress = self.findChild(QRadioButton, 'radio_btn_decompress')

        # GUI: radio button events
        self.radio_btn_compress.clicked.connect(self.radio_btn_compress_clicked)
        self.radio_btn_decompress.clicked.connect(self.radio_btn_decompress_clicked)

        # GUI: buttons
        self.btn_find_input_file_path = self.findChild(QPushButton, 'btn_find_input_file_path')
        self.btn_find_secret_file_path = self.findChild(QPushButton, 'btn_find_secret_file_path')
        self.btn_go = self.findChild(QPushButton, 'btn_go')

        # GUI: button events
        self.btn_find_input_file_path.clicked.connect(self.btn_find_input_file_path_clicked)
        self.btn_find_secret_file_path.clicked.connect(self.btn_find_secret_file_path_clicked)
        self.btn_go.clicked.connect(self.btn_go_clicked)

        self.show()

    def radio_btn_compress_clicked(self):
        self.input_output_file_name.setText('output.bin')

    def radio_btn_decompress_clicked(self):
        self.input_output_file_name.setText('decompressed.txt')

    def btn_find_input_file_path_clicked(self):
        try:
            input_file_name_path = user_choose_file_name("Izvēlēties Ievades failu")
            if input_file_name_path is not None:
                self.input_input_file_path.setText(input_file_name_path)
        except Exception as e:
            print(e)

    def btn_find_secret_file_path_clicked(self):
        try:
            secret_file_name_path = user_choose_file_name("Izvēlēties failu")
            if secret_file_name_path is not None:
                self.input_secret_file_path.setText(secret_file_name_path)
        except Exception as e:
            print(e)

    def btn_go_clicked(self):
        try:
            algorithm = None
            if self.radio_btn_huffman_coding.isChecked():
                algorithm = CodingAlgorithms.Huffman
            elif self.radio_btn_arithmetic_coding.isChecked():
                algorithm = CodingAlgorithms.Arithmetic
            else:
                show_error_message('Algorimts nav izvēlēts!',
                                   'Lūdzu, izvēlēties kādu no diviem algoritmiem: Huffman Coding vai Arithmetic Coding.')
                return

            method = None
            if self.radio_btn_compress.isChecked():
                method = CodingMethods.Compress
            elif self.radio_btn_decompress.isChecked():
                method = CodingMethods.Decompress
            else:
                show_error_message('Metode nav izvēlēts!',
                                   'Lūdzu, izvēlēties kādu no diviem metodēm: Saspiešana vai Dekodēšana.')
                return

            input_file_path = self.input_input_file_path.text()
            if not input_file_path:
                show_error_message('Ievades faila cēļš nav norādīts!',
                                   'Lūdzu, norādiet cēļu līdz ievades failam, ar kuru būs izdārīta saspiešana vai dekodēšana.')
                return

            output_file_name = self.input_output_file_name.text()
            output_file_path = None
            if not output_file_name:
                show_error_message('Izvades faila nosaukums nav norādīts!',
                                   'Lūdzu, norādiet ievades faila nosaukumu, kurā būs ierakstīts rezultāts.')
                return
            else:
                divider = '/'
                output_file_path = '{path_to_file}{divider}{file_name}'.format(
                    path_to_file=divider.join(input_file_path.split(divider)[:-1]),
                    divider=divider,
                    file_name=output_file_name)

            secret_file_path = None
            if algorithm is CodingAlgorithms.Huffman:
                if method is CodingMethods.Decompress:
                    secret_file_path = self.input_secret_file_path.text()
                    if not secret_file_path:
                        show_error_message('Dekodešanas faila cēļš nav norādīts!',
                                           'Lūdzu, norādiet cēļu līdz dekodešanas failam priekš Huffman algoritmam.')
                        return
                else:
                    divider = '/'
                    secret_file_path = '{path_to_file}{divider}{file_name}'.format(
                        path_to_file=divider.join(input_file_path.split(divider)[:-1]),
                        divider=divider,
                        file_name='decode_secret.pkl')

            # Call Coding algorithms
            if method is CodingMethods.Compress:
                compress(algorithm, input_file_path, output_file_path, secret_file_path)
            else:
                decompress(algorithm, input_file_path, output_file_path, secret_file_path)
        except Exception as e:
            print(e)
