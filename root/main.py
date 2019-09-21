from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5. QtGui import *

import sys

sys.path.insert(0, sys.path[0]+'\\ui')
print(sys.path)
from MainWindow import MainWindow

app = QApplication([])
GUI = MainWindow()
app.exec_()


# from PIL import Image
# import numpy as np

# def PIL2array(img):
#     return numpy.array(img.getdata(),
#                     numpy.uint8).reshape(img.size[1], img.size[0], 3)

# img = Image.open('images/einstein.jpg').convert('LA')
# img = np.asarray(img.getdata()).reshape(img.size[1], img.size[0], -1)
# print(img)