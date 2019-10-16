from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5. QtGui import *
#!/usr/bin/python
import imageio
import numpy as np
import sys
sys.path.insert(0, sys.path[0]+'\\..\\controllers')
print(sys.path)
from root.controllers import TransformationController
from root.ui import ImageView
class FourierModal(QDialog):

    def __init__(self,transformationController: TransformationController):
        super().__init__()
        self.setStyleSheet(" border:2px solid rgb(150,150, 150); ")
        self.setWindowTitle("Fourier Manager!")

        self.transformController = transformationController

        self.low_pass_button = QPushButton('Passa baixa', self)
        self.high_pass_button = QPushButton('Passa alta', self)
        self.band_pass_button = QPushButton('Passa banda', self)

        self.low_pass_button.clicked.connect(self.low_pass_filter)
        self.high_pass_button.clicked.connect(self.high_pass_filter)
        self.band_pass_button.clicked.connect(self.band_pass_filter)

        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

        mag = self.transformController.apply_fourier()
        img = mag

        self.imageView = ImageView(img)


        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept_action)
        self.buttonBox.rejected.connect(self.reject_action)

        self.layout = QVBoxLayout()


        mainMenu = QToolBar()

        undoAction = QAction(QtGui.QIcon('assets/icons/undo.png'),"Desfazer Ctrl+Z", self)
        redoAction = QAction(QtGui.QIcon('assets/icons/redo.png'),"Desfazer Ctrl+R", self)
        undoAction.setShortcut(QtGui.QKeySequence("Ctrl+Z"))
        redoAction.setShortcut(QtGui.QKeySequence("Ctrl+Y"))

        undoAction.triggered.connect(self.undoLastAction)
        redoAction.triggered.connect(self.redoLastAction)

        mainMenu.addAction(undoAction)
        mainMenu.addAction(redoAction)




        self.layout.addWidget(mainMenu)
        self.layout.addWidget(self.low_pass_button)
        self.layout.addWidget(self.high_pass_button)
        self.layout.addWidget(self.band_pass_button)


        self.layout.addWidget(self.imageView)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)

    def accept_action(self):
        buttonReply = QMessageBox.question(self, 'Alerta de Alteração', "Você deseja aplicar essas alterações na imagem original?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            print('Yes clicked.')
            self.accept()
        else:
            print('No clicked.')

    def reject_action(self):
        buttonReply = QMessageBox.question(self, 'Alerta de Alteração', "Você deseja cancelar a edição no domínio da frequência?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            print('Yes clicked.')
            self.reject()
        else:
            print('No clicked.')


    def loadImage(self,name):
        self.imageView.loadImage(name)

    def low_pass_filter(self):
        size, ok = QInputDialog.getText(self, 'Filtro passa baixa:',' adicione um valor em px')
        if ok:
            self.loadImage(self.transformController.apply_low_pass(int(size)))

    def high_pass_filter(self):
        size, ok = QInputDialog.getText(self, 'Filtro passa alta:',' adicione um valor em px')
        if ok:
            self.loadImage(self.transformController.apply_high_pass(int(size)))

    def band_pass_filter(self):
        size, ok = QInputDialog.getText(self, 'Filtro passa banda:',' adicione dois valores (raio menor e raio maior) separados por espaço')
        if ok:
            try:
                minor, major = size.split(' ')
                self.loadImage(self.transformController.apply_band_pass(int(minor),int(major)))
            except:
                print("Erro em passa banda")

    def undoLastAction(self):
        self.loadImage(self.transformController.undoFourierAction())

    def redoLastAction(self):
        self.loadImage(self.transformController.redoFourierAction())
