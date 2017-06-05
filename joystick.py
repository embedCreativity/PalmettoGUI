#!/usr/bin/env python

from evdev import InputDevice, categorize, ecodes
import PySide.QtCore as QtCore

class Joystick( QtCore.QThread ):

    _dev = InputDevice('/dev/input/event7')
    _cap = _dev.capabilities()

    # The following values are shared with whomever is using the joystick
    btnA = [0, False]
    btnB = [0, False]
    btnX = [0, False]
    btnY = [0, False]
    btnTL = [0, False]
    btnTR = [0, False]
    btnSelect = [0, False]
    btnStart = [0, False]
    btnMode = [0, False]
    btnThumbL = [0, False]
    btnThumbR = [0, False]
    absX = [0, _cap[ecodes.EV_ABS][0][1].min, _cap[ecodes.EV_ABS][0][1].max]
    absY = [0, _cap[ecodes.EV_ABS][1][1].min, _cap[ecodes.EV_ABS][1][1].max]
    absZ = [0, _cap[ecodes.EV_ABS][2][1].min, _cap[ecodes.EV_ABS][2][1].max]
    absRx = [0, _cap[ecodes.EV_ABS][3][1].min, _cap[ecodes.EV_ABS][3][1].max]
    absRy = [0, _cap[ecodes.EV_ABS][4][1].min, _cap[ecodes.EV_ABS][4][1].max]
    absRz = [0, _cap[ecodes.EV_ABS][5][1].min, _cap[ecodes.EV_ABS][5][1].max]
    absHatX = [0, _cap[ecodes.EV_ABS][6][1].min, _cap[ecodes.EV_ABS][6][1].max]
    absHatY = [0, _cap[ecodes.EV_ABS][7][1].min, _cap[ecodes.EV_ABS][7][1].max]
    running = True

    def __init__(self, lock):
        QtCore.QThread.__init__(self)
        self.lock = lock
        print 'Using {} as device!'.format(self._dev)

    def run(self):
        print "thread running"
        for event in self._dev.read_loop():
            if self.running:
                if event.type == ecodes.EV_KEY:
                    if event.code == ecodes.BTN_A:
                        self.btnA[0] = event.value
                        self.btnA[1] = True
                    elif event.code == ecodes.BTN_B:
                        self.btnB[0] = event.value
                        self.btnB[1] = True
                    elif event.code == ecodes.BTN_X:
                        self.btnX[0] = event.value
                        self.btnX[1] = True
                    elif event.code == ecodes.BTN_Y:
                        self.btnY[0] = event.value
                        self.btnY[1] = True
                    elif event.code == ecodes.BTN_TL:
                        self.btnTL[0] = event.value
                        self.btnTL[1] = True
                    elif event.code == ecodes.BTN_TR:
                        self.btnTR[0] = event.value
                        self.btnTR[1] = True
                    elif event.code == ecodes.BTN_SELECT:
                        self.btnSelect[0] = event.value
                        self.btnSelect[1] = True
                    elif event.code == ecodes.BTN_START:
                        self.btnStart[0] = event.value
                        self.btnStart[1] = True
                    elif event.code == ecodes.BTN_MODE:
                        self.btnMode[0] = event.value
                        self.btnMode[1] = True
                    elif event.code == ecodes.BTN_THUMBL:
                        self.btnThumbL[0] = event.value
                        self.btnThumbL[1] = True
                    elif event.code == ecodes.BTN_THUMBR:
                        self.btnThumbR[0] = event.value
                        self.btnThumbR[1] = True

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

        print "joystick quitting..."











