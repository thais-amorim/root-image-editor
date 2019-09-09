from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5. QtGui import *
#!/usr/bin/python
import imageio
import numpy as np
import sys

class ImageView(QWidget):
    def __init__(self, image_path):
        super().__init__()        
        self.setStyleSheet(" border:2px solid rgb(150,150, 150); ")

        self.label = QLabel(self)

        #Initialze QtGui.QImage() with arguments data, height, width, and QImage.Format

        im = imageio.imread(image_path, as_gray=False, pilmode="RGB")
        self.loadImage(im)

        self.label.setGeometry(0,0,self.image.width(), self.image.height())
        self.label.setAlignment(Qt.AlignCenter)


        mainLayout = QGridLayout()
        mainLayout.addWidget(self.label)
        self.setLayout(mainLayout)
    
    def loadImage(self,im):
        im = im.astype(np.uint8)
        qimage = self.toQImage(im)
        gray_color_table = [qRgb(i, i, i) for i in range(256)]
        qimage.setColorTable(gray_color_table)

        self.image = QPixmap.fromImage(qimage)
        self.label.setPixmap(self.image)


    def scale(self, width,height):
        if width > height:
           self.image = self.image.scaledToWidth(width)
        else: 
            self.image = self.image.scaledToHeight( height)
        self.label.setPixmap(self.image)


  
      
    def toQImage(self,im, copy=False):
        gray_color_table = [qRgb(i, i, i) for i in range(256)]
        
        if im is None:
            return QImage()

        if im.dtype == np.uint8:
            if len(im.shape) == 2:
                qim = QImage(im.data, im.shape[1], im.shape[0], im.strides[0], QImage.Format_Indexed8)
                qim.setColorTable(gray_color_table)
                return qim.copy() if copy else qim

            elif len(im.shape) == 3:
                if im.shape[2] == 3:
                    qim = QImage(im.data, im.shape[1], im.shape[0], im.strides[0], QImage.Format_RGB888)
                    return qim.copy() if copy else qim
                elif im.shape[2] == 4:
                    qim = QImage(im.data, im.shape[1], im.shape[0], im.strides[0], QImage.Format_ARGB32)
                    return qim.copy() if copy else qim
