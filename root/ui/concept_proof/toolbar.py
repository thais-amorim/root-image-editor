from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QAction, QMainWindow, QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtCore import *
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(50,50,800,600)
        self.setWindowTitle("Trabalho de PDI")

        openAction = QAction(QtGui.QIcon('assets/icons/open.png'),"&Abrir Ctrl+O", self)
        saveAction = QAction(QtGui.QIcon('assets/icons/save.png'),"Salvar Ctrl+S", self)
        saveAllAction = QAction(QtGui.QIcon('assets/icons/save-all.png'),"Salvar Como Ctrl+Shift+S", self)
        undoAction = QAction(QtGui.QIcon('assets/icons/undo.png'),"Desfazer Ctrl+Z", self)
        
        openAction.triggered.connect(self.fileOpen)
        # saveAction.triggered.connect(self.closeApplication)
        # saveAllAction.triggered.connect(self.closeApplication)
        # undoAction.triggered.connect(self.closeApplication)

        openAction.setShortcut("Ctrl+O")
        saveAction.setShortcut("Ctrl+S")
        saveAllAction.setShortcut("Ctrl+Shift+S")
        undoAction.setShortcut("Ctrl+Z")

        self.toolbar = self.addToolBar("Extraction")
        self.toolbar.addAction(openAction)
        self.toolbar.addAction(saveAction)
        self.toolbar.addAction(saveAllAction)
        self.toolbar.addAction(undoAction)


        self.home()

    def home(self):
        self.show()

    def fileOpen(self):
        name,_ = QtWidgets.QFileDialog.getOpenFileName(self,"Open File")
        file = open(name,'r')




#Para chamar a classe:
app = QApplication([])
GUI = Window()
app.exec_()