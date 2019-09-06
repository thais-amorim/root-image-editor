from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QAction, QMainWindow, QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtCore import *
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(50,50,800,600)
        self.setWindowTitle("Trabalho de PDI")
        app_icon = QtGui.QIcon()
        app_icon.addFile('assets/icons/camera-80.png',QSize(80,80))
        app_icon.addFile('assets/icons/camera-256.png',QSize(256,256))
        self.setWindowIcon(app_icon)   

        closeAction = QAction("&Exit", self)
        closeAction.setShortcut("Ctrl+Q")
        closeAction.setStatusTip("Leave The App")
        closeAction.triggered.connect(self.closeApplication)
        self.statusBar()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("File")
        editMenu = mainMenu.addMenu("Edit")
        windowMenu = mainMenu.addMenu("Window")
        helpMenu = mainMenu.addMenu("Help")
        fileMenu.addAction(closeAction)

        self.home()

    def home(self):
        # btn = QtWidgets.QPushButton("Quit", self)
        # btn.clicked.connect(self.closeApplication)
        # btn.resize(btn.minimumSizeHint())
        # btn.move(100,100)

        openAction = QAction(QtGui.QIcon('assets/icons/open.png'),"Abrir Ctrl+O", self)
        saveAction = QAction(QtGui.QIcon('assets/icons/save.png'),"Salvar Ctrl+S", self)
        saveAllAction = QAction(QtGui.QIcon('assets/icons/save-all.png'),"Salvar Como Ctrl+Shift+S", self)
        undoAction = QAction(QtGui.QIcon('assets/icons/undo.png'),"Desfazer Ctrl+Z", self)
        
        openAction.setShortcut("Ctrl+O")
        saveAction.setShortcut("Ctrl+S")
        saveAllAction.setShortcut("Ctrl+Shift+S")
        undoAction.setShortcut("Ctrl+Z")

        
        openAction.triggered.connect(self.closeApplication)
        saveAction.triggered.connect(self.closeApplication)
        saveAllAction.triggered.connect(self.closeApplication)
        undoAction.triggered.connect(self.closeApplication)


        self.toolbar = self.addToolBar("Extraction")
        self.toolbar.addAction(openAction)
        self.toolbar.addAction(saveAction)
        self.toolbar.addAction(saveAllAction)
        self.toolbar.addAction(undoAction)


        self.show()

    def closeApplication(self):
        # choice = QtWidgets.QMessagebox.question(self,"Extract!", "Get into the chopper?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        # if choice == QtWidgets.QMessageBox.Yes:
        print("Desligando....")
        sys.exit()
        # else:
        #     pass


import ctypes
myappid = u'mycompany.myproduct.subproduct.version' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

app = QApplication([])
GUI = Window()
app.exec_()