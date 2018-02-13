# PalmettoGUI

This Pyside (Python + Qt) script is designed to run in a Linux environment, as it is easier to access joystick devices this way. To use, make sure that the InputDevice line (~ln 8) in joystick.py points to the joystick associated with your machine. You can identify this by executing 'dmesg | tail' after plugging in your joystick. You will also be able to see it appear in '/dev/input'.

Start the program with './PalmettoGUI.py'.
