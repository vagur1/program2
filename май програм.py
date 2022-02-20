import logging
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import QSize
from style import style

import sys

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Програма мічта")
        self.setStyleSheet(style)

        self.text_edit = QtWidgets.QLineEdit(self)
        self.text_edit.setFont(QFont("CourierNew", 24, QFont.Bold))
        self.text_edit.setGeometry(75,75,150,30)

        self.btn = QtWidgets.QPushButton(self)
        self.btn.setIcon(QIcon('pic'))
        self.btn.setIconSize(QSize(140,100))
        self.btn.setGeometry(75, 130, 150, 40)
        self.btn.clicked.connect(self.text_reverse)
        self.btn.clicked.connect(self.log)

        self.log_file = logging.getLogger()

    def text_reverse(self):
        text = self.text_edit.text()
        text = text[::-1]
        self.text_edit.setText(text)

    def log(self):
        self.log_file.info("Шо ти хочеш тут побачити?")

def application():
    app = QApplication(sys.argv)
    window = Window()
    window.setFixedSize(300,250)
    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s %(asctime)s - %(message)s",
        handlers=[
            logging.FileHandler("logfile.log"),
            logging.StreamHandler()
        ]
    )

    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    application()

