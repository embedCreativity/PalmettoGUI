# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt.ui'
#
# Created: Wed Oct 11 11:16:00 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(369, 152)
        self.lblVoltage = QtGui.QLabel(Dialog)
        self.lblVoltage.setGeometry(QtCore.QRect(80, 80, 61, 20))
        self.lblVoltage.setObjectName("lblVoltage")
        self.txtBattery = QtGui.QLabel(Dialog)
        self.txtBattery.setGeometry(QtCore.QRect(20, 80, 61, 17))
        self.txtBattery.setObjectName("txtBattery")
        self.lblMotorPower = QtGui.QLabel(Dialog)
        self.lblMotorPower.setGeometry(QtCore.QRect(20, 40, 131, 17))
        self.lblMotorPower.setObjectName("lblMotorPower")
        self.txtCurrent = QtGui.QLabel(Dialog)
        self.txtCurrent.setGeometry(QtCore.QRect(20, 100, 68, 17))
        self.txtCurrent.setObjectName("txtCurrent")
        self.lblCurrent = QtGui.QLabel(Dialog)
        self.lblCurrent.setGeometry(QtCore.QRect(80, 100, 68, 17))
        self.lblCurrent.setObjectName("lblCurrent")
        self.lblSecurityCamMode = QtGui.QLabel(Dialog)
        self.lblSecurityCamMode.setGeometry(QtCore.QRect(20, 20, 171, 17))
        self.lblSecurityCamMode.setObjectName("lblSecurityCamMode")
        self.lblChargerDoor = QtGui.QLabel(Dialog)
        self.lblChargerDoor.setGeometry(QtCore.QRect(20, 60, 151, 17))
        self.lblChargerDoor.setObjectName("lblChargerDoor")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "PalmettoControl", None, QtGui.QApplication.UnicodeUTF8))
        self.lblVoltage.setText(QtGui.QApplication.translate("Dialog", "??", None, QtGui.QApplication.UnicodeUTF8))
        self.txtBattery.setText(QtGui.QApplication.translate("Dialog", "Battery:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblMotorPower.setText(QtGui.QApplication.translate("Dialog", "Motor Power Off", None, QtGui.QApplication.UnicodeUTF8))
        self.txtCurrent.setText(QtGui.QApplication.translate("Dialog", "Current:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblCurrent.setText(QtGui.QApplication.translate("Dialog", "??", None, QtGui.QApplication.UnicodeUTF8))
        self.lblSecurityCamMode.setText(QtGui.QApplication.translate("Dialog", "Security Cam Mode Off", None, QtGui.QApplication.UnicodeUTF8))
        self.lblChargerDoor.setText(QtGui.QApplication.translate("Dialog", "Charger Door Closed", None, QtGui.QApplication.UnicodeUTF8))

