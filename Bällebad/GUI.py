import pyqtgraph as pg
import numpy as np
import os
import sys
from pyqtgraph.Qt import QtCore, QtGui
import Bällebad  as b
import pyqtgraph as pg
import numpy as np
from PyQt6 import QtWidgets
import pyqtgraph.exporters
from PyQt6.QtWidgets import QLabel
from PyQt6.QtWidgets import *
import argparse
import sys

window = pg.plot()

window.setGeometry(100, 100, 600, 500)
title = "Bällebad"
window.setWindowTitle(title)


data = b.getData()

x = list(data.keys())
y = list(data.values())

files = os.listdir("./data")

bargraph = pg.BarGraphItem(x = x, height = y, width = 0.6, brush ='w')
window.addItem(bargraph)


if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QGuiApplication.instance().exec()
