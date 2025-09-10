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

files = os.listdir("./data")
x = list()
y = list()


def getData(file):
    data = b.getData(file)
    x = list(data.keys())
    y = list(data.values())
    return(x,y )

x,y = getData("ball00.txt")




class Window(QMainWindow):
    def FileClicked(self,item):
        x,y = getData(item.text())
        self.bargraph.setOpts(x = x, height = y)

        self.plot.removeItem(self.bargraph)
        self.plot.addItem(self.bargraph)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQtGraph")
        self.setGeometry(100, 100, 600, 500)
        self.UiComponents()
        self.show()

    def UiComponents(self):
        widget = QWidget()
        listWidget = QListWidget()
        listWidget.setMaximumWidth(300)
        listWidget.itemClicked.connect(self.FileClicked)
        for i in range(len(files)):
            listWidget.addItem(files[i])
        

        self.plot = pg.plot()

        self.bargraph = pg.BarGraphItem(x = x, height = y, width = 0.6, brush ='g')
        self.plot.addItem(self.bargraph)
        layout = QGridLayout()
        widget.setLayout(layout)
        layout.addWidget(listWidget)
        layout.addWidget(self.plot, 0, 1, 3, 1)
        self.setCentralWidget(widget)


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
