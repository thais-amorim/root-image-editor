import imageio
import numpy as np
from root.util import ImageUtil as util
from root.util import RgbUtil as rgb
from PIL import Image
from skimage import img_as_ubyte


class ColorFilter():

    @staticmethod
    def __normalize_max_value(value, pixel):
        if value > 255:
            pixel = 255
        else:
            pixel = value
        return pixel

    @staticmethod
    def apply_sepia(img):
        height, width = util.get_image_dimensions(img)
        obtained, img = util.get_empty_image_with_same_dimensions(img)
        r_matrix, g_matrix, b_matrix = rgb.get_rgb_layers(img)
        for i in range(height):
            for j in range(width):
                r, g, b = r_matrix[i][j], g_matrix[i][j], b_matrix[i][j]
                tr = int(0.393 * r + 0.769 * g + 0.189 * b)
                tg = int(0.349 * r + 0.686 * g + 0.168 * b)
                tb = int(0.272 * r + 0.534 * g + 0.131 * b)

                r = ColorFilter.__normalize_max_value(tr, r)
                g = ColorFilter.__normalize_max_value(tg, g)
                b = ColorFilter.__normalize_max_value(tb, b)

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
        x_size, y_size = util.get_image_dimensions(img)

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

    @staticmethod
    def apply_chroma_key(background, img, coord=(0, 0)):
        obtained = ColorFilter.remove_green_background(img)
        return ColorFilter.add_background(background, obtained, coord)

    @staticmethod
    def adjust_brightness (img, br):
        """
        0 < br < 1: decrease brightness
        br = 1: no changes
        br >: increase brightness
        """
        height,width = util.get_dimensions(img)
        obtained = np.zeros((height, width, 3), np.uint8)

        for i in range(height):
            for j in range(width):
                for k in range(img.shape[2]):
                    b = img[i][j][k] * br
                    if b > 255:
                        b = 255
                    obtained[i][j][k] = b
        return obtained.astype(np.uint8)
