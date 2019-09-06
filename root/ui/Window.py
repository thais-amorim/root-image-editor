from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(50,50,800,600)
        self.setWindowTitle("Trabalho de PDI")
        self.setWindowIcon(QtGui.QIcon('assets/icons/app.ico'))   
        
        extractAction = QAction("&Exit", self)
        extractAction.setShortcut("Ctrl+Q")
        extractAction.setStatusTip("Leave The App")
        extractAction.triggered.connect(self.closeApplication)
        self.statusBar()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("File")
        fileMenu.addAction(extractAction)

        self.home()

    def home(self):
        # btn = QtWidgets.QPushButton("Quit", self)
        # btn.clicked.connect(self.closeApplication)
        # btn.resize(btn.minimumSizeHint())
        # btn.move(100,100)
        self.show()

    def closeApplication(self):
        print("Desligando...")
        sys.exit()

app = QApplication([])
GUI = Window()
app.exec_()