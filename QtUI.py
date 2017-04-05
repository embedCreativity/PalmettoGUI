# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt.ui'
#
# Created: Wed Apr  5 00:27:55 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(633, 439)
        self.pbGo = QtGui.QPushButton(Dialog)
        self.pbGo.setGeometry(QtCore.QRect(140, 60, 99, 27))
        self.pbGo.setObjectName("pbGo")
        self.pbRotateRight = QtGui.QPushButton(Dialog)
        self.pbRotateRight.setGeometry(QtCore.QRect(250, 80, 99, 27))
        self.pbRotateRight.setObjectName("pbRotateRight")
        self.lblVoltage = QtGui.QLabel(Dialog)
        self.lblVoltage.setGeometry(QtCore.QRect(570, 410, 61, 20))
        self.lblVoltage.setObjectName("lblVoltage")
        self.pbRotateLeft = QtGui.QPushButton(Dialog)
        self.pbRotateLeft.setGeometry(QtCore.QRect(30, 80, 99, 27))
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
        self.pbBack = QtGui.QPushButton(Dialog)
        self.pbBack.setGeometry(QtCore.QRect(140, 90, 99, 27))
        self.pbBack.setObjectName("pbBack")
        self.sldPower = QtGui.QSlider(Dialog)
        self.sldPower.setGeometry(QtCore.QRect(490, 220, 29, 160))
        self.sldPower.setMaximum(1000)
        self.sldPower.setOrientation(QtCore.Qt.Vertical)
        self.sldPower.setObjectName("sldPower")
        self.txtPower = QtGui.QLabel(Dialog)
        self.txtPower.setGeometry(QtCore.QRect(480, 190, 51, 20))
        self.txtPower.setObjectName("txtPower")
        self.lblPower = QtGui.QLabel(Dialog)
        self.lblPower.setGeometry(QtCore.QRect(470, 380, 68, 17))
        self.lblPower.setAlignment(QtCore.Qt.AlignCenter)
        self.lblPower.setObjectName("lblPower")
        self.chkPower = QtGui.QCheckBox(Dialog)
        self.chkPower.setGeometry(QtCore.QRect(500, 160, 121, 22))
        self.chkPower.setObjectName("chkPower")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "PalmettoControl", None, QtGui.QApplication.UnicodeUTF8))
        self.pbGo.setText(QtGui.QApplication.translate("Dialog", "Go", None, QtGui.QApplication.UnicodeUTF8))
        self.pbRotateRight.setText(QtGui.QApplication.translate("Dialog", "Rotate Right", None, QtGui.QApplication.UnicodeUTF8))
        self.lblVoltage.setText(QtGui.QApplication.translate("Dialog", "??", None, QtGui.QApplication.UnicodeUTF8))
        self.pbRotateLeft.setText(QtGui.QApplication.translate("Dialog", "Rotate Left", None, QtGui.QApplication.UnicodeUTF8))
        self.txtBattery.setText(QtGui.QApplication.translate("Dialog", "Battery:", None, QtGui.QApplication.UnicodeUTF8))
        self.txtLED.setText(QtGui.QApplication.translate("Dialog", "LED", None, QtGui.QApplication.UnicodeUTF8))
        self.pbBack.setText(QtGui.QApplication.translate("Dialog", "Back", None, QtGui.QApplication.UnicodeUTF8))
        self.txtPower.setText(QtGui.QApplication.translate("Dialog", "Power", None, QtGui.QApplication.UnicodeUTF8))
        self.lblPower.setText(QtGui.QApplication.translate("Dialog", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.chkPower.setText(QtGui.QApplication.translate("Dialog", "Motor Power", None, QtGui.QApplication.UnicodeUTF8))

