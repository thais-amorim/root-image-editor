import matplotlib.pyplot as plt
import matplotlib.image as mpimg
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
