# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1062, 865)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_head = QtWidgets.QLabel(self.centralwidget)
        self.label_head.setGeometry(QtCore.QRect(20, 20, 1011, 81))
        self.label_head.setStyleSheet("background-color:green;\n"
"color:white;\n"
"align:center;\n"
"font-size:40px;")
        self.label_head.setObjectName("label_head")
        self.label_video = QtWidgets.QLabel(self.centralwidget)
        self.label_video.setGeometry(QtCore.QRect(80, 180, 851, 441))
        self.label_video.setStyleSheet("background-color:white;")
        self.label_video.setText("")
        self.label_video.setObjectName("label_video")
        self.pushButton_open = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_open.setGeometry(QtCore.QRect(160, 700, 75, 23))
        self.pushButton_open.setObjectName("pushButton_open")
        self.pushButton_close = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_close.setGeometry(QtCore.QRect(280, 700, 75, 23))
        self.pushButton_close.setObjectName("pushButton_close")
        self.pushButton_last = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_last.setGeometry(QtCore.QRect(740, 700, 75, 23))
        self.pushButton_last.setObjectName("pushButton_last")
        self.pushButton_next = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_next.setGeometry(QtCore.QRect(860, 700, 75, 23))
        self.pushButton_next.setObjectName("pushButton_next")
        self.pushButton_pause = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_pause.setGeometry(QtCore.QRect(410, 700, 75, 23))
        self.pushButton_pause.setObjectName("pushButton_pause")
        self.pushButton_restart = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_restart.setGeometry(QtCore.QRect(570, 700, 75, 23))
        self.pushButton_restart.setObjectName("pushButton_restart")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1062, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_head.setText(_translate("MainWindow", "智能辅助装配系统"))
        self.pushButton_open.setText(_translate("MainWindow", "打开"))
        self.pushButton_close.setText(_translate("MainWindow", "关闭"))
        self.pushButton_last.setText(_translate("MainWindow", "上一步"))
        self.pushButton_next.setText(_translate("MainWindow", "下一步"))
        self.pushButton_pause.setText(_translate("MainWindow", "暂停"))
        self.pushButton_restart.setText(_translate("MainWindow", "继续"))
