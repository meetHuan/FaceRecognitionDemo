# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(919, 949)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, -30, 771, 461))
        self.widget.setObjectName("widget")
        self.videoLabel = QtWidgets.QLabel(self.widget)
        self.videoLabel.setGeometry(QtCore.QRect(50, 40, 601, 401))
        self.videoLabel.setAutoFillBackground(True)
        self.videoLabel.setText("")
        self.videoLabel.setObjectName("videoLabel")
        self.open = QtWidgets.QPushButton(self.widget)
        self.open.setGeometry(QtCore.QRect(690, 100, 75, 23))
        self.open.setObjectName("open")
        self.capature = QtWidgets.QPushButton(self.widget)
        self.capature.setGeometry(QtCore.QRect(690, 140, 75, 23))
        self.capature.setObjectName("capature")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(19, 449, 771, 451))
        self.widget_2.setObjectName("widget_2")
        self.imgLabel = QtWidgets.QLabel(self.widget_2)
        self.imgLabel.setGeometry(QtCore.QRect(50, 10, 511, 431))
        self.imgLabel.setText("")
        self.imgLabel.setObjectName("imgLabel")
        self.pushButton = QtWidgets.QPushButton(self.widget_2)
        self.pushButton.setGeometry(QtCore.QRect(670, 40, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_2.setGeometry(QtCore.QRect(670, 90, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.resultNumber = QtWidgets.QLCDNumber(self.widget_2)
        self.resultNumber.setGeometry(QtCore.QRect(620, 260, 131, 51))
        self.resultNumber.setProperty("intValue", 3)
        self.resultNumber.setObjectName("resultNumber")
        self.resultLabel = QtWidgets.QLabel(self.widget_2)
        self.resultLabel.setGeometry(QtCore.QRect(620, 220, 54, 12))
        self.resultLabel.setObjectName("resultLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 919, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.open.clicked.connect(MainWindow.openStream)
        self.capature.clicked.connect(MainWindow.snap)
        self.pushButton.clicked.connect(MainWindow.openImage)
        self.pushButton_2.clicked.connect(MainWindow.recognize)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.open.setText(_translate("MainWindow", "打开摄像头"))
        self.capature.setText(_translate("MainWindow", "拍照"))
        self.pushButton.setText(_translate("MainWindow", "选择图片"))
        self.pushButton_2.setText(_translate("MainWindow", "识别"))
        self.resultLabel.setText(_translate("MainWindow", "识别结果："))

