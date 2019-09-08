from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5. QtGui import *
import sys

class ImageView(QWidget):
    def __init__(self):
        super().__init__()        

        self.label = QLabel(self)
        image = QPixmap("images/einstein.jpg")
        self.label.setPixmap(image)
        self.label.setGeometry(0,0,image.width(), image.height())
        self.label.setAlignment(Qt.AlignCenter)

        mainLayout = QGridLayout()
        mainLayout.addWidget(self.label)
        self.setLayout(mainLayout)
    
    def loadImage(self,name):
        image = QPixmap(name)
        self.label.setPixmap(image)