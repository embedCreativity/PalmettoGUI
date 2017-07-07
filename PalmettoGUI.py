#!/usr/bin/env python

import sys

from PySide.QtGui import *
import PySide.QtCore as QtCore
import QtUI
import time
from joystick import Joystick

from embedcreativity import PalmettoAPI

SlowMoRate = 0.5
TiltDefault = 750

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
        self.current = -1

        # Status variables to keep track of what we've sent the board
        self.motorPowerOn = False
        self.slowMo = True
        self.tiltDecButtonDown = False
        self.tiltIncButtonDown = False
        self.tiltPWM = TiltDefault

    def ServiceHeartBeat(self, value):

        # Get motor settings
        if self.slowMo:
            pwr = int(1000.0 * SlowMoRate * float(self.joystick.absRy[0])/float(self.joystick.absRy[2]))
        else:
            pwr = int(1000.0 * float(self.joystick.absRy[0])/float(self.joystick.absRy[2]))
        self.Send('setmotor 1 {}'.format(-1 * pwr))
        self.Send('setmotor 2 {}'.format(-1 * pwr))

        if self.slowMo:
            pwr = int(1000.0 * SlowMoRate * float(self.joystick.absY[0]) / float(self.joystick.absY[2]))
        else:
            pwr = int(1000.0 * float(self.joystick.absY[0]) / float(self.joystick.absY[2]))
        self.Send('setmotor 3 {}'.format(pwr))
        self.Send('setmotor 4 {}'.format(-1 * pwr))

        # Get LED setting
        pwr = abs(int(1000.0 * float(self.joystick.absRz[0]) / float(self.joystick.absRz[2])))
        self.Send('setled {}'.format(pwr))

        # Get Pan Servo setting
        pan= 600 + int(500 * float(self.joystick.absRx[0]) / float(self.joystick.absRx[2]))
        self.Send('setservo 1 {}'.format(pan))

        # Check Center Mode Button for Motor On/Off
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
        # Check Back Button for SlowMo
        if self.joystick.btnSelect[1]:  # new button activity (either pressed or released)
            self.joystick.btnSelect[1] = False  # reset flag
            if 1 == self.joystick.btnSelect[0]: # button pressed!
                if self.slowMo: # it's on, let's turn it off
                    self.slowMo = False
                    self.lblSlowMo.setText('SlowMo Off')
                else: # it's off, let's turn it on
                    self.slowMo = True
                    self.lblSlowMo.setText('SlowMo On')
        # Check Button B for reset Tilt Servo to center
        if self.joystick.btnB[1]:  # new button activity (either pressed or released)
            self.joystick.btnB[1] = False  # reset flag
            if 1 == self.joystick.btnB[0]: # button pressed!
                self.tiltPWM = TiltDefault
        # Check Right Trigger for Tilt Servo Down decrement
        if self.joystick.btnTR[1]:  # new button activity (either pressed or released)
            self.joystick.btnTR[1] = False  # reset flag
            if 1 == self.joystick.btnTR[0]: # button down
                self.tiltDecButtonDown = True
            else:
                self.tiltDecButtonDown = False

        # Check Left Trigger for Tilt Servo Up increment
        if self.joystick.btnTL[1]:  # new button activity (either pressed or released)
            self.joystick.btnTL[1] = False  # reset flag
            if 1 == self.joystick.btnTL[0]: # button down
                self.tiltIncButtonDown = True
            else:
                self.tiltIncButtonDown = False

        # Check if buttons are still down and continually inc/dec while they are
        if self.tiltDecButtonDown:
            if self.tiltPWM > 0:
                self.tiltPWM -= 10
        if self.tiltIncButtonDown:
            if self.tiltPWM < 1500:
                self.tiltPWM += 10

        self.Send('setservo 2 {}'.format(self.tiltPWM))
        self.heartBeat.lockHeartBeat.unlock() # allow heartbeat thread to continue

    def UpdatePower(self):
        self.lblPower.setText(str(self.sldPower.value()))

    def Send(self, cmd):
        self.ProcessResponse(self.API.send(cmd))

    def ProcessResponse(self, response):
        self.status = response[0]
        self.voltage = response[1]
        self.current = response[2]
        if -1 == self.voltage or -1 == self.current:
            self.lblVoltage.setText('?')
            self.lblCurrent.setText('?')
        else:
            self.lblVoltage.setText('{:.2f}V'.format(self.voltage))
            self.lblCurrent.setText('{:.2f}A'.format(self.current))


if __name__ == "__main__":
    gui = PalmettoGUI()
    gui.startGui()

