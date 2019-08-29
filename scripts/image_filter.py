import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def read_image(image_path):
    return mpimg.imread(image_path)

def save_image(path, image_as_byte):
    plt.imshow(image_as_byte)
    mpimg.imsave(path, image_as_byte)

def apply_negative(img_name, img):
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            negative_byte = 255 - img[i][j]
            img[i][j] = negative_byte
    save_image('images/' + img_name, img)
