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
