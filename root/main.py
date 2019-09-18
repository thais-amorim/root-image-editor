#!/usr/bin/python

from image_filter import *

img = read_image("images/sobel_original.jpeg")
img = rgb_to_gray(img)
obtained = apply_sobel(img.copy())
save_image("images/sobel_output.jpg", obtained)
draw_histogram("images/hist_sobel_output.jpg", obtained)
