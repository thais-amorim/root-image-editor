#!/usr/bin/python

from image_filter import *
from color_converter import *
from color_filter import *

img = read_image("images\sobel_original.jpeg")
obtained = apply_sepia(img.copy())
save_image("images/obtained.jpg", obtained)
