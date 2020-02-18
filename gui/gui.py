from PyQt5 import QtWidgets, uic


def user_choose_file_name(title: str) -> str:
    file_name, _ = QtWidgets.QFileDialog.getOpenFileName(None, title, "", "All files (*)")
    return file_name


class Gui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Gui, self).__init__()
        uic.loadUi('gui/gui.ui', self)

        # input_input_file
        self.input_input_file = self.findChild(QtWidgets.QLineEdit, 'input_input_file')

        # btn_find_input_file
        self.btn_find_input_file = self.findChild(QtWidgets.QPushButton, 'btn_find_input_file')
        self.btn_find_input_file.clicked.connect(self.btn_find_input_file_pressed)

        self.show()

    def btn_find_input_file_pressed(self):
        try:
            input_file_name = user_choose_file_name("Izvēlēties Ievades failu")
            if input_file_name is not None:
                self.input_input_file.setText(input_file_name)
        except Exception as e:
            print(e)
