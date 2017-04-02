#!/usr/bin/env python

import sys

from PySide.QtCore import *
from PySide.QtGui import *
import QtUI
import time

from embedcreativity import PalmettoAPI

class MainDialog(QDialog, QtUI.Ui_Dialog):

    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)
        self.setupUi(self)
        self.pbGo.clicked.connect(self.Go)
        self.pbStop.clicked.connect(self.Stop)
        self.pbRotateRight.clicked.connect(self.RotateRight)
        self.pbRotateLeft.clicked.connect(self.RotateLeft)
        self.API = PalmettoAPI()
        self.API.send('mon')
        self.API.send('setled 100')

    def Go(self):
        self.API.send('setservo 1 0')
    def Stop(self):
        self.API.send('setservo 1 1500')
    def RotateRight(self):
        self.API.send('pivotright')
    def RotateLeft(self):
        self.API.send('pivotleft')




app = QApplication(sys.argv)
form = MainDialog()
form.show()
app.exec_()