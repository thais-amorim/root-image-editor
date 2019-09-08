from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5. QtGui import *
import sys

class LeftBar(QWidget):
    def __init__(self):
        super().__init__()
        self.btn_1 = QPushButton('Filtro-1', self)
        self.btn_2 = QPushButton('Filtro-2', self)
        self.btn_3 = QPushButton('Filtro-3', self)
        self.btn_4 = QPushButton('Filtro-4', self)
        self.btn_5 = QPushButton('Filtro-5', self)

        left_layout = QGridLayout()
        # left_layout.addStretch(0)
        # left_layout.setStretch(1,1)
        left_layout.setSpacing(10)
        left_layout.addWidget(self.btn_1,1,0)
        left_layout.addWidget(self.btn_2,2,0)
        left_layout.addWidget(self.btn_3,3,0)
        left_layout.addWidget(self.btn_4,4,0)
        left_layout.addWidget(self.btn_5,4,0)


        self.setLayout(left_layout)

        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.gray)
        self.setPalette(p)
