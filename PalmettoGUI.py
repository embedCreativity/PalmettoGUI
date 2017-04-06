#!/usr/bin/env python

import sys

from PySide.QtGui import *
import PySide.QtCore as QtCore
import QtUI
import time
from joystick import Joystick

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
        self.lockHeartBeat = QtCore.QMutex()

    def run(self):
        while True:
            for i in range(100):
                # Make sure we've returned from comms before calling again
                self.lockHeartBeat.lock()
                self.heartBeat.emit(i)
                time.sleep(0.01)

class MainDialog(QDialog, QtUI.Ui_Dialog):

    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)
        self.setupUi(self)
        self.chkPower.clicked.connect(self.MotorPower)
        self.sldLED.valueChanged.connect(self.SetLED)
        self.sldPower.valueChanged.connect(self.UpdatePower)

        # set up the heartbeat callback
        self.heartBeat = HeartBeat()
        self.heartBeat.heartBeat.connect(self.ServiceHeartBeat)
        self.heartBeat.start() # start the heartbeat thread!

        print '123'
        # set up the joystick thread
        self.lockJoystick = QtCore.QMutex()
        self.joystick = Joystick(self.lockJoystick)
        self.joystick.start()

        print 'foo'
        # This is the embedcreativity API
        self.API = PalmettoAPI()
        self.API.send('setled 3')
        self.status = -1
        self.voltage = -1

        print 'bar'

        # Status variables to keep track of what we've sent the board
        self.stateGo = False
        self.stateRotateRight = False
        self.stateRotateLeft = False
        self.stateBack = False

    def SetLED(self):
        self.Send('setled ' + str(self.sldLED.value()))
    def MotorPower(self):
        if True == self.chkPower.isChecked():
            self.Send('mon')
        else:
            self.Send('moff')

    def ServiceHeartBeat(self, value):

        led = abs(int(1000.0 * float(self.joystick.absRy[0])/float(self.joystick.absRy[2])))
        self.Send('setled {}'.format(int(led)))

        if self.pbGo.isDown() != self.stateGo:
            self.stateGo = self.pbGo.isDown() # update state
            if self.pbGo.isDown():
                self.Send('setmotor 1 ' + str(self.sldPower.value()))
                self.Send('setmotor 2 ' + str(self.sldPower.value()))
                self.Send('setmotor 3 ' + str(-1 * self.sldPower.value()))
                self.Send('setmotor 4 ' + str(-1 * self.sldPower.value()))
            else:
                self.Send('setmotor 1 0')
                self.Send('setmotor 2 0')
                self.Send('setmotor 3 0')
                self.Send('setmotor 4 0')

        if self.pbBack.isDown() != self.stateBack:
            self.stateBack = self.pbBack.isDown() # update state
            if self.pbBack.isDown():
                self.Send('setmotor 1 ' + str(-1 * self.sldPower.value()))
                self.Send('setmotor 2 ' + str(-1 * self.sldPower.value()))
                self.Send('setmotor 3 ' + str(self.sldPower.value()))
                self.Send('setmotor 4 ' + str(self.sldPower.value()))
            else:
                self.Send('setmotor 1 0')
                self.Send('setmotor 2 0')
                self.Send('setmotor 3 0')
                self.Send('setmotor 4 0')

        if self.pbRotateLeft.isDown() != self.stateRotateLeft:
            self.stateRotateLeft = self.pbRotateLeft.isDown() # update state
            if self.pbRotateLeft.isDown():
                self.Send('setmotor 1 ' + str(-1 * self.sldPower.value()))
                self.Send('setmotor 2 ' + str(-1 * self.sldPower.value()))
                self.Send('setmotor 3 ' + str(-1 * self.sldPower.value()))
                self.Send('setmotor 4 ' + str(-1 * self.sldPower.value()))
            else:
                self.Send('setmotor 1 0')
                self.Send('setmotor 2 0')
                self.Send('setmotor 3 0')
                self.Send('setmotor 4 0')

        if self.pbRotateRight.isDown() != self.stateRotateRight:
            self.stateRotateRight = self.pbRotateRight.isDown() # update state
            if self.pbRotateRight.isDown():
                self.Send('setmotor 1 ' + str(self.sldPower.value()))
                self.Send('setmotor 2 ' + str(self.sldPower.value()))
                self.Send('setmotor 3 ' + str(self.sldPower.value()))
                self.Send('setmotor 4 ' + str(self.sldPower.value()))
            else:
                self.Send('setmotor 1 0')
                self.Send('setmotor 2 0')
                self.Send('setmotor 3 0')
                self.Send('setmotor 4 0')

        self.heartBeat.lockHeartBeat.unlock() # allow heartbeat thread to continue

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

