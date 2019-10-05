#!/usr/bin/python

from image_filter import *
from color_filter import *
from color_converter import *
from util import read_image, save_image

img = read_image("images/hip-salt.jpg")
r, g, b = get_rgb_layers(img)
img = rgb_to_gray_via_weighted_average(r, g, b)
median_out = apply_harmonic_mean(img.copy(), 3)
save_image("images/output.jpg", median_out)
