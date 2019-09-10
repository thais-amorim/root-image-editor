from Window import Window
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5. QtGui import *
from SideBar import SideBar
from ImageView import ImageView
import sys
# sys.path.append('../controllers')




class MainWindow(Window):
    
    def __init__(self):
        super().__init__()
        
        self.main_layout = QHBoxLayout()
        self.initToolBar()
        self.initMenuBar()
        self.setLayouts()

        

        print("Iniciando")

    def setLayouts(self):
        
        self.main_layout.addWidget(self.imageView)
        self.main_layout.addWidget(self.side_bar)
        self.main_layout.setStretch(0, 40)
        # self.main_layout.setStretch(1, 200)


        main_widget = QWidget()
        main_widget.setObjectName("main-widget")
        main_widget.setLayout(self.main_layout)
        main_widget.setStyleSheet("QWidget#main-widget{ border:2px solid rgb(150,150, 150);} ")
        self.setCentralWidget(main_widget)

    def initMenuBar(self):
        closeAction = QAction("&Exit", self)
        closeAction.setShortcut("Ctrl+Q")
        closeAction.setStatusTip("Leave The App")
        closeAction.triggered.connect(self.closeApplication)


        negativeFilterAction = QAction("&Negative", self)
        negativeFilterAction.triggered.connect(self.negative_transform)

        logFilterAction = QAction("&Logarithmic", self)
        logFilterAction .triggered.connect(self.logarithmic_transform)

        gammaFilterAction = QAction("&Gamma", self)
        gammaFilterAction .triggered.connect(self.gamma_transform)

        gaussianFilterAction = QAction("&Gaussian", self)
        
        laplaceFilterAction = QAction("&Laplace", self)
        sobelFilterAction = QAction("&Sobel", self)

        self.statusBar()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("File")
        imageMenu = mainMenu.addMenu("Image")
        transformMenu = imageMenu.addMenu("GrayScale Transformations")
        filtersMenu = imageMenu.addMenu("Filters")
        
        windowMenu = mainMenu.addMenu("Window")
        helpMenu = mainMenu.addMenu("Help")
        
        fileMenu.addAction(closeAction)

        transformMenu.addAction(negativeFilterAction)
        transformMenu.addAction(logFilterAction)
        transformMenu.addAction(gammaFilterAction)

        filtersMenu.addAction(gaussianFilterAction)
        
        filtersMenu.addAction(laplaceFilterAction)
        filtersMenu.addAction(sobelFilterAction)

    def initToolBar(self):

        openAction = QAction(QtGui.QIcon('assets/icons/open.png'),"&Abrir Ctrl+O", self)
        saveAction = QAction(QtGui.QIcon('assets/icons/save.png'),"Salvar Ctrl+S", self)
        saveAllAction = QAction(QtGui.QIcon('assets/icons/save-as.png'),"Salvar Como Ctrl+Shift+S", self)
        undoAction = QAction(QtGui.QIcon('assets/icons/undo.png'),"Desfazer Ctrl+Z", self)
        brushAction = QAction(QtGui.QIcon('assets/icons/brush.png'),"Pincel", self)

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
        self.toolbar.addSeparator()
        self.toolbar.addSeparator()     
        self.toolbar.addAction(brushAction)       


    def negative_transform(self):
        self.loadImage(self.transformController.negativeTransform())
      
    def logarithmic_transform(self):
        self.loadImage(self.transformController.logarithmicTransform())

    def gamma_transform(self):
        self.loadImage(self.transformController.gammaTransform(0.3))


    def fileOpen(self):
        name,_ = QtWidgets.QFileDialog.getOpenFileName(self,"Open File")
        self.setWindowTitle(name)
        self.transformController.loadImage(name)
        self.openImage(self.transformController.getCurrentImage())

    def openImage(self,name):
        self.imageView.loadImage(name)
        self.side_bar.loadImage(name)
        
    def loadImage(self,name):
        self.imageView.loadImage(name)
        # self.side_bar.loadImage(name)



app = QApplication([])
GUI = MainWindow()
app.exec_()