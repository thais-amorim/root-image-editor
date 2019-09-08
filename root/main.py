#!/usr/bin/python

from image_filter import *

img = read_image("images/averaging_test.jpg")
img = rgb_to_gray(img)
obtained = apply_average(img.copy(), 15)
save_image("average.jpg", obtained)
draw_histogram("hist_average.jpg",obtained)
