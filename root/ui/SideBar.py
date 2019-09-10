from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5. QtGui import *
from ImageView import ImageView
import sys

class SideBar(QWidget):
    def __init__(self, image_path):
        super().__init__()        
        self.originalImageView = ImageView(image_path)
        self.originalImageView.scale(self.width()/3,self.height()/3)

        self.init_propertiesWidget()

        name = QLabel('Properties')
        name.setStyleSheet(" border:2px solid rgb(150,150, 150)")
        image_name = QLabel('Original image')
        image_name.setStyleSheet(" border:2px solid rgb(150,150, 150)")


        side_layout = QVBoxLayout()
        side_layout.addWidget(image_name)
        side_layout.addWidget(self.originalImageView)
        side_layout.addWidget(name)
        side_layout.addWidget(self.properties)



        self.setLayout(side_layout)
       
        
        
        # self.setLayout(side_layout)
        # self.setAutoFillBackground(True)
        # p = self.palette()
        # p.setColor(self.backgroundRole(), Qt.gray)
        # self.setPalette(p)


    def loadImage(self, image_path):
        self.originalImageView.loadImage(image_path)
        self.originalImageView.scale(self.width()/3,self.height()/3)



    def init_propertiesWidget(self):
        self.properties = QWidget()
        self.properties.setObjectName('properties')
        self.properties.setStyleSheet("QWidget#properties { border:2px solid rgb(150,150, 150) } ")
        


        title = QLabel('Propriedade1')
        author = QLabel('Propriedade2')
        review = QLabel('Propriedade3')

        titleEdit = QLineEdit()
        titleEdit.setReadOnly(True)
        authorEdit = QLineEdit()
        authorEdit.setReadOnly(True)
        reviewEdit = QTextEdit()
        reviewEdit.setReadOnly(True)

        grid = QVBoxLayout()
        # grid.setSpacing(10)


        grid.addWidget(title)
        grid.addWidget(titleEdit)

        grid.addWidget(author)
        grid.addWidget(authorEdit)

        grid.addWidget(review)
        grid.addWidget(reviewEdit)
        
        self.properties.setLayout(grid) 
        
        # self.setGeometry(300, 300, 350, 300)
        # self.setWindowTitle('Review') 