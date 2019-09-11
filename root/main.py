#!/usr/bin/python

from image_filter import *
import numpy as np

kernel = np.array([
    [-1, -1, -1],
    [-1,  8, -1],
    [-1, -1, -1]])


img = read_image("images/UNit3.png")
img = rgb_to_gray(img)
obtained = apply_laplacian(img.copy())
save_image("images/laplace_output.jpg", obtained)
draw_histogram("images/hist_laplace_output.jpg", obtained)

obtained2 = apply_convolution(img.copy(), kernel)
save_image("images/convolution_output.jpg", obtained2)
draw_histogram("images/hist_convolution_output.jpg", obtained2)
