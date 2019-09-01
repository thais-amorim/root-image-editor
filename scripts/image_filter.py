import imageio
import matplotlib.pyplot as plt
import numpy as np
import math

_max_pixel = 255;

def read_image(image_path):
    return imageio.imread(image_path, as_gray=False, pilmode="RGB")

def save_image(path, image_as_byte):
    imageio.imwrite(path, image_as_byte.astype('uint8'))

def rgb_to_gray(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])

def apply_negative(img_name, img):
    negative = _max_pixel - img
    save_image('images/' + img_name, negative)

def compute_log(img):
    max_obtained = np.max(img)
    c = (_max_pixel/np.log(1+max_obtained))
    return  c * np.log(1+img)

def apply_logarithmic(img_name, img):
    max_pixel_value = np.max(img)
    log_img = compute_log(img)
    save_image('images/' + img_name, log_img)

def apply_gamma_correction(img_name, img, gamma):
    gamma_correction = ((img/_max_pixel) ** (1/gamma));
    save_image('images/' + img_name, gamma_correction)

def draw_histogram(img_name, img):
    data = img.flatten()
    plt.hist(data, _max_pixel+1)
    plt.savefig('images/' + img_name) #save_image() doesn't work here. It needs investigation!
    plt.close()
