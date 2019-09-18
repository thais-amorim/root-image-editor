#!/usr/bin/python

from image_filter import *
from color_conversor import *

img = read_image("images/sobel_original.jpeg")
weighted_obtained = rgb_to_gray_via_weighted_average(img.copy())
save_image("images/weighted_output.jpg", weighted_obtained)

simple_obtained = rgb_to_gray_via_weighted_average(img.copy())
save_image("images/simple_output.jpg", simple_obtained)
