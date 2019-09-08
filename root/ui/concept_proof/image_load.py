from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QAction, QMainWindow, QApplication, QWidget, QPushButton, QMessageBox, QLabel, QGridLayout
from PyQt5.QtCore import *
from PyQt5. QtGui import *
import sys

# class Frame(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setGeometry(50,50,800,600)
#         self.setWindowTitle("Trabalho de PDI")
#         self.show()
#         f = Window()

        
        

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(50,50,800,600)
        self.setWindowTitle("Trabalho de PDI")
        self.f = QWidget(self)
        self.f.setGeometry(0,0,self.width(), self.height())
        self.home()

    def home(self):

        mainLayout = QGridLayout()
        self.f.setLayout(mainLayout)


        self.label = QLabel(self)
        image = QPixmap("images/einstein.jpg")
        self.label.setPixmap(image)
        self.label.setGeometry(0,0,image.width(), image.height())
        self.label.setAlignment(Qt.AlignCenter)


        mainLayout.addWidget(self.label)
       
        self.show()
        # self.f.show()



#Para chamar a classe:
app = QApplication([])
GUI = Window()
sys.exit(app.exec_())



