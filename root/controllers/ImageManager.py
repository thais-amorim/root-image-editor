#!/usr/bin/python
import imageio
import matplotlib.pyplot as plt
import numpy as np
import math

_max_pixel = 255
_images_path = 'images/'


class ImageManager():

    def __init__(self):
        super().__init__()


    #Abre um arquivo e retorna ???
    def read_image(self,image_path):
        return imageio.imread(image_path, as_gray=False, pilmode="RGB")

    def save_image(self,name, image_as_byte):
        import matplotlib
        ##Correção: com esse código, é possível salvar a imagem e conseguir abrir no windows depois
        matplotlib.image.imsave(_images_path+name, image_as_byte, cmap = matplotlib.cm.gray)
        # imageio.imwrite(_images_path+name, image_as_byte)

    #Converte a imagem de 8bits para escala de cinza
    def rgb_to_gray(self,rgb):
        return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])

    # Return odd size N, where N >= 3 and filter would be a matrix N x N
    def format_size(self,size):
        min_size = 3
        if size < 3:
            result = min_size
        elif (size % 2) == 0:
            result = size + 1
        else:
            result = size

        return result

    def get_empty_image_with_same_dimensions(self,img):
        data = np.array(img)
        height = data.shape[0]
        width = data.shape[1]
        empty_image = np.zeros((height, width), np.uint8)
        return empty_image, data

# img = read_image("images/einstein.jpg")
# img = rgb_to_gray(img)


# coordinates_x = np.array([0,10,11,13,14,255])
# coordinates_y = np.array([0,10,11,100,101,255])
# apply_piecewise_linear("piecewise_linear.jpg",img.copy(),coordinates_x,coordinates_y)