# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt.ui'
#
# Created: Thu Apr  6 12:50:31 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(328, 78)
        self.lblVoltage = QtGui.QLabel(Dialog)
        self.lblVoltage.setGeometry(QtCore.QRect(80, 40, 61, 20))
        self.lblVoltage.setObjectName("lblVoltage")
        self.txtBattery = QtGui.QLabel(Dialog)
        self.txtBattery.setGeometry(QtCore.QRect(20, 40, 61, 17))
        self.txtBattery.setObjectName("txtBattery")
        self.chkPower = QtGui.QCheckBox(Dialog)
        self.chkPower.setGeometry(QtCore.QRect(10, 10, 121, 22))
        self.chkPower.setObjectName("chkPower")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "PalmettoControl", None, QtGui.QApplication.UnicodeUTF8))
        self.lblVoltage.setText(QtGui.QApplication.translate("Dialog", "??", None, QtGui.QApplication.UnicodeUTF8))
        self.txtBattery.setText(QtGui.QApplication.translate("Dialog", "Battery:", None, QtGui.QApplication.UnicodeUTF8))
        self.chkPower.setText(QtGui.QApplication.translate("Dialog", "Motor Power", None, QtGui.QApplication.UnicodeUTF8))

