#!/usr/bin/python

from image_filter import *

img = read_image("images/einstein.jpg")
img = rgb_to_gray(img)
#save_image("save_test.jpg", img.copy())
#apply_negative("negative_test.jpg", img.copy())
#apply_logarithmic("log_test.jpg", img.copy())
#apply_gamma_correction("gamma_test.jpg", img.copy(), 1.5)
#draw_histogram("histogram_test.jpg", img.copy())
#apply_equalized_histogram("eq_test.jpg", img.copy())
#apply_median(img.copy(), -5, "median2.jpg")

coordinates_x = np.array([0,10,11,13,14,255])
coordinates_y = np.array([0,10,11,100,101,255])
apply_piecewise_linear("piecewise_linear.jpg",img.copy(),coordinates_x,coordinates_y)
