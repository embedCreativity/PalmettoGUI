#!/usr/bin/env python

from evdev import InputDevice, categorize, ecodes

dev = InputDevice('/dev/input/event7')

print 'Using {} as device!'.format(dev)

for event in dev.read_loop():
    if event.type == ecodes.EV_KEY:
        if event.code == ecodes.BTN_A:
            if event.value == 1:
                print 'BTN A down!'
            else:
                print 'BTN A up!'
        elif event.code == ecodes.BTN_B:
            if event.value == 1:
                print 'BTN B down!'
            else:
                print 'BTN B up!'
        elif event.code == ecodes.BTN_X:
            if event.value == 1:
                print 'BTN X down!'
            else:
                print 'BTN X up!'
        elif event.code == ecodes.BTN_Y:
            if event.value == 1:
                print 'BTN Y down!'
            else:
                print 'BTN Y up!'
        elif event.code == ecodes.BTN_TL:
            if event.value == 1:
                print 'BTN TL down!'
            else:
                print 'BTN TL up!'
        elif event.code == ecodes.BTN_TR:
            if event.value == 1:
                print 'BTN TR down!'
            else:
                print 'BTN TR up!'
        elif event.code == ecodes.BTN_SELECT:
            if event.value == 1:
                print 'BTN SELECT down!'
            else:
                print 'BTN SELECT up!'
        elif event.code == ecodes.BTN_START:
            if event.value == 1:
                print 'BTN START down!'
            else:
                print 'BTN START up!'
        elif event.code == ecodes.BTN_MODE:
            if event.value == 1:
                print 'BTN MODE down!'
            else:
                print 'BTN MODE up!'
        elif event.code == ecodes.BTN_THUMBL:
            if event.value == 1:
                print 'BTN THUMBL down!'
            else:
                print 'BTN THUMBL up!'
        elif event.code == ecodes.BTN_THUMBR:
            if event.value == 1:
                print 'BTN THUMBR down!'
            else:
                print 'BTN THUMBR up!'

    elif event.type == ecodes.EV_ABS:
        if event.code == ecodes.ABS_X:
            print 'ABS_X: {}'.format(event.value)
        elif event.code == ecodes.ABS_Y:
            print 'ABS_Y: {}'.format(event.value)
        elif event.code == ecodes.ABS_Z:
            print 'ABS_Z: {}'.format(event.value)
        elif event.code == ecodes.ABS_RX:
            print 'ABS_RX: {}'.format(event.value)
        elif event.code == ecodes.ABS_RY:
            print 'ABS_RY: {}'.format(event.value)
        elif event.code == ecodes.ABS_RZ:
            print 'ABS_RZ: {}'.format(event.value)
        elif event.code == ecodes.ABS_HAT0X:
            print 'ABS_HAT0X: {}'.format(event.value)
        elif event.code == ecodes.ABS_HAT0Y:
            print 'ABS_HAT0Y: {}'.format(event.value)






