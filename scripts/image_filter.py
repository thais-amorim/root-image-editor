import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def read_image(image_path):
    img = mpimg.imread(image_path)
    plt.imshow(img)
    plt.show()

def save_image(name, image_path):
    img = mpimg.imread(image_path)
    plt.imshow(img)
    mpimg.imsave(name, img)
