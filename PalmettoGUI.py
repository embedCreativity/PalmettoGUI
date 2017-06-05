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

        # set up the heartbeat callback
        self.heartBeat = HeartBeat()
        self.heartBeat.heartBeat.connect(self.ServiceHeartBeat)
        self.heartBeat.start() # start the heartbeat thread!

        # set up the joystick thread
        self.lockJoystick = QtCore.QMutex()
        self.joystick = Joystick(self.lockJoystick)
        self.joystick.start()

        # This is the embedcreativity API
        self.API = PalmettoAPI()
        self.API.send('setled 3')
        self.status = -1
        self.voltage = -1

        # Status variables to keep track of what we've sent the board
        self.motorPowerOn = False

    def ServiceHeartBeat(self, value):

        pwr = int(1000.0 * float(self.joystick.absRy[0])/float(self.joystick.absRy[2]))
        self.Send('setmotor 3 {}'.format(pwr))
        self.Send('setmotor 4 {}'.format(pwr))

        pwr = -1 * int(1000.0 * float(self.joystick.absY[0]) / float(self.joystick.absY[2]))
        self.Send('setmotor 1 {}'.format(pwr))
        self.Send('setmotor 2 {}'.format(pwr))

        pwr = abs(int(1000.0 * float(self.joystick.absRz[0]) / float(self.joystick.absRz[2])))
        self.Send('setled {}'.format(pwr))

        if self.joystick.btnMode[1]: # new button activity (either pressed or released)
            self.joystick.btnMode[1] = False #reset flag
            if 1 == self.joystick.btnMode[0]: # button pressed!
                if self.motorPowerOn: # it's on, let's turn it off
                    self.motorPowerOn = False
                    self.lblMotorPower.setText('Motor Power Off')
                    self.Send('moff')
                else: # it's off, let's turn it on
                    self.motorPowerOn = True
                    self.lblMotorPower.setText('Motor Power On')
                    self.Send('mon')

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

