from root.ui import Window
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5. QtGui import *
from root.ui import SideBar
from root.ui import ImageView
from root.ui import FourierModal
import sys
import numpy as np


class MainWindow(Window):

    def __init__(self):
        super().__init__()

        self.main_layout = QHBoxLayout()
        self.initToolBar()
        self.initMenuBar()
        self.setLayouts()

    def setLayouts(self):

        self.main_layout.addWidget(self.imageView)
        self.main_layout.addWidget(self.side_bar)
        self.main_layout.setStretch(0, 40)

        main_widget = QWidget()
        main_widget.setObjectName("main-widget")
        main_widget.setLayout(self.main_layout)
        main_widget.setStyleSheet(
            "QWidget#main-widget{ border:2px solid rgb(150,150, 150);} ")
        self.setCentralWidget(main_widget)

    def initMenuBar(self):

        self.statusBar()

        # menu
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("File")
        imageMenu = mainMenu.addMenu("Image")
        compressMenu = mainMenu.addMenu("Compress")
        uncompressMenu = mainMenu.addMenu("Uncompress")

        # fileMenu
        closeAction = QAction("&Exit", self)
        closeAction.setShortcut("Ctrl+Q")
        closeAction.setStatusTip("Leave The App")
        closeAction.triggered.connect(self.closeApplication)

        fileMenu.addAction(closeAction)

        # imagemenu
        colorModeMenu = imageMenu.addMenu("Gray Converter")
        colorFiltersMenu = imageMenu.addMenu("Color Filters")
        imageMenu.addSeparator()
        filtersMenu = imageMenu.addMenu("Filters")
        frequenceFiltersMenu = imageMenu.addMenu(
            "Filters in the Frequency Domain")
        imageMenu.addSeparator()
        histogramMenu = imageMenu.addMenu("Histogram")
        spacialMenu = imageMenu.addMenu("Spatial Transformations")
        imageMenu.addSeparator()
        steganographyMenu = imageMenu.addMenu("Steganography")
        imageMenu.addMenu(steganographyMenu)

        #Spacial Transformations
        scalarNearestAction = QAction("Scale via Nearest Neighbours",self)
        scalarNearestAction.triggered.connect(self.scale_nearest)
        scalarBilinearAction = QAction("Scale via Bilinear",self)
        scalarBilinearAction.triggered.connect(self.scale_bilinear)

        rotateNearestAction = QAction("Rotate via Nearest Neighbours",self)
        rotateNearestAction.triggered.connect(self.rotate_nearest)
        rotateBilinearAction = QAction("Rotate via Bilinear",self)
        rotateBilinearAction.triggered.connect(self.rotate_bilinear)

        spacialMenu.addAction(scalarNearestAction)
        spacialMenu.addAction(scalarBilinearAction)
        spacialMenu.addAction(rotateNearestAction)
        spacialMenu.addAction(rotateBilinearAction)

        #Steganography
        steganographyAction = QAction("Write Message",self)
        steganographyAction.triggered.connect(self.steganography)
        steganographyMenu.addAction(steganographyAction)

        steganographyAction = QAction("Read Message", self)
        steganographyAction.triggered.connect(self.steganography_read)
        steganographyMenu.addAction(steganographyAction)

        ##Color Filters menu
        sepiaFilterAction = QAction("&Sepia", self)
        sepiaFilterAction.triggered.connect(self.sepia_filter)
        chromaKeyAction = QAction("&Apply Chroma", self)
        chromaKeyAction.triggered.connect(self.chroma_key)

        colorFiltersMenu.addAction(chromaKeyAction)
        colorFiltersMenu.addAction(sepiaFilterAction)

        ## Colormode
        rgbAction = QAction("&RGB", self)

        grayScaleAction = QAction("&Convert to gray via weighted mean", self)
        grayScaleAction.triggered.connect(self.rgb_to_gray)
        hsvAction = QAction("&HSV", self)
        hsvAction.triggered.connect(self.rgb_to_hsv)

        colorModeMenu.addAction(grayScaleAction)


        ## filters
        negativeFilterAction = QAction("&Negative", self)
        negativeFilterAction.triggered.connect(self.negative_transform)

        logFilterAction = QAction("&Logarithmic", self)
        logFilterAction .triggered.connect(self.logarithmic_transform)

        gammaFilterAction = QAction("&Gamma", self)
        gammaFilterAction.triggered.connect(self.gamma_transform)

        sobelFilterAction = QAction("&Sobel", self)
        sobelFilterAction.triggered.connect(self.sobel_filtering)

        gradientFilterAction = QAction("&Gradient", self)
        gradientFilterAction.triggered.connect(self.gradient_filtering)

        genericConvolutionFilterAction = QAction(
            "&Convolution (generic)", self)
        genericConvolutionFilterAction.triggered.connect(
            self.generic_convolution)

        medianFilterAction = QAction("&Median", self)
        medianFilterAction.triggered.connect(self.median_filter)

        meanFilterAction = QAction("&Blur via simple mean", self)
        meanFilterAction.triggered.connect(self.mean_filtering)

        gaussianFilterAction = QAction("&Blur via Gaussian", self)
        gaussianFilterAction.triggered.connect(self.gaussian)

        piecewiseAction = QAction("Piecewise",self)
        piecewiseAction.triggered.connect(self.piecewise)

        # filters/sharp
        laplaceFilterAction = QAction("&Laplacian", self)
        laplaceFilterAction.triggered.connect(self.laplacian)
        highBoostFilterAction = QAction("&HighBoost", self)
        highBoostFilterAction.triggered.connect(self.hi_boost_filtering)
        # add filters
        filtersMenu.addAction(negativeFilterAction)
        filtersMenu.addAction(logFilterAction)
        filtersMenu.addAction(gammaFilterAction)
        filtersMenu.addAction(piecewiseAction)
        filtersMenu.addSeparator()
        filtersMenu.addAction(genericConvolutionFilterAction)
        filtersMenu.addAction(medianFilterAction)
        filtersMenu.addSeparator()
        filtersMenu.addAction(meanFilterAction)
        filtersMenu.addAction(gaussianFilterAction)
        filtersMenu.addSeparator()
        filtersMenu.addAction(sobelFilterAction)
        filtersMenu.addAction(gradientFilterAction)
        filtersMenu.addAction(laplaceFilterAction)
        filtersMenu.addAction(highBoostFilterAction)

        # filtros na frequência
        spectrumFilterAction = QAction(
            "&Spectre of Fourier Transform", self)
        spectrumFilterAction.triggered.connect(self.fourier_spectrum)
        frequenceFiltersMenu.addAction(spectrumFilterAction)
        frequenceFiltersMenu.addSeparator()

        geometricFilterAction = QAction("&Geometric Mean", self)
        geometricFilterAction.triggered.connect(self.geometric_filtering)
        harmonicFilterAction = QAction("&Harmonic Mean", self)
        harmonicFilterAction.triggered.connect(self.harmonic_filtering)
        counterharmonicFilterAction = QAction("&Contra-harmonic Mean", self)
        counterharmonicFilterAction.triggered.connect(
            self.contra_harmonic_filtering)

        filtersMenu.addAction(geometricFilterAction)
        filtersMenu.addAction (harmonicFilterAction)
        filtersMenu.addAction (counterharmonicFilterAction)

        # histogram Menu
        equalizationAction = QAction("&Histogram Equalization", self)
        equalizationAction.triggered.connect(self.histEqualize)

        showHistogramAction = QAction("&See Histogram", self)
        showHistogramAction.triggered.connect(self.showHistogram)

        histogramMenu.addAction(equalizationAction)
        histogramMenu.addAction(showHistogramAction)

    def initToolBar(self):

        openAction = QAction(QtGui.QIcon(
            'assets/icons/open.png'), "&Open Ctrl+O", self)
        saveAction = QAction(QtGui.QIcon(
            'assets/icons/save.png'), "&Save Ctrl+S", self)
        saveAllAction = QAction(QtGui.QIcon(
            'assets/icons/save-as.png'), "&Save As Ctrl+Shift+S", self)
        undoAction = QAction(QtGui.QIcon(
            'assets/icons/undo.png'), "&Undo Ctrl+Z", self)
        redoAction = QAction(QtGui.QIcon(
            'assets/icons/redo.png'), "&Redo Ctrl+R", self)
        brushAction = QAction(QtGui.QIcon(
            'assets/icons/brush.png'), "&Brush", self)

        openAction.setShortcut("Ctrl+O")
        saveAction.setShortcut("Ctrl+S")
        saveAllAction.setShortcut("Ctrl+Shift+S")
        undoAction.setShortcut(QtGui.QKeySequence("Ctrl+Z"))
        redoAction.setShortcut(QtGui.QKeySequence("Ctrl+Y"))

        openAction.triggered.connect(self.fileOpen)
        saveAction.triggered.connect(self.saveFile)
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

    def gaussian(self):
        filter_size, ok = QInputDialog.getText(self, 'Suavização Gaussiana',
                                         'Choose the dimension size for your filter (>=3)')
        if ok and filter_size:
            sigma, ok = QInputDialog.getText(self, 'Suavização Gaussiana',
                                         'Choose a value for sigma')
            if ok and sigma:
                self.loadImage(self.transformController.apply_gaussian(int(filter_size),float(sigma)))

    def laplacian(self):
        self.loadImage(self.transformController.apply_laplacian())

    def piecewise(self):
        x,y = self.getCoordinateInput()
        self.loadImage(self.transformController.apply_piecewise_linear(x,y))

    def negative_transform(self):
        self.loadImage(self.transformController.negativeTransform())

    def logarithmic_transform(self):
        c, ok = QInputDialog.getText(self, 'Logaritmcic',
                                         'Enter c value (real):')
        if ok and c:
            self.loadImage(self.transformController.logarithmicTransform(float(c)))

    def gamma_transform(self):
        gamma, ok = QInputDialog.getText(self, 'Gamma Correction',
                                         'Enter gamma value (real):')
        if ok:
            self.loadImage(
                self.transformController.gammaTransform(float(gamma)))

    def median_filter(self):
        size, ok = QInputDialog.getText(self, 'Median',
                                        'Choose a filter dimension (> 2):')
        if ok:
            self.loadImage(self.transformController.apply_median(int(size)))

    def histEqualize(self):
        self.loadImage(self.transformController.apply_equalized_histogram())
    def showHistogram(self):
        self.loadImage(self.transformController.show_histogram())

    def generic_convolution(self):
        self.loadImage(self.transformController.apply_convolution(
            self.getMatrixInput()))


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
            i = i + 1
        try:
            table = np.float_(table)
            return table
        except:
            return None

    def getCoordinateInput(self):
        dialog = MatrixDialog()
        if dialog.exec():
            print(dialog.getInputs())
            gamma = dialog.getInputs()
        lines = gamma.split("\n")
        x = np.int_(lines[0].split(" "))
        y = np.int_(lines[1].split(" "))
        return x,y


    def gradient_filtering(self):
        self.loadImage(self.transformController.apply_gradient(
                self.getMatrixInput()))

    def mean_filtering(self):
        size, ok = QInputDialog.getText(self, 'Arithmetic Mean',
                                        'Choose a filter dimension (> 2):')
        if ok:
            self.loadImage(
                self.transformController.apply_arithmetic_mean(int(size)))

    def geometric_filtering(self):
        size, ok = QInputDialog.getText(self, 'Geometric Mean',
                                        'Choose a filter dimension (> 2):')
        if ok:
            self.loadImage(
                self.transformController.apply_geometric_mean(int(size)))

    def harmonic_filtering(self):
        size, ok = QInputDialog.getText(self, 'Harmonic Mean',
                                        'Choose a filter dimension (> 2):')
        if ok:
            self.loadImage(
                self.transformController.apply_harmonic_mean(int(size)))

    def contra_harmonic_filtering(self):
        size, ok = QInputDialog.getText(self, 'Contra-harmonic Mean',
                                        'Choose a filter dimension (> 2):')
        if ok:
            q, ok = QInputDialog.getText(self, 'Contra-harmonic Mean',
                                         'Choose a value for q')
            if ok:
                self.loadImage(
                    self.transformController.apply_contra_harmonic_mean(int(size), float(q)))

    def hi_boost_filtering(self):
        size, ok = QInputDialog.getText(self, 'HighBoost',
                                        'Choose a filter dimension (> 2):')
        if ok:
            c, ok = QInputDialog.getText(self, 'HighBoost',
                                         'Entre com o valor de c')
            if ok:
                self.loadImage(
                    self.transformController.apply_highboost(int(size), float(c)))

    def fourier_spectrum(self):
        w = FourierModal(self.transformController)
        if w.exec_():
            self.loadImage(self.transformController.apply_inverse_fourier())
            print("Success!")
        else:
            print("Cancel!")

    def rgb_to_gray(self):
        self.loadImage(self.transformController.rgb_to_gray())

    def rgb_to_hsv(self):
        self.loadImage(self.transformController.rgb_to_hsv())

    def sepia_filter(self):
        self.loadImage(self.transformController.apply_sepia())

    def chroma_key(self):
            name,_ = QtWidgets.QFileDialog.getOpenFileName(self,"Choose a background image")
            if name:
                faixa, ok = QInputDialog.getText(self, 'Chroma Key',
            'Choose a filter dimension (> 0):')
                if ok and faixa:
                    background = self.transformController.openImage(name)
                    self.loadImage(self.transformController.apply_chroma_key(background,int(faixa)))

    def steganography(self):
        name, _ = QtWidgets.QFileDialog.getOpenFileName(
            self, "Choose an image")
        if name:
            text, ok = QInputDialog.getText(self, 'Steganography',
                                            'Choose a filter dimension (> 0):')
            if ok and text:
                image = self.transformController.steganograph_encode(
                    name, text)
                name2, t = QtWidgets.QFileDialog.getSaveFileName(
                    self, 'Name your image with the hidden message', "", "BMP (*.bmp)")
                if name2:
                    self.transformController.saveImage(name2, image)

    def steganography_read(self):
        name, _ = QtWidgets.QFileDialog.getOpenFileName(
            self, "Choose an image")
        if name:
            text = self.transformController.steganograph_decode(name)
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("The following message was hidden inside the image: ")
            msg.setInformativeText(text)
            msg.setWindowTitle("Steganography")
            msg.exec_()


    def scale_nearest(self):
        scale, ok = QInputDialog.getText(self, 'Scale via Nearest Neighbours',
            'Choose a scale number')
        if(ok and scale):
            self.loadImage(self.transformController.apply_scale_nearest(float(scale)))

    def scale_bilinear(self):
        scale, ok = QInputDialog.getText(self, 'Scale via Bilinear',
            'Choose a scale number')
        if(ok and scale):
            self.loadImage(self.transformController.apply_scale_bilinear(float(scale)))

    def rotate_nearest(self):
        angle, ok = QInputDialog.getText(self, 'Rotate via Nearest Neighbours',
            'Choose an angle')
        if(ok and angle):
            self.loadImage(self.transformController.apply_rotation_nearest(float(angle)))
    def rotate_bilinear(self):
        angle, ok = QInputDialog.getText(self, 'Rotate via Bilinear',
            'Choose an angle')
        if(ok and angle):
            self.loadImage(self.transformController.apply_rotate_bilinear(float(angle)))


class MatrixDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.matrix = QPlainTextEdit(self)
        buttonBox = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)

        layout = QFormLayout(self)
        layout.addRow("Write down a matrix", self.matrix)
        layout.addWidget(buttonBox)

        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

    def getInputs(self):
        return (self.matrix.toPlainText())
