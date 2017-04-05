#!/usr/bin/env python

import sys

from PySide.QtGui import *
import PySide.QtCore as QtCore
import QtUI
import time
#import threading

from embedcreativity import PalmettoAPI

class PalmettoGUI():
    def __init__(self):
        # Set up and start the GUI
        self.GUI = QApplication(sys.argv)
        self.form = MainDialog()
        self.form.show()

    def startGui(self):
        self.GUI.exec_()

class HeartBeat( QtCore.QThread ):

    heartBeat = QtCore.Signal(int)

    def __init__(self):
        QtCore.QThread.__init__(self)

    def run(self):
        while True:
            for i in range(100):
                self.heartBeat.emit(i)
                time.sleep(0.1)

class MainDialog(QDialog, QtUI.Ui_Dialog):

    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)
        self.setupUi(self)
        self.pbGo.clicked.connect(self.Go)
        self.pbStop.clicked.connect(self.Stop)
        self.pbRotateRight.clicked.connect(self.RotateRight)
        self.pbRotateLeft.clicked.connect(self.RotateLeft)
        self.pbBack.clicked.connect(self.Back)
        self.chkPower.clicked.connect(self.MotorPower)
        self.sldLED.valueChanged.connect(self.SetLED)
        self.sldPower.valueChanged.connect(self.UpdatePower)

        self.heartBeat = HeartBeat()
        self.heartBeat.heartBeat.connect(self.UpdateProgressBar)
        self.heartBeat.start()

        self.API = PalmettoAPI()
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
    def MotorPower(self):
        if True == self.chkPower.isChecked():
            self.Send('mon')
        else:
            self.Send('moff')

    def UpdateProgressBar(self, value):
        self.progressBar.setValue(value)

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


if __name__ == "__main__":
    gui = PalmettoGUI()
    gui.startGui()

