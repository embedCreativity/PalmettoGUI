#!/usr/bin/env python

import sys

from PySide.QtGui import *
import PySide.QtCore as QtCore
import QtUI
import time
from joystick import Joystick

from embedcreativity import PalmettoAPI

SlowMoRate = 0.5
ledDefault = 0

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
        self.status = -1
        self.voltage = -1
        self.current = -1

        # Status variables to keep track of what we've sent the board
        self.motorPowerOn = False
        self.slowMo = True
        self.ledDecButtonDown = False
        self.ledIncButtonDown = False
        self.pwrLED = ledDefault
        # Security Cam Mode variables
        self.hatXDown = False
        self.hatYDown = False
        self.securityCamMode = False
        self.securityCamLeftPos = 650
        self.securityCamRightPos = 690
        self.securityCamDirectionIncreasing = True
        self.securityCamPositionLast = 670
        self.securityCamIncAmount = 2
        self.securityCamIncAmountMin = 1
        self.securityCamIncAmountMax = 10

    def ServiceHeartBeat(self, value):

        # Get max speed for motors
        if self.slowMo:
            maxRate = 1000.0 * SlowMoRate
        else:
            maxRate = 1000.0

        # Mix motor settings
        Ymotors = int(maxRate * float(self.joystick.absY[0]) / float(self.joystick.absY[2]))
        Xmotors = int(maxRate * float(self.joystick.absX[0]) / float(self.joystick.absX[2]))

        # First add Ymotors to both sides equally
        Rmotors = Ymotors
        Lmotors = Ymotors

        # Then split XMotors across each side (add to one side, subtract from other)
        Rmotors += Xmotors
        Lmotors -= Xmotors

        # ceiling/floor limits
        if Rmotors > maxRate:
            Rmotors = maxRate
        elif Rmotors < (-1 * maxRate):
            Rmotors = (-1 * maxRate)
        if Lmotors > maxRate:
            Lmotors = maxRate
        elif Lmotors < (-1 * maxRate):
            Lmotors = (-1 * maxRate)

        # Set Right Motors
        self.Send('setmotor 1 {}'.format(-1 * Rmotors))
        self.Send('setmotor 2 {}'.format(-1 * Rmotors))

        # Set Left Motors
        self.Send('setmotor 3 {}'.format(Lmotors))
        self.Send('setmotor 4 {}'.format(-1 * Lmotors))

        # Get Pan Servo setting
        if self.securityCamMode: # automated panning
            if self.securityCamDirectionIncreasing:
                if self.securityCamPositionLast < self.securityCamRightPos:
                    self.securityCamPositionLast += self.securityCamIncAmount
                else:
                    self.securityCamDirectionIncreasing = False # flip directions
                    self.securityCamPositionLast -= self.securityCamIncAmount
            else:
                if self.securityCamPositionLast > self.securityCamLeftPos:
                    self.securityCamPositionLast -= self.securityCamIncAmount
                else:
                    self.securityCamDirectionIncreasing = True # flip directions
                    self.securityCamPositionLast += self.securityCamIncAmount
            pan = self.securityCamPositionLast
        else: # joystick controlled
            pan = 670 + int(560.0 * float(self.joystick.absRx[0]) / float(self.joystick.absRx[2]))

        self.Send('setservo 1 {}'.format(pan))

        # Get Tilt Servo setting
        tilt = 750 + int(750.0 * float(self.joystick.absRy[0]) / float(self.joystick.absRy[2]))
        if tilt < 200: # don't allow it go too far up
            tilt = 200

        self.Send('setservo 2 {}'.format(tilt))

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
        # Toggle Security Cam Mode
        if self.joystick.btnStart[1]: # new button activity (either pressed or released)
            self.joystick.btnStart[1] = False #reset flag
            if 1 == self.joystick.btnStart[0]: # button pressed!
                if self.securityCamMode: # it's on, let's turn it off
                    self.securityCamMode = False
                    self.lblSecurityCamMode.setText('Security Cam Mode Off')
                else: # it's off, let's turn it on
                    self.securityCamMode = True
                    self.lblSecurityCamMode.setText('Security Cam Mode On')

        # Right/Left Hat buttons
        if self.joystick.absHatX[0] != 0 and self.hatXDown == False:
            self.hatXDown = True
            if self.joystick.absHatX[0] == self.joystick.absHatX[1]: # left hat button pressed
                self.securityCamLeftPos = pan # capture pan position
            else: # right hat button pressed
                self.securityCamRightPos = pan # capture pan position
        elif self.joystick.absHatX[0] == 0 and self.hatXDown == True: # button up - reset flag
            self.hatXDown = False

        # Up/Down Hat buttons
        if self.joystick.absHatY[0] != 0 and self.hatYDown == False:
            self.hatYDown = True
            if self.joystick.absHatY[0] == self.joystick.absHatY[1]: # up hat button pressed
                if  self.securityCamIncAmount < self.securityCamIncAmountMax:
                    self.securityCamIncAmount += 1
            else: # down hat button pressed
                if  self.securityCamIncAmount > self.securityCamIncAmountMin:
                    self.securityCamIncAmount -= 1
        elif self.joystick.absHatY[0] == 0 and self.hatYDown == True: # button up - reset flag
            self.hatYDown = False

        # Check Button B for reset LED to 0
        if self.joystick.btnB[1]:  # new button activity (either pressed or released)
            self.joystick.btnB[1] = False  # reset flag
            if 1 == self.joystick.btnB[0]: # button pressed!
                self.pwrLED = ledDefault
        # Check Right Trigger for LED decrement
        if self.joystick.btnTR[1]:  # new button activity (either pressed or released)
            self.joystick.btnTR[1] = False  # reset flag
            if 1 == self.joystick.btnTR[0]: # button down
                self.ledDecButtonDown = True
            else:
                self.ledDecButtonDown = False

        # Check Left Trigger for LED increment
        if self.joystick.btnTL[1]:  # new button activity (either pressed or released)
            self.joystick.btnTL[1] = False  # reset flag
            if 1 == self.joystick.btnTL[0]: # button down
                self.ledIncButtonDown = True
            else:
                self.ledIncButtonDown = False

        # Check if buttons are still down and continually inc/dec while they are
        if self.ledDecButtonDown:
            if self.pwrLED > 0:
                self.pwrLED -= 10
        if self.ledIncButtonDown:
            if self.pwrLED < 1000:
                self.pwrLED += 10
        self.Send('setled {}'.format(self.pwrLED))

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

