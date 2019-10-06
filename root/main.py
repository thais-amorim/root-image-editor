#!/usr/bin/python

from image_filter import *
from color_filter import *
from color_converter import *

img = read_image("images/contra-harmonic-mean/Fig0508a.jpg")
r, g, b = get_rgb_layers(img)
img = rgb_to_gray_via_weighted_average(r, g, b)
output = apply_contra_harmonic_mean(img.copy(), 3, 1.5)
save_image("images/contra-harmonic-mean/output.jpg", output)
