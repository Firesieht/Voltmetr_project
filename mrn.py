# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MenuSPTgNx.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from step2 import Ui_Menu1

class Ui_Menu(object):

    def setupUi(self, Menu):
        if not Menu.objectName():
            Menu.setObjectName(u"Menu")
        Menu.resize(484, 449)
        Menu.setStyleSheet(u"background-color:rgb(71,71,71)")
        self.centralwidget = QWidget(Menu)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(30, 330, 181, 31))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(87)
        font.setStrikeOut(False)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"  position: relative;\n"
"  display: inline-block;\n"
"  font-size: 90%;\n"
"  font-weight: 700;\n"
"  color: rgb(209,209,217);\n"
"  text-decoration: none;\n"
"  text-shadow: 0 -1px 2px rgba(0,0,0,.2);\n"
"  padding: .5em 1em;\n"
"  outline: none;\n"
"  border-radius: 3px;\n"
"  background: linear-gradient(rgb(110,112,120), rgb(81,81,86)) rgb(110,112,120);\n"
"  box-shadow:\n"
"   0 1px rgba(255,255,255,.2) inset,\n"
"   0 3px 5px rgba(0,1,6,.5),\n"
"   0 0 1px 1px rgba(0,1,6,.2);\n"
"  transition: .2s ease-in-out;\n"
"}\n"
"QPushButton:hover {\n"
"  background: linear-gradient(rgb(126,126,134), rgb(70,71,76)) rgb(126,126,134);\n"
"}\n"
"QPushButton:pressed {\n"
"  top: 1px;\n"
"  background: linear-gradient(rgb(76,77,82), rgb(56,57,62)) rgb(76,77,82);\n"
"  box-shadow:\n"
"   0 0 1px rgba(0,0,0,.5) inset,\n"
"   0 2px 3px rgba(0,0,0,.5) inset,\n"
"   0 1px 1px rgba(255,255,255,.1);\n"
"}")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(240, 330, 171, 31))
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"  position: relative;\n"
"  display: inline-block;\n"
"  font-size: 90%;\n"
"  font-weight: 700;\n"
"  color: rgb(209,209,217);\n"
"  text-decoration: none;\n"
"  text-shadow: 0 -1px 2px rgba(0,0,0,.2);\n"
"  padding: .5em 1em;\n"
"  outline: none;\n"
"  border-radius: 3px;\n"
"  background: linear-gradient(rgb(110,112,120), rgb(81,81,86)) rgb(110,112,120);\n"
"  box-shadow:\n"
"   0 1px rgba(255,255,255,.2) inset,\n"
"   0 3px 5px rgba(0,1,6,.5),\n"
"   0 0 1px 1px rgba(0,1,6,.2);\n"
"  transition: .2s ease-in-out;\n"
"}\n"
"QPushButton:hover {\n"
"  background: linear-gradient(rgb(126,126,134), rgb(70,71,76)) rgb(126,126,134);\n"
"}\n"
"QPushButton:pressed {\n"
"  top: 1px;\n"
"  background: linear-gradient(rgb(76,77,82), rgb(56,57,62)) rgb(76,77,82);\n"
"  box-shadow:\n"
"   0 0 1px rgba(0,0,0,.5) inset,\n"
"   0 2px 3px rgba(0,0,0,.5) inset,\n"
"   0 1px 1px rgba(255,255,255,.1);\n"
"}")
        self.spinBox_2 = QSpinBox(self.centralwidget)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setGeometry(QRect(310, 60, 91, 31))
        font1 = QFont()
        font1.setPointSize(12)
        self.spinBox_2.setFont(font1)
        self.spinBox_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.spinBox_2.setStyleSheet(u"  color: rgb(209,209,217);")
        self.spinBox_2.setMaximum(150)
        self.spinBox_1 = QSpinBox(self.centralwidget)
        self.spinBox_1.setObjectName(u"spinBox_1")
        self.spinBox_1.setGeometry(QRect(310, 20, 91, 31))
        self.spinBox_1.setFont(font1)
        self.spinBox_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.spinBox_1.setStyleSheet(u"  color: rgb(209,209,217);")
        self.spinBox_1.setMaximum(9999)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 20, 241, 21))
        self.label.setFont(font1)
        self.label.setStyleSheet(u"  color: rgb(209,209,217);")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 60, 271, 21))
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"  color: rgb(209,209,217);")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 120, 271, 21))
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"  color: rgb(209,209,217);")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 160, 271, 21))
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"  color: rgb(209,209,217);")
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(290, 120, 171, 31))
        font2 = QFont()
        font2.setPointSize(8)
        font2.setBold(True)
        font2.setUnderline(False)
        font2.setWeight(87)
        font2.setStrikeOut(False)
        self.pushButton_3.setFont(font2)
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet(u"QPushButton {\n"
"  position: relative;\n"
"  display: inline-block;\n"
"  font-size: 90%;\n"
"  font-weight: 700;\n"
"  color: rgb(209,209,217);\n"
"  text-decoration: none;\n"
"  text-shadow: 0 -1px 2px rgba(0,0,0,.2);\n"
"  padding: .5em 1em;\n"
"  outline: none;\n"
"  border-radius: 3px;\n"
"  background: linear-gradient(rgb(110,112,120), rgb(81,81,86)) rgb(110,112,120);\n"
"  box-shadow:\n"
"   0 1px rgba(255,255,255,.2) inset,\n"
"   0 3px 5px rgba(0,1,6,.5),\n"
"   0 0 1px 1px rgba(0,1,6,.2);\n"
"  transition: .2s ease-in-out;\n"
"}\n"
"QPushButton:hover {\n"
"  background: linear-gradient(rgb(126,126,134), rgb(70,71,76)) rgb(126,126,134);\n"
"}\n"
"QPushButton:pressed {\n"
"  top: 1px;\n"
"  background: linear-gradient(rgb(76,77,82), rgb(56,57,62)) rgb(76,77,82);\n"
"  box-shadow:\n"
"   0 0 1px rgba(0,0,0,.5) inset,\n"
"   0 2px 3px rgba(0,0,0,.5) inset,\n"
"   0 1px 1px rgba(255,255,255,.1);\n"
"}")
        Menu.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Menu)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 484, 22))
        Menu.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Menu)
        self.statusbar.setObjectName(u"statusbar")
        Menu.setStatusBar(self.statusbar)

        self.retranslateUi(Menu)

        QMetaObject.connectSlotsByName(Menu)
    # setupUi

    def retranslateUi(self, Menu):
        Menu.setWindowTitle(QCoreApplication.translate("Menu", u"Menu", None))
        self.pushButton.setText(QCoreApplication.translate("Menu", u"\u041d\u0430\u0447\u0430\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c", None))
        self.pushButton_2.setText(QCoreApplication.translate("Menu", u"\u041a\u0430\u043b\u0438\u0431\u0440\u043e\u0432\u043a\u0430", None))
        self.label.setText(QCoreApplication.translate("Menu", u"\u041f\u0440\u043e\u043c\u0435\u0436\u0443\u0442\u043e\u043a \u0437\u0430\u043f\u0438\u0441\u0438, \u0441\u0435\u043a", None))
        self.label_2.setText(QCoreApplication.translate("Menu", u"Начальное значение, вольты", None))
        self.label_3.setText(QCoreApplication.translate("Menu", u"\u0422\u0435\u043a\u0443\u0449\u0435\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435:", None))
        self.label_4.setText(QCoreApplication.translate("Menu", u"\u0412\u0440\u0435\u043c\u044f:", None))
        self.pushButton_3.setText(QCoreApplication.translate("Menu", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435", None))
    # retranslateUi

