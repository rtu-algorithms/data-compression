from PyQt5.QtWidgets import QMessageBox


def show_error_message(text, description):
    ErrorMessage('Kļūda', text, description).show()


class ErrorMessage:
    def __init__(self, title, text, description):
        self.error_message = QMessageBox()
        self.error_message = QMessageBox()
        self.error_message.setIcon(QMessageBox.Critical)
        self.error_message.setWindowTitle(title)
        self.error_message.setText(text)
        self.error_message.setInformativeText(description)

    def show(self):
        self.error_message.exec_()
