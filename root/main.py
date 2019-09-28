#!/usr/bin/python

from image_filter import *
from color_converter import *

img = read_image("images/aranha_trevosa.jpeg")
r, g, b = get_rgb_layers(img.copy())
gray_image = rgb_to_gray_via_weighted_average(r, g, b)
obtained = apply_sobel(gray_image)
save_image("images/obtained2.jpg", obtained)
save_image("images/final2.jpg", gray_image + obtained)
