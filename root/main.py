#!/usr/bin/python

from filter import ImageFilter as filter
from filter import ColorFilter as color
from color_converter import *

img = filter.read_image("images/contra-harmonic-mean/Fig0508a.jpg")
r, g, b = color.get_rgb_layers(img)
img = rgb_to_gray_via_weighted_average(r, g, b)
output = filter.apply_contra_harmonic_mean(img.copy(), 3, 1.5)
filter.save_image("images/contra-harmonic-mean/output.jpg", output)
