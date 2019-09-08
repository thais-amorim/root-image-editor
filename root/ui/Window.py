from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5. QtGui import *
from LeftBar import LeftBar
from ImageView import ImageView
import sys

class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(50,50,Const.WIDTH,Const.HEIGHT)
        self.setWindowTitle(Const.WINDOW_TITLE)
        self.initIcons()
        self.show()
    

    def initIcons(self):
        import ctypes
        myappid = u'mycompany.myproduct.subproduct.version' # arbitrary string
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

        app_icon = QtGui.QIcon()
        app_icon.addFile(Const.ICONS_PATH + 'camera-80.png',QSize(80,80))
        app_icon.addFile(Const.ICONS_PATH + 'camera-256.png',QSize(256,256))
        self.setWindowIcon(app_icon)   

    def fileOpen(self):
        name,_ = QtWidgets.QFileDialog.getOpenFileName(self,"Open File")
        file = open(name,'r')
        self.setWindowTitle(name)
        self.imageView.loadImage(name)
    
    def closeApplication(self):
        print("Desligando....")
        sys.exit()

class Const():
    WINDOW_TITLE = "PytoShop"
    ICONS_PATH = "assets/icons/"
    WIDTH = 800
    HEIGHT = 600