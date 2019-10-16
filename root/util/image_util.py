#!/usr/bin/python
import imageio
import numpy as np

_MIN_PIXEL = 0
_MAX_PIXEL = 255


class ImageUtil():
<<<<<<< HEAD

    @staticmethod
    def read_image(image_path, type="RGB"):
=======
    @staticmethod
    def isGrayScale(img):
        if len(img.shape) == 2:
            return True
        return False

    @staticmethod
    def isRgb(img):
        if len(img.shape) == 3:
            return True
        return False

    @staticmethod
    def read_image(image_path, type="RGBA"):
>>>>>>> merge_frontend_develop
        return imageio.imread(image_path, as_gray=False, pilmode=type)

    @staticmethod
    def save_image(name, image_as_byte):
        imageio.imwrite(name, image_as_byte)

    @staticmethod
    def normalize_image(img):
        min_input = img.min()
        max_input = img.max()

        min_output = _MIN_PIXEL
        max_output = _MAX_PIXEL
        return (img - min_input) * ((max_output - min_output) / (max_input - min_input) + min_output)

    @staticmethod
    def get_empty_image_with_same_dimensions(img):
        height, width = ImageUtil.get_dimensions(img)
        empty_image = np.zeros((height, width), np.uint8)
        return empty_image, img

    @staticmethod
    def get_dimensions(img):
        data = np.array(img)
        height = data.shape[0]
        try:
            width = data.shape[1]
        except:
            width = 1
        return height, width

    @staticmethod
    def format_filter_size(size):
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
