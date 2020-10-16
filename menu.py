import sys
from PySide2.QtWidgets import QApplication, QMainWindow
import PySide2.QtCore
from step1 import Ui_Step1

from mrn import Ui_Menu
from step2 import Ui_Menu1
import func
from WorkImg import Application, writer
from PySide2.QtCore import QCoreApplication, QTimer
import time


f = func.func()


class CalibrWindow(QMainWindow):
    stepNum = 1

    def __init__(self):
        super(CalibrWindow, self).__init__()
        self.ui = Ui_Menu1()
        self.ui.setupUi(self)
        self.ui.pushButton_4.clicked.connect(self.btn_func)

    def btn_func(self):
        self.stepNum += 1

        if self.stepNum == 6:
            self.close()
            self.TwoWindow = Menu()
            self.TwoWindow.show()

        self.ui.label.setText("Шаг " + str(self.stepNum))

        if self.stepNum == 1:
            f.rectangle_img()
        if self.stepNum == 2:
            self.ui.textBrowser.setHtml(QCoreApplication.translate("Step1",
                                                                   u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                                   "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                                   "p, li { white-space: pre-wrap; }\n"
                                                                   "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                                                                   "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">""С помощью ползунков сделай так, чтобы на маске остались только зеленые квадраты""</span></p></body></html>",
                                                                   None))
            f.greenQuads()
        if self.stepNum == 3:
            self.ui.textBrowser.setHtml(QCoreApplication.translate("Step1",
                                                                   u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                                   "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                                   "p, li { white-space: pre-wrap; }\n"
                                                                   "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                                                                   "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">""Выдели зону, где располагются штрихи на вольтметре""</span></p></body></html>",
                                                                   None))
            f.recognition_zone()
        if self.stepNum == 4:
            self.ui.textBrowser.setHtml(QCoreApplication.translate("Step1",
                                                                   u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                                   "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                                   "p, li { white-space: pre-wrap; }\n"
                                                                   "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                                                                   "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">""Расположи камеру и ползунки так, чтобы счетчик показывал нужное тебе количество распозноваемых делений и на каждой черте был зеленый бокс""</span></p></body></html>",
                                                                   None))
            f.chert()
        if self.stepNum == 5:
            self.ui.textBrowser.setHtml(QCoreApplication.translate("Step1",
                                                                   u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                                   "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                                   "p, li { white-space: pre-wrap; }\n"
                                                                   "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                                                                   "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">""Включи вольтметр в сеть и расположи ползунки так, чтобы на маске остался только желтый элепс""</span></p></body></html>",
                                                                   None))
            f.yellow_eleps()


class Menu(QMainWindow):

    def __init__(self):
        super(Menu, self).__init__()
        self.ui = Ui_Menu()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.btn2)
        self.ui.pushButton.clicked.connect(self.btn)
        self.ui.pushButton_3.clicked.connect(self.safe)
        f = open("zp.txt", "w")
        f.write("None")
        timer = QTimer(self)
        timer.timeout.connect(self.clock)
        timer.start(1000)

    def safe(self):
        f = open("zp.txt", "r")
        a = f.readline()
        writer(a)


    def clock(self):
        self.ui.label_4.setText("Время: " + time.ctime().split(" ")[3])
        f = open("zp.txt", "r")
        a = f.readline()
        self.ui.label_3.setText("Текущие значение: " + a)

    def btn(self):
        Application(self.ui.spinBox_1.value(), self.ui.spinBox_2.value())

    def btn2(self):
        self.close()
        self.TwoWindow = CalibrWindow()
        self.TwoWindow.show()
        f.rectangle_img()


def menu():
    app = QApplication(sys.argv)

    window = Menu()
    window.show()
    app.exec_()


if __name__ == "__main__":
    menu()
