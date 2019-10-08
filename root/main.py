from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5. QtGui import *

from image_filter import *
from color_converter import *
from color_filter import *

img = read_image("images/falcon.png", "RGBA")
bg = read_image("images/bg.png", "RGBA")
final = apply_chroma_key(bg, img)
save_image("images/final.png", final)
