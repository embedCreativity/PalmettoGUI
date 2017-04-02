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
        self.sldLED.valueChanged.connect(self.SetLED)

        self.API = PalmettoAPI()
        self.API.send('mon')
        self.API.send('setled 3')
        self.status = -1
        self.voltage = -1



    def Go(self):
        self.Send('setservo 1 0')
    def Stop(self):
        self.Send('setservo 1 1500')
    def RotateRight(self):
        self.Send('pivotright')
    def RotateLeft(self):
        self.Send('pivotleft')
    def SetLED(self):
        self.Send('setled ' + str(self.sldLED.value()))



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