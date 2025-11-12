import numpy as np
import os
import sys
import numpy as np
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QLabel
from PyQt6.QtWidgets import *
import argparse
import sys
import Silbentrennung as s

files = os.listdir("data")
x = list()
y = list()

def loadSampleText(file):
    with open('data/tasks/' + file) as f:
        lines = f.read()
        return lines


class Window(QMainWindow):
    def FileClicked(self,item):
        self.text_edit.setText(loadSampleText(item.text()))

    def seperateSillables(self):
        sepText = s.doSeperation(self.text_edit.toPlainText(), True) # Das called den tatsächlichen Algorithmus
        self.text_edit.setText(sepText)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Silbentrennung")
        self.setGeometry(100, 100, 600, 500)
        self.UiComponents()
        self.show()


    def UiComponents(self):
        widget = QWidget()

        # Beispiel Daten Widget
        listWidget = QListWidget()
        listWidget.setMaximumWidth(200)
        listWidget.itemClicked.connect(self.FileClicked)
        for i in range(len(files)):
            listWidget.addItem(files[i])

        # Text Editor
        self.text_edit = QTextEdit(self)

        # N Knopf halt, wat willste dazu sagen
        doSeperationBtn = QPushButton(text="Silben trennen", parent = self)
        doSeperationBtn.clicked.connect(self.seperateSillables)
        
        # Also Jannes ich hoffe du ließt diesen Kommentar und kriegst n Lachflash 🤓
        layout = QGridLayout()
        widget.setLayout(layout)
        layout.addWidget(listWidget)
        layout.addWidget(self.text_edit, 0, 1, 1, 1)
        layout.addWidget(doSeperationBtn, 1, 1, 1, 1)

        self.setCentralWidget(widget)


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
