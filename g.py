import sys
import time
#import random
#from PySide2 import QtCore, QtWidgets, QtGui      # ваш импорт
from PyQt5 import QtCore, QtWidgets, QtGui         # мой импорт
#import time


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.button = QtWidgets.QPushButton("Start")
        self.button.clicked.connect(self.click)

        self.text = QtWidgets.QLabel(time.ctime().split(" ")[3])
        self.text.setAlignment(QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_func)
        self.m, self.s, self.h = 0, 0, 0

    def click(self):
        self.timer.start(10)                     # 10 ms

    def update_func(self):
        self.text.setText(time.ctime().split(" ")[3])


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())