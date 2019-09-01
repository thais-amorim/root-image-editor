#!/usr/bin/python
import imageio
import matplotlib.pyplot as plt
import numpy as np
import math

_max_pixel = 255;
_images_path = 'images/'

def read_image(image_path):
    return imageio.imread(image_path, as_gray=False, pilmode="RGB")

def save_image(name, image_as_byte):
    imageio.imwrite(_images_path+name, image_as_byte)

def rgb_to_gray(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])

def apply_negative(img_name, img):
    negative = _max_pixel - img
    save_image(img_name, negative.astype('uint8'))

def apply_logarithmic(img_name, img):
    max_obtained = np.max(img)
    c = (_max_pixel/np.log(1+max_obtained))
    log_img = c * np.log(1+img)
    save_image(img_name, log_img.astype('uint8'))

def apply_gamma_correction(img_name, img, gamma):
    gamma_correction = ((img/_max_pixel) ** (1/gamma));
    save_image(img_name, gamma_correction)

def draw_histogram(img_name, img):
    data = img.flatten()
    plt.hist(data, _max_pixel+1, [0,256])
    plt.savefig(_images_path + img_name)
    plt.close()

def apply_equalized_histogram(img_name, img):
    # Getting the pixel values of the image
    original = np.array(img)
    # Creating a new matrix for the image
    equalized_img = np.copy(original)
    # Getting unique pixels and frequency of the values from the image
    unique_pixels, pixels_frequency = np.unique(original, return_counts=True)
    # Image pixels divided by the size of the image
    pk = pixels_frequency/img.size
    pk_length = len(pk)
    # Getting the cummulative frequency of the unique pixel values
    sk = np.cumsum(pk)
    # Multiplying the cummulative frequency by the maximum value of the pixels
    mul = sk*np.max(original)
    roundVal = np.round(mul)
    # Mapping the pixels for the equalization
    for i in range(len(original)):
        for j in range(len(original[0])):
            equalized_img[i][j] = roundVal[np.where(unique_pixels == original[i][j])]

    save_image(img_name, equalized_img.astype('uint8'))
    draw_histogram("hist_"+img_name,equalized_img)

def get_empty_image_with_same_dimensions(img):
    data = np.array(img)
    height = data.shape[0]
    width = data.shape[1]
    empty_image = np.zeros((height, width), np.uint8)
    return empty_image, data

# Return odd size N, where N >= 3 and filter would be a matrix N x N
def format_size(size):
    min_size = 3
    if size < 3:
        result = min_size
    elif (size % 2) == 0:
        result = size + 1
    else:
        result = size

    return result


def get_median(filter_size, i, j, data):
    filter_size = format_size(filter_size)
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
                neighbors.append(data[i + z - mid_position][j + k - mid_position])

    neighbors.sort()
    return neighbors[len(neighbors) // 2]

def apply_median(img, filter_size, img_name):
    obtained, original = get_empty_image_with_same_dimensions(img)
    for i in range(len(original)):
        for j in range(len(original[0])):
            obtained[i][j] = get_median(filter_size,i,j,original)

    save_image(img_name, obtained.astype('uint8'))
    draw_histogram("hist_"+img_name,obtained)
