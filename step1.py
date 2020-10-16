# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Step1.ui'
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


class Ui_Step1(object):
    def setupUi(self, Step1):
        if not Step1.objectName():
            Step1.setObjectName(u"Step1")
        Step1.resize(446, 280)
        Step1.setStyleSheet(u"background-color:rgb(71,71,71)")
        self.textBrowser = QTextBrowser(Step1)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(30, 70, 401, 111))
        self.textBrowser.setStyleSheet(u"  color: rgb(209,209,217);")
        self.label = QLabel(Step1)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(180, 20, 71, 31))
        font = QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet(u"  color: rgb(209,209,217);")
        self.pushButton_4 = QPushButton(Step1)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(160, 200, 121, 41))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setUnderline(False)
        font1.setWeight(87)
        font1.setStrikeOut(False)
        self.pushButton_4.setFont(font1)
        self.pushButton_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet(u"QPushButton {\n"
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

        self.retranslateUi(Step1)

        QMetaObject.connectSlotsByName(Step1)
    # setupUi

    def retranslateUi(self, Step1):
        Step1.setWindowTitle(QCoreApplication.translate("Step1", u"\u0428\u0430\u0433 1", None))
        self.textBrowser.setHtml(QCoreApplication.translate("Step1", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">\u0412\u044b\u043a\u043b\u044e\u0447\u0438 \u0432\u043e\u043b\u044c\u0442\u043c\u0435\u0442\u0440 \u0438\u0437 \u0441\u0435\u0442\u0438 \u0438 \u043f\u043e\u0441\u0442\u0430\u0440\u0430\u0439\u0441\u044f \u0440\u0430\u0437\u043c\u0435\u0441\u0442\u0438\u0442\u044c \u043a\u0430\u043c\u0435\u0440\u0443 \u0442\u0430\u043a, \u0447\u0442\u043e\u0431\u044b \u0440\u0430\u0441\u043f\u043e\u0437\u043d\u043e\u0432\u0430\u0435\u043c\u0430\u044f \u043e\u0431\u043b\u0430\u0441\u0442\u044c \u043f\u043e\u043f\u0430\u043b\u0430 \u0432 \u0437"
                        "\u0435\u043b\u0435\u043d\u044b\u0439 \u043f\u0440\u044f\u043c\u043e\u0443\u0433\u043e\u043b\u044c\u043d\u0438\u043a</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("Step1", u"\u0428\u0430\u0433 1", None))
        self.pushButton_4.setText(QCoreApplication.translate("Step1", u"\u0414\u0430\u043b\u0435\u0435", None))
    # retranslateUi

