# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt.ui'
#
# Created: Sun Apr  2 07:24:09 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(634, 439)
        self.pbGo = QtGui.QPushButton(Dialog)
        self.pbGo.setGeometry(QtCore.QRect(140, 50, 99, 27))
        self.pbGo.setObjectName("pbGo")
        self.pbStop = QtGui.QPushButton(Dialog)
        self.pbStop.setGeometry(QtCore.QRect(140, 80, 99, 27))
        self.pbStop.setObjectName("pbStop")
        self.pbRotateRight = QtGui.QPushButton(Dialog)
        self.pbRotateRight.setGeometry(QtCore.QRect(250, 70, 99, 27))
        self.pbRotateRight.setObjectName("pbRotateRight")
        self.lblVoltage = QtGui.QLabel(Dialog)
        self.lblVoltage.setGeometry(QtCore.QRect(570, 410, 61, 20))
        self.lblVoltage.setObjectName("lblVoltage")
        self.pbRotateLeft = QtGui.QPushButton(Dialog)
        self.pbRotateLeft.setGeometry(QtCore.QRect(30, 70, 99, 27))
        self.pbRotateLeft.setObjectName("pbRotateLeft")
        self.txtBattery = QtGui.QLabel(Dialog)
        self.txtBattery.setGeometry(QtCore.QRect(510, 410, 61, 17))
        self.txtBattery.setObjectName("txtBattery")
        self.sldLED = QtGui.QSlider(Dialog)
        self.sldLED.setGeometry(QtCore.QRect(550, 220, 29, 160))
        self.sldLED.setMaximum(1000)
        self.sldLED.setOrientation(QtCore.Qt.Vertical)
        self.sldLED.setObjectName("sldLED")
        self.txtLED = QtGui.QLabel(Dialog)
        self.txtLED.setGeometry(QtCore.QRect(550, 190, 31, 20))
        self.txtLED.setObjectName("txtLED")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.pbGo.setText(QtGui.QApplication.translate("Dialog", "Go", None, QtGui.QApplication.UnicodeUTF8))
        self.pbStop.setText(QtGui.QApplication.translate("Dialog", "Stop", None, QtGui.QApplication.UnicodeUTF8))
        self.pbRotateRight.setText(QtGui.QApplication.translate("Dialog", "Rotate Right", None, QtGui.QApplication.UnicodeUTF8))
        self.lblVoltage.setText(QtGui.QApplication.translate("Dialog", "??", None, QtGui.QApplication.UnicodeUTF8))
        self.pbRotateLeft.setText(QtGui.QApplication.translate("Dialog", "Rotate Left", None, QtGui.QApplication.UnicodeUTF8))
        self.txtBattery.setText(QtGui.QApplication.translate("Dialog", "Battery:", None, QtGui.QApplication.UnicodeUTF8))
        self.txtLED.setText(QtGui.QApplication.translate("Dialog", "LED", None, QtGui.QApplication.UnicodeUTF8))

