#!/usr/bin/python

from image_filter import *

img = read_image("images/UNit3.png")
img = rgb_to_gray(img)
obtained = apply_laplace(img.copy())
save_image("images/laplace_output.jpg", obtained)
draw_histogram("images/hist_laplace_output.jpg", obtained)
