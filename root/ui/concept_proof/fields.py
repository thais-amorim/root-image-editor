from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QAction, QMainWindow, QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtCore import *
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(50,50,800,600)
        self.setWindowTitle("Trabalho de PDI")

        self.home()

    def home(self):
        checkBox = QtWidgets.QCheckBox("PP - Enlarge Window", self)
        checkBox.move(100,100)
        checkBox.stateChanged.connect(self.enlargeWindow)

        self.progress = QtWidgets.QProgressBar(self)
        self.progress.setGeometry(200,80,250,20)


        btn = QtWidgets.QPushButton("Action", self)
        btn.move(120,120)
        btn.clicked.connect(self.actionProgress)

        self.show()



    def actionProgress(self):
        self.completed = 0
        
        while self.completed < 100:
            self.completed += 0.00001
            self.progress.setValue(self.completed)

    def enlargeWindow(self, state):
        if state == Qt.Checked:
            self.setGeometry(50,50,1000,600)
        else:
            self.setGeometry(50,50,500,300)

    def closeApplication(self):
        # choice = QtWidgets.QMessagebox.question(self,"Extract!", "Get into the chopper?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        # if choice == QtWidgets.QMessageBox.Yes:
        print("Desligando....")
        sys.exit()
        # else:
        #     pass


app = QApplication([])
GUI = Window()
app.exec_()