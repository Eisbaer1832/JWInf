import os
import Baellebad  as b
import pyqtgraph as pg
from PyQt6.QtWidgets import QLabel
from PyQt6.QtWidgets import *
import sys
from pyqtgraph.exporters import ImageExporter
files = os.listdir("data")
x = list()
y = list()


def getData(file):
    maxValue, maxHour, maxDay, timeStamps = b.getData(file)
    x_labels = list(timeStamps.keys())
    x = list(range(len(x_labels)))
    y = list(timeStamps.values())
    return maxValue, maxHour,maxDay, x_labels, x,y


class Window(QMainWindow):
    def FileClicked(self,item):
        maxValue, maxHour, maxDay, x_labels, x, y = getData(item.text())
        self.bargraph.setOpts(x = x, height = y)
        self.resultText.setText("Die Schule braucht höchstens " + str(maxValue) + " Bälle am " + maxDay + " um " + str(maxHour) + " Uhr!")
        self.plot.getAxis('bottom').setTicks([list(zip(x, x_labels))])
        self.plot.removeItem(self.bargraph)
        self.plot.addItem(self.bargraph)
        self.plot.setBackground('w')  # white background
        self.plot.getAxis('left').setTextPen('k')  # black y-axis labels
        self.plot.getAxis('bottom').setTextPen('k')  # black x-axis labels
        self.plot.getAxis('left').setPen('k')  # black axis line
        self.plot.getAxis('bottom').setPen('k')
        #---AUTO EXPORT---
        export_dir = "exports"
        os.makedirs(export_dir, exist_ok=True)

        filename = os.path.splitext(item.text())[0] + ".png"
        export_path = os.path.join(export_dir, filename)

        exporter = ImageExporter(self.plot.plotItem)
        exporter.parameters()['width'] = 800  # adjust image resolution if you like
        exporter.export(export_path)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bällebad")
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

        self.resultText = QLabel()

        self.plot = pg.plot()

        self.bargraph = pg.BarGraphItem(x = x, height = y, width = 0.6, brush ='b')
        self.plot.addItem(self.bargraph)
        layout = QGridLayout()
        widget.setLayout(layout)
        layout.addWidget(listWidget, 0, 0)
        layout.addWidget(self.plot, 0, 1)
        layout.addWidget(self.resultText, 1, 1)
        self.setCentralWidget(widget)


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
