# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Calculator(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(271, 376)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 0, 241, 61))
        self.label.setObjectName("label")
        self.pushButton_clear = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_clear.setGeometry(QtCore.QRect(20, 60, 61, 61))
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.pushButton_divide = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_divide.setGeometry(QtCore.QRect(200, 60, 61, 61))
        self.pushButton_divide.setObjectName("pushButton_divide")
        self.pushButton_percentage = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_percentage.setGeometry(QtCore.QRect(140, 60, 61, 61))
        self.pushButton_percentage.setObjectName("pushButton_percentage")
        self.pushButton_plus_minus = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_plus_minus.setGeometry(QtCore.QRect(80, 60, 61, 61))
        self.pushButton_plus_minus.setObjectName("pushButton_plus_minus")
        self.pushButton_09 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_09.setGeometry(QtCore.QRect(140, 120, 61, 61))
        self.pushButton_09.setObjectName("pushButton_09")
        self.pushButton_07 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_07.setGeometry(QtCore.QRect(20, 120, 61, 61))
        self.pushButton_07.setObjectName("pushButton_07")
        self.pushButton_multiply = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_multiply.setGeometry(QtCore.QRect(200, 120, 61, 61))
        self.pushButton_multiply.setObjectName("pushButton_multiply")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(80, 120, 61, 61))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_06 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_06.setGeometry(QtCore.QRect(140, 180, 61, 61))
        self.pushButton_06.setObjectName("pushButton_06")
        self.pushButton_04 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_04.setGeometry(QtCore.QRect(20, 180, 61, 61))
        self.pushButton_04.setObjectName("pushButton_04")
        self.pushButton_minus = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_minus.setGeometry(QtCore.QRect(200, 180, 61, 61))
        self.pushButton_minus.setObjectName("pushButton_minus")
        self.pushButton_05 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_05.setGeometry(QtCore.QRect(80, 180, 61, 61))
        self.pushButton_05.setObjectName("pushButton_05")
        self.pushButton_03 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_03.setGeometry(QtCore.QRect(140, 240, 61, 61))
        self.pushButton_03.setObjectName("pushButton_03")
        self.pushButton_plus = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_plus.setGeometry(QtCore.QRect(200, 240, 61, 61))
        self.pushButton_plus.setObjectName("pushButton_plus")
        self.pushButton_02 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_02.setGeometry(QtCore.QRect(80, 240, 61, 61))
        self.pushButton_02.setObjectName("pushButton_02")
        self.pushButton_01 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_01.setGeometry(QtCore.QRect(20, 240, 61, 61))
        self.pushButton_01.setObjectName("pushButton_01")
        self.pushButton_dot = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_dot.setGeometry(QtCore.QRect(140, 300, 61, 61))
        self.pushButton_dot.setObjectName("pushButton_dot")
        self.pushButton_equals = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_equals.setGeometry(QtCore.QRect(200, 300, 61, 61))
        self.pushButton_equals.setObjectName("pushButton_equals")
        self.pushButton_0 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_0.setGeometry(QtCore.QRect(20, 300, 121, 61))
        self.pushButton_0.setObjectName("pushButton_0")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "0"))
        self.pushButton_clear.setText(_translate("MainWindow", "C"))
        self.pushButton_divide.setText(_translate("MainWindow", "/"))
        self.pushButton_percentage.setText(_translate("MainWindow", "%"))
        self.pushButton_plus_minus.setText(_translate("MainWindow", "+/-"))
        self.pushButton_09.setText(_translate("MainWindow", "9"))
        self.pushButton_07.setText(_translate("MainWindow", "7"))
        self.pushButton_multiply.setText(_translate("MainWindow", "x"))
        self.pushButton_8.setText(_translate("MainWindow", "8"))
        self.pushButton_06.setText(_translate("MainWindow", "6"))
        self.pushButton_04.setText(_translate("MainWindow", "4"))
        self.pushButton_minus.setText(_translate("MainWindow", "-"))
        self.pushButton_05.setText(_translate("MainWindow", "5"))
        self.pushButton_03.setText(_translate("MainWindow", "3"))
        self.pushButton_plus.setText(_translate("MainWindow", "+"))
        self.pushButton_02.setText(_translate("MainWindow", "2"))
        self.pushButton_01.setText(_translate("MainWindow", "1"))
        self.pushButton_dot.setText(_translate("MainWindow", "."))
        self.pushButton_equals.setText(_translate("MainWindow", "="))
        self.pushButton_0.setText(_translate("MainWindow", "0"))