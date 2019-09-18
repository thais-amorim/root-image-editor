import numpy as np

def rgb_to_gray_via_weighted_average(rgb):
    red = rgb[:, :, 0]
    green = rgb[:, :, 1]
    blue = rgb[:, :, 2]

    return (red * 0.2989) + (green * 0.5870) + (blue * 0.1140)

def rgb_to_gray_via_simple_average(rgb):
    red = rgb[:, :, 0]
    green = rgb[:, :, 1]
    blue = rgb[:, :, 2]

    return (red + green + blue) / 3
