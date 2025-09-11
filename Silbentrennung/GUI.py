import pyqtgraph as pg
import numpy as np
import os
import sys
from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph as pg
import numpy as np
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QLabel
from PyQt6.QtWidgets import *
import argparse
import sys

files = os.listdir("./data")
x = list()
y = list()

def loadSampleText(file):
    with open('data/' + file) as f:
        lines = f.read()
        return lines



class Window(QMainWindow):
    def FileClicked(self,item):
        self.text_edit.setText(loadSampleText(item.text()))

    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQtGraph")
        self.setGeometry(100, 100, 600, 500)
        self.UiComponents()
        self.show()

    def UiComponents(self):
        widget = QWidget()
        listWidget = QListWidget()
        listWidget.setMaximumWidth(200)
        listWidget.itemClicked.connect(self.FileClicked)
        for i in range(len(files)):
            listWidget.addItem(files[i])

        self.text_edit = QTextEdit(self)
        
        layout = QGridLayout()
        widget.setLayout(layout)
        layout.addWidget(listWidget)
        layout.addWidget(self.text_edit, 0, 1, 3, 1)
        self.setCentralWidget(widget)


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
