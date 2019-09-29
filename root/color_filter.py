import imageio
import numpy as np
from image_filter import normalize_image, get_image_dimensions


def get_rgb_layers(rgb):
    r = rgb[:, :, 0]
    g = rgb[:, :, 1]
    b = rgb[:, :, 2]

    return r, g, b


def apply_sepia(img):
    height, width = get_image_dimensions(img)
    r_matrix, g_matrix, b_matrix = get_rgb_layers(img)
    for i in range(height):
        for j in range(width):
            r, g, b = r_matrix[i][j], g_matrix[i][j], b_matrix[i][j]
            tr = int(0.393 * r + 0.769 * g + 0.189 * b)
            tg = int(0.349 * r + 0.686 * g + 0.168 * b)
            tb = int(0.272 * r + 0.534 * g + 0.131 * b)

            if tr > 255:
                r = 255
            else:
                r = tr

            if tg > 255:
                g = 255
            else:
                g = tg

            if tb > 255:
                b = 255
            else:
                b = tb

            img[i][j] = [r, g, b]

    return img
