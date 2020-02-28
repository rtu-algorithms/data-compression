from PyQt5.QtWidgets import QMessageBox


def show_error_message_box(text, description):
    MessageBox(QMessageBox.Critical, 'Kļūda', text, description).show()


def show_message_box(text, description):
    MessageBox(QMessageBox.Information, 'Rezultāti', text, description).show()


class MessageBox:
    def __init__(self, icon, title, text, description):
        self.message_box = QMessageBox()
        self.message_box.setIcon(icon)
        self.message_box.setWindowTitle(title)
        self.message_box.setText(text)
        self.message_box.setInformativeText(description)

    def show(self):
        self.message_box.exec_()
