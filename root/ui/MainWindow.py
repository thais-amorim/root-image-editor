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


        self.statusBar()

        #menu
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("File")
        imageMenu = mainMenu.addMenu("Image")
        windowMenu = mainMenu.addMenu("Window")
        helpMenu = mainMenu.addMenu("Help")

        #fileMenu
        closeAction = QAction("&Exit", self)
        closeAction.setShortcut("Ctrl+Q")
        closeAction.setStatusTip("Leave The App")
        closeAction.triggered.connect(self.closeApplication)

        fileMenu.addAction(closeAction)

        
   

        #imagemenu
        colorModeMenu = imageMenu.addMenu("Modos de Cor")
        imageMenu.addSeparator()
        transformMenu = imageMenu.addMenu("Transformações")
        imageMenu.addSeparator()
        filtersMenu = imageMenu.addMenu("Filters")
        frequenceFiltersMenu = imageMenu.addMenu("Filtro no Domínio da Frequência")
        imageMenu.addSeparator()
        histogramMenu = imageMenu.addMenu("Histogram")
        imageMenu.addSeparator()
        stegranographyMenu = imageMenu.addMenu("Esteganografia")
        imageMenu.addSeparator()
        chromaKeyMenu = imageMenu.addMenu("Chroma Key")
        
        




        #colormode
        rgbAction = QAction("&RGB",self)
        grayScaleAction = QAction("&Escala de Cinza",self)
        hsvAction = QAction("&HSV",self)

        colorModeMenu.addAction(rgbAction)
        colorModeMenu.addAction(grayScaleAction)
        colorModeMenu.addAction(hsvAction)


        #transformations
        negativeFilterAction = QAction("&Negative", self)
        negativeFilterAction.triggered.connect(self.negative_transform)

        logFilterAction = QAction("&Logarithmic", self)
        logFilterAction .triggered.connect(self.logarithmic_transform)

        gammaFilterAction = QAction("&Gamma", self)
        gammaFilterAction.triggered.connect(self.gamma_transform)

        transformMenu.addAction(negativeFilterAction)
        transformMenu.addAction(logFilterAction)
        transformMenu.addAction(gammaFilterAction)

        #filters
        sobelFilterAction = QAction("&Sobel", self)
        genericConvolutionFilterAction = QAction("&Genérico por Convolução", self)
        medianFilterAction = QAction("&Filtragem por Mediana", self)
        meanFilterAction = QAction("&Suaviazação por Média", self)
        gaussianFilterAction = QAction("&Suavização Gaussiana", self)   
        sharpFilterAction = QAction("&Aguçamento",self)
       
        #filters/sharp
        laplaceFilterAction = QAction("&Laplaciano", self)
        highBoostFilterAction = QAction("&HighBoost", self)
        ##add filters
        filtersMenu.addAction(genericConvolutionFilterAction)
        filtersMenu.addAction(medianFilterAction)
        filtersMenu.addSeparator()
        filtersMenu.addAction(meanFilterAction)
        filtersMenu.addAction(gaussianFilterAction)
        filtersMenu.addSeparator()
        filtersMenu.addAction(sobelFilterAction)
        filtersMenu.addAction(laplaceFilterAction)
        
        ##add filters/sharp   
        sharpFilterMenu = filtersMenu.addMenu("Aguçamento")
        sharpFilterMenu.addAction(gaussianFilterAction)
        sharpFilterMenu.addAction(highBoostFilterAction)

        #filtros na frequência
        spectrumFilterAction = QAction("&Espectro da Transformada de Fourier", self)
        radialFilterAction = QAction("&Filtros Radiais(Passa alta, baixa ou faixa)", self)
        geometricFilterAction = QAction("&Média Geométrica", self)
        harmonicFilterAction = QAction("&Média Harmônica", self)
        counterharmonicFilterAction = QAction("&Média Contra-harmônica", self)

        frequenceFiltersMenu.addAction (spectrumFilterAction)
        frequenceFiltersMenu.addSeparator()
        frequenceFiltersMenu.addAction (radialFilterAction)
        frequenceFiltersMenu.addSeparator()
        frequenceFiltersMenu.addAction (geometricFilterAction)
        frequenceFiltersMenu.addAction (harmonicFilterAction)
        frequenceFiltersMenu.addAction (counterharmonicFilterAction)




    def initToolBar(self):

        openAction = QAction(QtGui.QIcon('assets/icons/open.png'),"&Abrir Ctrl+O", self)
        saveAction = QAction(QtGui.QIcon('assets/icons/save.png'),"Salvar Ctrl+S", self)
        saveAllAction = QAction(QtGui.QIcon('assets/icons/save-as.png'),"Salvar Como Ctrl+Shift+S", self)
        undoAction = QAction(QtGui.QIcon('assets/icons/undo.png'),"Desfazer Ctrl+Z", self)
        brushAction = QAction(QtGui.QIcon('assets/icons/brush.png'),"Pincel", self)

        openAction.setShortcut("Ctrl+O")
        saveAction.setShortcut("Ctrl+S")
        saveAllAction.setShortcut("Ctrl+Shift+S")
        undoAction.setShortcut(QtGui.QKeySequence("Ctrl+Z"))

        openAction.triggered.connect(self.fileOpen)
        # saveAction.triggered.connect(self.closeApplication)
        # saveAllAction.triggered.connect(self.closeApplication)
        undoAction.triggered.connect(self.undoLastAction)
        


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

        gamma, ok = QInputDialog.getText(self, 'Gamma Correction', 
            'Enter gamma value (real):')
        
        if ok:
           self.loadImage(self.transformController.gammaTransform(float(gamma)))

    def undoLastAction(self):
        self.loadImage(self.transformController.undoAction())


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



