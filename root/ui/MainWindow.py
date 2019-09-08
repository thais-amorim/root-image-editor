from Window import Window
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5. QtGui import *
from LeftBar import LeftBar
from ImageView import ImageView
import sys


class MainWindow(Window):
    
    def __init__(self):
        super().__init__()

        self.main_layout = QHBoxLayout()
        self.left_bar = LeftBar()
        self.imageView = ImageView()
        

        self.initToolBar()
        self.initMenuBar()
        self.setLayouts()
        print("Iniciando")

    def setLayouts(self):
        self.main_layout.addWidget(self.left_bar)
        self.main_layout.addWidget(self.imageView)
        self.main_layout.setStretch(0, 40)
        self.main_layout.setStretch(1, 200)

        main_widget = QWidget()
        main_widget.setLayout(self.main_layout)
        self.setCentralWidget(main_widget)



    def initMenuBar(self):
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

    def initToolBar(self):

        openAction = QAction(QtGui.QIcon('assets/icons/open.png'),"&Abrir Ctrl+O", self)
        saveAction = QAction(QtGui.QIcon('assets/icons/save.png'),"Salvar Ctrl+S", self)
        saveAllAction = QAction(QtGui.QIcon('assets/icons/save-all.png'),"Salvar Como Ctrl+Shift+S", self)
        undoAction = QAction(QtGui.QIcon('assets/icons/undo.png'),"Desfazer Ctrl+Z", self)
        
        openAction.triggered.connect(self.fileOpen)
        saveAction.triggered.connect(self.closeApplication)
        saveAllAction.triggered.connect(self.closeApplication)
        undoAction.triggered.connect(self.closeApplication)
        
        openAction.setShortcut("Ctrl+O")
        saveAction.setShortcut("Ctrl+S")
        saveAllAction.setShortcut("Ctrl+Shift+S")
        undoAction.setShortcut("Ctrl+Z")

        self.toolbar = self.addToolBar("Extraction")
        self.toolbar.addAction(openAction)
        self.toolbar.addAction(saveAction)
        self.toolbar.addAction(saveAllAction)
        self.toolbar.addAction(undoAction)       









app = QApplication([])
GUI = MainWindow()
app.exec_()