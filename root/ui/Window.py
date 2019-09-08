from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5. QtGui import *
from SideBar import SideBar
from ImageView import ImageView
import sys

class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.const = Const()
        self.setGeometry(50,50,self.const.WIDTH,self.const.HEIGHT)
        self.setWindowTitle(self.const.WINDOW_TITLE)
        self.side_bar = SideBar(self.const.DEFAULT_IMAGE)
        self.imageView = ImageView(self.const.DEFAULT_IMAGE)
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


    def closeApplication(self):
        print("Desligando....")
        sys.exit()

class Const():
    DEFAULT_IMAGE = "images/einstein.jpg"
    WINDOW_TITLE = "PytoShop"
    ICONS_PATH = "assets/icons/"
    WIDTH = 800
    HEIGHT = 600