from PyQt5 import QtWidgets


def user_choose_file_name(title: str) -> str:
    file_name, _ = QtWidgets.QFileDialog.getOpenFileName(None, title, "", "All files (*)")
    return file_name
