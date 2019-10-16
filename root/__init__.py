from root.filter import ImageFilter as filter
from root.filter import RgbFilter as rgbFilter
from root.filter import ColorFilter as color
from root.converter import ColorConverter as converter
from root.converter import ScaleConverter as scale
from root.util import ImageUtil as util
from root.util import RgbUtil as rgb
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
sys.path.insert(0, sys.path[0]+'\\ui')
print(sys.path)

from root.ui import MainWindow


def main():
    app = QApplication([])
    GUI = MainWindow()
    app.exec_()


if __name__ == "__main__":
    main()
