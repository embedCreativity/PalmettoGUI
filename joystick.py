#!/usr/bin/env python

from evdev import InputDevice, categorize, ecodes
import PySide.QtCore as QtCore

class Joystick( QtCore.QThread ):

    _dev = InputDevice('/dev/input/event7')
    _cap = _dev.capabilities()

    # The following values are shared with whomever is using the joystick
    btnA = 0
    btnB = 0
    btnX = 0
    btnY = 0
    btnTL = 0
    btnTR = 0
    btnSelect = 0
    btnStart = 0
    btnMode = 0
    btnThumbL = 0
    btnThumbR = 0
    absX = [0, _cap[ecodes.EV_ABS][0][1].min, _cap[ecodes.EV_ABS][0][1].max]
    absY = [0, _cap[ecodes.EV_ABS][1][1].min, _cap[ecodes.EV_ABS][1][1].max]
    absZ = [0, _cap[ecodes.EV_ABS][2][1].min, _cap[ecodes.EV_ABS][2][1].max]
    absRx = [0, _cap[ecodes.EV_ABS][3][1].min, _cap[ecodes.EV_ABS][3][1].max]
    absRy = [0, _cap[ecodes.EV_ABS][4][1].min, _cap[ecodes.EV_ABS][4][1].max]
    absRz = [0, _cap[ecodes.EV_ABS][5][1].min, _cap[ecodes.EV_ABS][5][1].max]
    absHatX = [0, _cap[ecodes.EV_ABS][6][1].min, _cap[ecodes.EV_ABS][6][1].max]
    absHatY = [0, _cap[ecodes.EV_ABS][7][1].min, _cap[ecodes.EV_ABS][7][1].max]

    def __init__(self, lock):
        QtCore.QThread.__init__(self)
        self.lock = lock
        print 'Using {} as device!'.format(self._dev)

    def run(self):
        print "thread running"
        for event in self._dev.read_loop():
            if event.type == ecodes.EV_KEY:
                if event.code == ecodes.BTN_A:
                    self.btnA = event.value
                elif event.code == ecodes.BTN_B:
                    self.btnB = event.value
                elif event.code == ecodes.BTN_X:
                    self.btnX = event.value
                elif event.code == ecodes.BTN_Y:
                    self.btnY = event.value
                elif event.code == ecodes.BTN_TL:
                    self.btnTL = event.value
                elif event.code == ecodes.BTN_TR:
                    self.btnTR = event.value
                elif event.code == ecodes.BTN_SELECT:
                    self.btnSelect = event.value
                elif event.code == ecodes.BTN_START:
                    self.btnStart = event.value
                elif event.code == ecodes.BTN_MODE:
                    self.btnMode = event.value
                elif event.code == ecodes.BTN_THUMBL:
                    self.btnThumbL = event.value
                elif event.code == ecodes.BTN_THUMBR:
                    self.btnThumbR = event.value

            elif event.type == ecodes.EV_ABS:
                if event.code == ecodes.ABS_X:
                    self.absX[0] = event.value
                elif event.code == ecodes.ABS_Y:
                    self.absY[0] = event.value
                elif event.code == ecodes.ABS_Z:
                    self.absZ[0] = event.value
                elif event.code == ecodes.ABS_RX:
                    self.absRx[0] = event.value
                elif event.code == ecodes.ABS_RY:
                    self.absRy[0] = event.value
                elif event.code == ecodes.ABS_RZ:
                    self.absRz[0] = event.value
                elif event.code == ecodes.ABS_HAT0X:
                    self.absHatX[0] = event.value
                elif event.code == ecodes.ABS_HAT0Y:
                    self.absHatY[0] = event.value











