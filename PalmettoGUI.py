#!/usr/bin/env python

import sys

from PySide.QtCore import *
from PySide.QtGui import *
import QtUI
import time

from embedcreativityAPI import PalmettoAPI

class MainDialog(QDialog, QtUI.Ui_Dialog):

    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)
        self.setupUi(self)
        self.pbA.clicked.connect(self.changeLabel)
        self.API = PalmettoAPI()

    def changeLabel(self):
        self.lblFoo.setText("clicked!")
        self.API.send('setled 100')




app = QApplication(sys.argv)
form = MainDialog()
form.show()
app.exec_()