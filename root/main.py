#!/usr/bin/python

from image_filter import *
from color_filter import *
from color_converter import *

img = read_image("images/mona_with_noisy.jpg")
r,g,b = get_rgb_layers(img)
img = rgb_to_gray_via_simple_average(r,g,b)
median_out = apply_median(img.copy(), 3)
save_image("images/median.png", median_out)
