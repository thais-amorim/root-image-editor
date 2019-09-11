#!/usr/bin/python
import imageio
import matplotlib.pyplot as plt
import numpy as np
import math

_MAX_PIXEL = 255


def read_image(image_path):
    return imageio.imread(image_path, as_gray=False, pilmode="RGB")


def save_image(name, image_as_byte):
    imageio.imwrite(name, image_as_byte)


def rgb_to_gray(rgb):
    return np.dot(rgb[..., :3], [0.2989, 0.5870, 0.1140])


def apply_negative(img):
    return _MAX_PIXEL - img


def apply_logarithmic(img):
    max_obtained = np.max(img)
    c = (_MAX_PIXEL / np.log(1 + max_obtained))
    log_img = c * np.log(1 + img)
    return log_img.astype('uint8')


def apply_gamma_correction(img_name, img, gamma):
    return ((img / _MAX_PIXEL) ** (1 / gamma))


def draw_histogram(img_name, img):
    data = img.flatten()
    plt.hist(data, _MAX_PIXEL + 1, [0, 256])
    plt.savefig(img_name)
    plt.close()


def apply_equalized_histogram(img):
    # Getting the pixel values of the image
    original = np.array(img)
    # Creating a new matrix for the image
    equalized_img = np.copy(original)
    # Getting unique pixels and frequency of the values from the image
    unique_pixels, pixels_frequency = np.unique(original, return_counts=True)
    # Image pixels divided by the size of the image
    pk = pixels_frequency / img.size
    pk_length = len(pk)
    # Getting the cummulative frequency of the unique pixel values
    sk = np.cumsum(pk)
    # Multiplying the cummulative frequency by the maximum value of the pixels
    mul = sk * np.max(original)
    roundVal = np.round(mul)
    # Mapping the pixels for the equalization
    for i in range(len(original)):
        for j in range(len(original[0])):
            equalized_img[i][j] = roundVal[np.where(
                unique_pixels == original[i][j])]

    return equalized_img


def get_empty_image_with_same_dimensions(img):
    height, width = get_image_dimensions(img)
    empty_image = np.zeros((height, width), np.uint8)
    return empty_image, img


def get_image_dimensions(img):
    data = np.array(img)
    height = data.shape[0]
    width = data.shape[1]
    return height, width


def format_size(size):
    '''
    Return odd size N, where N >= 3 and filter would be a matrix N x N
    '''
    min_size = 3
    if size < 3:
        result = min_size
    elif (size % 2) == 0:
        result = size + 1
    else:
        result = size

    return result


def get_neighbors_matrix(filter_size, i, j, data):
    mid_position = filter_size // 2
    neighbors = []
    for z in range(filter_size):
        if i + z - mid_position < 0 or i + z - mid_position > len(data) - 1:
            for c in range(filter_size):
                neighbors.append(0)
        elif j + z - mid_position < 0 or j + mid_position > len(data[0]) - 1:
            neighbors.append(0)
        else:
            for k in range(filter_size):
                neighbors.append(data[i + z - mid_position]
                                 [j + k - mid_position])

    return neighbors


def get_median(filter_size, i, j, data):
    filter_size = format_size(filter_size)
    mid_position = filter_size // 2
    neighbors = get_neighbors_matrix(filter_size, i, j, data)
    neighbors.sort()
    return neighbors[len(neighbors) // 2]


def apply_median(img, filter_size):
    obtained, original = get_empty_image_with_same_dimensions(img)
    for i in range(len(original)):
        for j in range(len(original[0])):
            obtained[i][j] = get_median(filter_size, i, j, original)

    return obtained


def apply_piecewise_linear(img, coordinates_x, coordinates_y):
    x = np.array(range(0, _MAX_PIXEL + 1), dtype=np.uint8)
    interp = np.interp(x, coordinates_x, coordinates_y)
    obtained = img.copy()
    for i in range(obtained.shape[0]):
        for j in range(obtained.shape[1]):
            index = int(np.round(obtained[i][j]))
            obtained[i][j] = interp[index]

    return obtained


def get_average(filter_size, i, j, data):
    filter_size = format_size(filter_size)
    neighbors = get_neighbors_matrix(filter_size, i, j, data)
    sum_value = sum(neighbors)
    counter = len(neighbors)
    return sum_value / counter


def apply_average(img, filter_size):
    obtained, original = get_empty_image_with_same_dimensions(img)
    for i in range(len(original)):
        for j in range(len(original[0])):
            obtained[i][j] = get_average(filter_size, i, j, original)

    return obtained


def apply_convolution(img, filter_matrix):
    obtained, original = get_empty_image_with_same_dimensions(img)
    height, width = get_image_dimensions(img)

    for row in range(1, height - 1):
        for col in range(1, width - 1):
            value = filter_matrix * \
                original[(row - 1):(row + 2), (col - 1):(col + 2)]
            max_obtained_value = max(0, value.sum())
            obtained[row, col] = min(max_obtained_value, _MAX_PIXEL)

    return obtained


def apply_laplacian(img):
    kernel = np.array([
        [-1, -1, -1],
        [-1,  8, -1],
        [-1, -1, -1]])

    return apply_convolution(img,kernel)
