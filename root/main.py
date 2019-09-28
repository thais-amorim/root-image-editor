#!/usr/bin/python

from image_filter import *
from color_converter import *

img = read_image("images/blurry_moon.bmp")
r, g, b = get_rgb_layers(img.copy())
gray_image = rgb_to_gray_via_weighted_average(r, g, b)
obtained, sharpened = apply_laplacian(gray_image)
save_image("images/obtained.jpg", obtained)
save_image("images/final.jpg", sharpened)
