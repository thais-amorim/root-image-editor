import imageio
import numpy as np
from . import ImageFilter
from PIL import Image
from skimage import img_as_ubyte
import math

class ColorFilter():

    @staticmethod
    def get_rgb_layers(rgb):
        r = rgb[:, :, 0]
        g = rgb[:, :, 1]
        b = rgb[:, :, 2]

        return r, g, b

    @staticmethod
    def merge_rgb_layers(red_layer, green_layer, blue_layer):
        return np.stack([red_channel, green_channel, blue_channel], axis=2)

    @staticmethod
    def normalize_max_value(value, pixel):
        if value > 255:
            pixel = 255
        else:
            pixel = value
        return pixel

    @staticmethod
    def apply_sepia(img):
        height, width = ImageFilter.get_image_dimensions(img)
        obtained, img = ImageFilter.get_empty_image_with_same_dimensions(img)
        r_matrix, g_matrix, b_matrix = ColorFilter.get_rgb_layers(img)
        for i in range(height):
            for j in range(width):
                r, g, b = r_matrix[i][j], g_matrix[i][j], b_matrix[i][j]
                tr = int(0.393 * r + 0.769 * g + 0.189 * b)
                tg = int(0.349 * r + 0.686 * g + 0.168 * b)
                tb = int(0.272 * r + 0.534 * g + 0.131 * b)

                r = ColorFilter.normalize_max_value(tr, r)
                g = ColorFilter.normalize_max_value(tg, g)
                b = ColorFilter.normalize_max_value(tb, b)

                obtained[i][j] = [r, g, b]

        return obtained

    @staticmethod
    def remove_green_background(img):
        '''
        Remove green background from a image. First step to use Chroma-Key color filter.
        Input: img as a numpy.array containing 4 channel image (RGBA).
        Output: img without green background
        '''
        max_pixel_value = 255

        """
        Obtain the ratio of the green/red/blue
        channels based on the max pixel value.
        """
        red_ratio = img[:, :, 0] / max_pixel_value
        green_ratio = img[:, :, 1] / max_pixel_value
        blue_ratio = img[:, :, 2] / max_pixel_value

        """
        Darker pixels would be around 0.
        In order to ommit removing dark pixels we
        sum .28 to make small negative numbers to be
        above 0.
        """
        red_vs_green = (red_ratio - green_ratio) + .28
        blue_vs_green = (blue_ratio - green_ratio) + .28

        """
        Now pixels below 0. value would have a
        high probability to be background green
        pixels.
        """
        red_vs_green[red_vs_green < 0] = 0
        blue_vs_green[blue_vs_green < 0] = 0

        """
        Combine the red(blue) vs green ratios to
        set an alpha layer with valid alpha-values.
        """
        alpha = (red_vs_green + blue_vs_green) * 255
        alpha[alpha > 50] = 255

        img[:, :, 3] = alpha

        return img

    @staticmethod
    def add_background(background, img, coord=(0, 0)):
        img = img_as_ubyte(img)
        x_size, y_size = ImageFilter.get_image_dimensions(img)

        (y_begin, x_begin) = coord
        x_end = x_begin + x_size
        y_end = y_begin + y_size

        background_crop = background[
            x_begin:x_end,
            y_begin:y_end,
            :]

        pixel_preserve = (img[:, :, 3] > 10)
        background_crop[pixel_preserve] = img[pixel_preserve]

        background[x_begin:x_end, y_begin:y_end, :] = background_crop

        return background

    # @staticmethod
    # def apply_chroma_key(background, img, coord=(0, 0)):
    #     obtained = ColorFilter.remove_green_background(img)
    #     return ColorFilter.add_background(background, obtained, coord)
    @staticmethod
    def dist(x0, y0, x1, y1):
        return math.sqrt((x1 - x0)**2 + (y1 - y0)**2)

    @staticmethod
    def apply_chroma_key(background,image, faixa=50):
        max_pixel_value = 255
        img= image.copy()
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                r, g, b = img[i,j,0], img[i,j,1], img[i,j,2]
                """
                Obtain the ratio of the green/red/blue
                channels based on the max pixel value.
                """
                red_ratio = r / max_pixel_value
                green_ratio = g / max_pixel_value
                blue_ratio = b / max_pixel_value

                """Darker pixels would be around 0.
                In order to ommit removing dark pixels we
                sum .28 to make small negative numbers to be
                above 0.
                """
                red_vs_green = (red_ratio - green_ratio) + .28
                blue_vs_green = (blue_ratio - green_ratio) + .28
                if red_vs_green < 0:
                    red_vs_green = 0
                if blue_vs_green < 0:
                    blue_vs_green = 0
                alpha =  red_vs_green + blue_vs_green * max_pixel_value
            
                if (alpha <= faixa):
                    img[i,j,0] = background[i,j,0] 
                    img[i,j,1] = background[i,j,1]
                    img[i,j,2] = background[i,j,2]

        return img
