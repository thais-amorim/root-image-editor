from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5. QtGui import *
import sys

class ImageView(QWidget):
    def __init__(self, image_path):
        super().__init__()        
        self.setStyleSheet(" border:2px solid rgb(150,150, 150); ")

        self.label = QLabel(self)
        self.image = QPixmap(image_path)
        self.label.setPixmap(self.image)
        self.label.setGeometry(0,0,self.image.width(), self.image.height())
        self.label.setAlignment(Qt.AlignCenter)

        mainLayout = QGridLayout()
        mainLayout.addWidget(self.label)
        self.setLayout(mainLayout)
    
    def loadImage(self,name):
        self.image = QPixmap.fromImage(name)
        self.label.setPixmap(self.image)

    def scale(self, width,height):
        if width > height:
           self.image = self.image.scaledToWidth(width)
        else: 
            self.image = self.image.scaledToHeight( height)
        self.label.setPixmap(self.image)