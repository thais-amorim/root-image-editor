#!/usr/bin/python

from image_filter import *
from color_filter import *
from color_converter import *

img = read_image("images/cat.jpg")
r,g,b = get_rgb_layers(img)
img = rgb_to_gray_via_simple_average(r,g,b)
final = apply_highboost(img, 2, 3)
save_image("images/final.png", final)
