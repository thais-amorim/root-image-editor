from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QAction, QMainWindow, QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtCore import *
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(50,50,800,600)
        self.setWindowTitle("Trabalho de PDI")

        #Essas três linhas são importantes, porque por algum motivo, o ícone da barra de tarefas naõ aparecia no windows
        import ctypes
        myappid = u'mycompany.myproduct.subproduct.version' # arbitrary string
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid) 
        
        ## Adicionando ícones: o ícone de 80px deve aparecer lá em cima, do lado do nome da janela, 
        # já o de 256 é o que aparece na barra de tarefas do windows
        app_icon = QtGui.QIcon()
        app_icon.addFile('assets/icons/camera-80.png',QSize(80,80))
        app_icon.addFile('assets/icons/camera-256.png',QSize(256,256))
        self.setWindowIcon(app_icon)  
        
        self.home()

    def home(self):
        self.show()


#Para chamar a classe:
app = QApplication([])
GUI = Window()
app.exec_()