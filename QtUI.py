# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt.ui'
#
# Created: Sat Apr  1 20:29:18 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.pbGo = QtGui.QPushButton(Dialog)
        self.pbGo.setGeometry(QtCore.QRect(140, 50, 99, 27))
        self.pbGo.setObjectName("pbGo")
        self.pbStop = QtGui.QPushButton(Dialog)
        self.pbStop.setGeometry(QtCore.QRect(140, 80, 99, 27))
        self.pbStop.setObjectName("pbStop")
        self.pbRotateRight = QtGui.QPushButton(Dialog)
        self.pbRotateRight.setGeometry(QtCore.QRect(250, 70, 99, 27))
        self.pbRotateRight.setObjectName("pbRotateRight")
        self.lblFoo = QtGui.QLabel(Dialog)
        self.lblFoo.setGeometry(QtCore.QRect(300, 260, 91, 17))
        self.lblFoo.setObjectName("lblFoo")
        self.pbRotateLeft = QtGui.QPushButton(Dialog)
        self.pbRotateLeft.setGeometry(QtCore.QRect(30, 70, 99, 27))
        self.pbRotateLeft.setObjectName("pbRotateLeft")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.pbGo.setText(QtGui.QApplication.translate("Dialog", "Go", None, QtGui.QApplication.UnicodeUTF8))
        self.pbStop.setText(QtGui.QApplication.translate("Dialog", "Stop", None, QtGui.QApplication.UnicodeUTF8))
        self.pbRotateRight.setText(QtGui.QApplication.translate("Dialog", "Rotate Right", None, QtGui.QApplication.UnicodeUTF8))
        self.lblFoo.setText(QtGui.QApplication.translate("Dialog", "Untouched", None, QtGui.QApplication.UnicodeUTF8))
        self.pbRotateLeft.setText(QtGui.QApplication.translate("Dialog", "Rotate Left", None, QtGui.QApplication.UnicodeUTF8))

