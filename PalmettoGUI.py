#!/usr/bin/env python

import sys

from PySide.QtCore import *
from PySide.QtGui import *
import QtUI
import time

from embedcreativity import PalmettoAPI

class MainDialog(QDialog, QtUI.Ui_Dialog):

    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)
        self.setupUi(self)
        self.pbGo.clicked.connect(self.Go)
        self.pbStop.clicked.connect(self.Stop)
        self.pbRotateRight.clicked.connect(self.RotateRight)
        self.pbRotateLeft.clicked.connect(self.RotateLeft)
        self.pbBack.clicked.connect(self.Back)
        self.sldLED.valueChanged.connect(self.SetLED)
        self.sldPower.valueChanged.connect(self.UpdatePower)

        self.API = PalmettoAPI()
        self.API.send('mon')
        self.API.send('setled 3')
        self.status = -1
        self.voltage = -1



    def Go(self):
        self.Send('setmotor 1 ' + str(self.sldPower.value()))
        self.Send('setmotor 2 ' + str(self.sldPower.value()))
        self.Send('setmotor 3 ' + str(-1 * self.sldPower.value()))
        self.Send('setmotor 4 ' + str(-1 * self.sldPower.value()))
    def Stop(self):
        self.Send('setmotor 1 0')
        self.Send('setmotor 2 0')
        self.Send('setmotor 3 0')
        self.Send('setmotor 4 0')
    def Back(self):
        self.Send('setmotor 1 ' + str(-1 * self.sldPower.value()))
        self.Send('setmotor 2 ' + str(-1 * self.sldPower.value()))
        self.Send('setmotor 3 ' + str(self.sldPower.value()))
        self.Send('setmotor 4 ' + str(self.sldPower.value()))
    def RotateRight(self):
        self.Send('setmotor 1 ' + str(self.sldPower.value()))
        self.Send('setmotor 2 ' + str(self.sldPower.value()))
        self.Send('setmotor 3 ' + str(self.sldPower.value()))
        self.Send('setmotor 4 ' + str(self.sldPower.value()))
    def RotateLeft(self):
        self.Send('setmotor 1 ' + str(-1 * self.sldPower.value()))
        self.Send('setmotor 2 ' + str(-1 * self.sldPower.value()))
        self.Send('setmotor 3 ' + str(-1 * self.sldPower.value()))
        self.Send('setmotor 4 ' + str(-1 * self.sldPower.value()))
    def SetLED(self):
        self.Send('setled ' + str(self.sldLED.value()))


    def UpdatePower(self):
        self.lblPower.setText(str(self.sldPower.value()))

    def Send(self, cmd):
        self.ProcessResponse(self.API.send(cmd))

    def ProcessResponse(self, response):
        self.status = response[0]
        self.voltage = response[1]
        if -1 == self.voltage:
            self.lblVoltage.setText('?')
        else:
            self.lblVoltage.setText('{:.2f}V'.format(self.voltage))



app = QApplication(sys.argv)
form = MainDialog()
form.show()
app.exec_()