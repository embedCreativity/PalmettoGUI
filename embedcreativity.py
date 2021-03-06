#!/usr/bin/env python

import socket
import sys
import time

TCP_IP = '192.168.0.60'
DEFAULT_PORT = 49000
DEFAULT_MSG = 'Go'
PERIOD_BEFORE_CLOSE = 2 # seconds

class PalmettoAPI:

    def __init__(self, port=DEFAULT_PORT):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((TCP_IP, port))
        self.data = ''

    def send(self, cmd=DEFAULT_MSG):
        self.sock.send(str(cmd))
        #time.sleep(0.001)
        self.data = self.sock.recv(100)
        try:
            values = self.data.split(',')
            status = int(values[0],16)
            voltage = float(values[1])
            current = float(values[2])
            return [status, voltage, current]
        except:
            #print "ERROR: parsing response"
            return [-1,-1,-1]

    def close(self):
        self.sock.close()

if (__name__ == '__main__' ):
    if len(sys.argv) != 3:
        print "usage: " + str(sys.argv[0]) + " <port> <command>"
        quit()

    try:
        port = int(sys.argv[1])
    except:
        print "usage: " + str(sys.argv[0]) + " <port> <command>"
        quit()

    foo = PalmettoAPI(port)
    foo.send(sys.argv[2])
    time.sleep(PERIOD_BEFORE_CLOSE)
    foo.close()

