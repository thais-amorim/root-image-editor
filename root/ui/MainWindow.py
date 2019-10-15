from Window import Window
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5. QtGui import *
from SideBar import SideBar
from ImageView import ImageView
from FourierModal import FourierModal
import sys
import numpy as np
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
        
        
        #chroma key menu
        chromaKeyAction = QAction("&Aplicar Chroma",self)
        chromaKeyAction.triggered.connect(self.chroma_key)

        chromaKeyMenu.addAction(chromaKeyAction)

        #colormode
        rgbAction = QAction("&RGB",self)
        
        grayScaleAction = QAction("&Escala de Cinza",self)
        grayScaleAction.triggered.connect(self.rgb_to_gray)
        hsvAction = QAction("&HSV",self)
        hsvAction.triggered.connect(self.rgb_to_hsv)

        colorModeMenu.addAction(grayScaleAction)
        colorModeMenu.addAction(rgbAction)
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
        sobelFilterAction.triggered.connect(self.sobel_filtering)
        gradientFilterAction = QAction("&Gradient Detecção", self)
        gradientFilterAction.triggered.connect(self.gradient_filtering)
        genericConvolutionFilterAction = QAction("&Genérico por Convolução", self)
        genericConvolutionFilterAction.triggered.connect(self.generic_convolution)
        medianFilterAction = QAction("&Filtragem por Mediana", self)
        medianFilterAction.triggered.connect(self.median_filter)
        meanFilterAction = QAction("&Suaviazação por Média", self)
        meanFilterAction.triggered.connect(self.mean_filtering)
        gaussianFilterAction = QAction("&Suavização Gaussiana", self)   
        sharpFilterAction = QAction("&Aguçamento",self)
        sepiaFilterAction = QAction("&Sepia",self)
        sepiaFilterAction.triggered.connect(self.sepia_filter)
       
        geometricFilterAction = QAction("&Média Geométrica", self)
        geometricFilterAction.triggered.connect(self.geometric_filtering)

        #filters/sharp
        laplaceFilterAction = QAction("&Laplaciano", self)
        highBoostFilterAction = QAction("&HighBoost", self)
        highBoostFilterAction.triggered.connect(self.hi_boost_filtering)
        ##add filters
        filtersMenu.addAction(genericConvolutionFilterAction)
        filtersMenu.addAction(medianFilterAction)
        filtersMenu.addSeparator()
        filtersMenu.addAction(meanFilterAction)
        filtersMenu.addAction(gaussianFilterAction)
        filtersMenu.addSeparator()
        filtersMenu.addAction(sobelFilterAction)
        filtersMenu.addAction(gradientFilterAction)
        filtersMenu.addAction(laplaceFilterAction)
        filtersMenu.addAction (geometricFilterAction)
        filtersMenu.addAction(sepiaFilterAction)
        ##add filters/sharp   
        sharpFilterMenu = filtersMenu.addMenu("Aguçamento")
        sharpFilterMenu.addAction(gaussianFilterAction)
        sharpFilterMenu.addAction(highBoostFilterAction)

        #filtros na frequência
        spectrumFilterAction = QAction("&Espectro da Transformada de Fourier", self)
        spectrumFilterAction.triggered.connect(self.fourier_spectrum)
        radialFilterAction = QAction("&Filtros Radiais(Passa alta, baixa ou faixa)", self)
        
        harmonicFilterAction = QAction("&Média Harmônica", self)
        harmonicFilterAction.triggered.connect(self.harmonic_filtering)
        counterharmonicFilterAction = QAction("&Média Contra-harmônica", self)
        counterharmonicFilterAction.triggered.connect(self.contra_harmonic_filtering)

        frequenceFiltersMenu.addAction (spectrumFilterAction)
        frequenceFiltersMenu.addSeparator()
        frequenceFiltersMenu.addAction (radialFilterAction)
        frequenceFiltersMenu.addSeparator()
        
        frequenceFiltersMenu.addAction (harmonicFilterAction)
        frequenceFiltersMenu.addAction (counterharmonicFilterAction)

    
        #histogram Menu
        equalizationAction = QAction("&Equalização por Histograma", self)
        equalizationAction.triggered.connect(self.histEqualize)

        showHistogramAction = QAction("&Ver Histograma", self)


        histogramMenu.addAction(equalizationAction)
        histogramMenu.addAction(showHistogramAction)


    def initToolBar(self):

        openAction = QAction(QtGui.QIcon('assets/icons/open.png'),"&Abrir Ctrl+O", self)
        saveAction = QAction(QtGui.QIcon('assets/icons/save.png'),"Salvar Ctrl+S", self)
        saveAllAction = QAction(QtGui.QIcon('assets/icons/save-as.png'),"Salvar Como Ctrl+Shift+S", self)
        undoAction = QAction(QtGui.QIcon('assets/icons/undo.png'),"Desfazer Ctrl+Z", self)
        redoAction = QAction(QtGui.QIcon('assets/icons/redo.png'),"Desfazer Ctrl+R", self)
        brushAction = QAction(QtGui.QIcon('assets/icons/brush.png'),"Pincel", self)

        openAction.setShortcut("Ctrl+O")
        saveAction.setShortcut("Ctrl+S")
        saveAllAction.setShortcut("Ctrl+Shift+S")
        undoAction.setShortcut(QtGui.QKeySequence("Ctrl+Z"))
        redoAction.setShortcut(QtGui.QKeySequence("Ctrl+Y"))

        openAction.triggered.connect(self.fileOpen)
        # saveAction.triggered.connect(self.closeApplication)
        # saveAllAction.triggered.connect(self.closeApplication)
        undoAction.triggered.connect(self.undoLastAction)
        redoAction.triggered.connect(self.redoLastAction)


        self.toolbar = self.addToolBar("Extraction")
        
        self.toolbar.addAction(openAction)
        self.toolbar.addAction(saveAction)
        self.toolbar.addAction(saveAllAction)
        self.toolbar.addAction(undoAction)  
        self.toolbar.addAction(redoAction) 
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
    
    def median_filter(self):
        size, ok = QInputDialog.getText(self, 'Filtragem por Median', 
            'Entre com o tamanho do filtro: (deve ser maior que 0)')
        if ok:
            self.loadImage(self.transformController.apply_median(int(size)))

    def histEqualize(self):
        self.loadImage(self.transformController.apply_equalized_histogram())

    def generic_convolution(self):
        try:
            self.loadImage(self.transformController.apply_convolution(self.getMatrixInput()))
        except:
            print("Ocorreu um erro")

    def sobel_filtering(self):
        self.loadImage(self.transformController.apply_sobel())

    def getMatrixInput(self):
        dialog = MatrixDialog()
        if dialog.exec():
            print(dialog.getInputs())
            gamma = dialog.getInputs()
        lines = gamma.split("\n")
        table = []
        i = 0
        for l in lines:
            table.append([])
            table[i] = l.split(' ')
            i = i+1
        try:
            table = np.array(table)
            table = np.float_(table)
            return table
        except:
            return None
     
    def gradient_filtering(self):
        try:
            self.loadImage(self.transformController.apply_gradient(self.getMatrixInput()))
        except:
            print("Ocorreu um erro")
    
    def mean_filtering(self):
        size, ok = QInputDialog.getText(self, 'Filtro por Média Aritimética', 
            'Entre com o tamanho do filtro: (deve ser maior que 0)')
        if ok:
            self.loadImage(self.transformController.apply_arithmetic_mean(int(size)))
    
    def geometric_filtering(self):
        size, ok = QInputDialog.getText(self, 'Filtro por Média Geométrica', 
            'Entre com o tamanho do filtro: (deve ser maior que 0)')
        if ok:
            self.loadImage(self.transformController.apply_geometric_mean(int(size)))

    def harmonic_filtering(self):
        size, ok = QInputDialog.getText(self, 'Filtro por Média Harmônica', 
            'Entre com o tamanho do filtro: (deve ser maior que 0)')
        if ok:
            self.loadImage(self.transformController.apply_harmonic_mean(int(size)))

    def contra_harmonic_filtering(self):
        size, ok = QInputDialog.getText(self, 'Filtro por Média Contra Harmônica', 
            'Entre com o tamanho do filtro: (deve ser maior que 0)')
        if ok:
            q, ok = QInputDialog.getText(self, 'Filtro por Média Harmônica', 
            'Entre com o valor de q')
            if ok:
                self.loadImage(self.transformController.apply_contra_harmonic_mean(int(size),float(q)))
    
    def hi_boost_filtering(self):
        size, ok = QInputDialog.getText(self, 'Filtro por Hi Boost', 
            'Entre com o tamanho do filtro: (deve ser maior que 0)')
        if ok:
            c, ok = QInputDialog.getText(self, 'Filtro por Média Harmônica', 
            'Entre com o valor de c')
            if ok:
                self.loadImage(self.transformController.apply_highboost(int(size),float(c)))
    
    def fourier_spectrum(self):
        # mag = self.transformController.apply_fourier()
        # mag = mag.astype(np.uint8)
        # print("Shape da Magnitude")
        # print(mag.shape)
        # print("strides")
        # print(mag.strides[0])
        # print(mag.shape[0])
        # print(mag.shape[1])
        # print(mag.data)


        # print("IM:")
        # im = self.transformController.current_image
        # print(im.shape)
        # print(im)
        # print("im data")
        # print(im.strides[0])
        # print(im.shape[0])
        # print(im.shape[1])
        # print(im.data)
        w = FourierModal(self.transformController)
        if w.exec_():
            self.loadImage(self.transformController.apply_inverse_fourier())
            print("Success!")
        else:
            print("Cancel!")



        # self.side_bar.loadImage(name)
    def rgb_to_gray(self):
        self.loadImage(self.transformController.rgb_to_gray())
    
    def rgb_to_hsv(self):
        self.loadImage(self.transformController.rgb_to_hsv())

    def sepia_filter(self):
        self.loadImage(self.transformController.apply_sepia())

    def chroma_key(self):
        # try:
            name,_ = QtWidgets.QFileDialog.getOpenFileName(self,"Escolha o fundo da chroma key")
            if name:
                background = self.transformController.openImage(name)
                self.loadImage(self.transformController.apply_chroma_key(background))
        # except:
        #     print("Ocorreu um erro")

class MatrixDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.matrix = QPlainTextEdit(self)
        # self.second = QLineEdit(self)
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)

        layout = QFormLayout(self)
        layout.addRow("Escreva a matriz", self.matrix)
        # layout.addRow("Second text", self.second)
        layout.addWidget(buttonBox)

        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

    def getInputs(self):
        return (self.matrix.toPlainText())