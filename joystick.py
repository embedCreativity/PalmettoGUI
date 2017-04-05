import os
import time
import pygame

pygame.display.init()
pygame.joystick.init()
pygame.joystick.Joystick(0).init()

# Prints the joystick's name
JoyName = pygame.joystick.Joystick(0).get_name()
print "Name of the joystick:"
print JoyName

pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()


# Gets the number of axes
JoyAx = pygame.joystick.Joystick(0).get_numaxes()
print "Number of axis:"


# Prints the values for axis0
while True:
    pygame.event.pump()
    os.system('clear')
    foo = ''
    for i in range(joystick.get_numaxes()):
        foo += '{:.2f} '.format(pygame.joystick.Joystick(0).get_axis(i))
    print foo
    time.sleep(0.01)
