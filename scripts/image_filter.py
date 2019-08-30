import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import math

def read_image(image_path):
    return mpimg.imread(image_path)

def save_image(path, image_as_byte):
    plt.imshow(image_as_byte)
    mpimg.imsave(path, image_as_byte)

def apply_negative(img_name, img):
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            img[i][j] = 255 - img[i][j]
    save_image('images/' + img_name, img)

def apply_logarithmic(img_name, img):
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            img[i][j] = compute_log(img[i][j])
    save_image('images/' + img_name, img)

def compute_log(pixel):
    c = 255/math.log(255+1,10);
    return c * math.log(float(1 + pixel[0]),10);

def apply_gamma_correction(img_name, img, exponent):
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            img[i][j] = (255/(255+1 ** exponent)) * ((1 + img[i][j]) ** exponent)
    save_image('images/' + img_name, img)

def draw_histogram(img_name, img):
    data = img.flatten()
    plt.hist(data, 256)
    plt.savefig('images/' + img_name) #save_image() doesn't work here. It needs investigation!
    plt.close()

def cumsum(img_matrix):
	# finds cumulative sum of a numpy array, list
	return [sum(img_matrix[:i+1]) for i in range(len(img_matrix))]

def normalize_histogram(img):
    h = [0.0] * 256
    width, height = img.shape
    for i in range(width):
        for j in range(height):
            h[img[i, j]] += 1
    return np.array(h)/(width*height)


def apply_histogram_equalization(img_name, img):
    normalized_hist = normalize_histogram(img)
    cdf = np.array(normalized_hist.cumsum())
    transfer_function_values = np.uint8(255 * cdf)
    equalized_img = np.zeros_like(img)

    width, height = img.shape
    for i in range(width):
        for j in range(height):
            equalized_img[i][j] = transfer_function_values[img[i][j]]

    save_image('images/' + img_name, equalized_img)
    draw_histogram('chart_' + img_name, equalized_img) #output is weirdo. Review it!
