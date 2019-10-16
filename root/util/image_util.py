#!/usr/bin/python
import imageio
import numpy as np
from PIL import Image
import numpy
_MIN_PIXEL = 0
_MAX_PIXEL = 255


class ImageUtil():
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
    def read_image(image_path, type="RGB"):
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
        # height, width = ImageUtil.get_dimensions(img)
        # empty_image = np.zeros((height, width), np.uint8)
        empty_image = np.zeros(np.shape(img))
        return empty_image, img

    @staticmethod
    def get_image_dimensions(img):
        data = np.array(img)
        height = data.shape[0]
        try:
            width = data.shape[1]
        except:
            width = 1
        return height, width

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

    @staticmethod
    def fig2data ( fig ):
        """
        @brief Convert a Matplotlib figure to a 4D numpy array with RGBA channels and return it
        @param fig a matplotlib figure
        @return a numpy 3D array of RGBA values
        """
        # draw the renderer
        fig.canvas.draw ( )
    
        # Get the RGBA buffer from the figure
        w,h = fig.canvas.get_width_height()
        buf = numpy.fromstring ( fig.canvas.tostring_argb(), dtype=numpy.uint8 )
        buf.shape = ( w, h,4 )
    
        # canvas.tostring_argb give pixmap in ARGB mode. Roll the ALPHA channel to have it in RGBA mode
        buf = numpy.roll ( buf, 3, axis = 2 )
        return buf


    
    @staticmethod
    def fig2img ( fig ):
        """
        @brief Convert a Matplotlib figure to a PIL Image in RGBA format and return it
        @param fig a matplotlib figure
        @return a Python Imaging Library ( PIL ) image
        """
        # put the figure pixmap into a numpy array
        buf = ImageUtil.fig2data ( fig )
        w, h, d = buf.shape
        return numpy.asarray(Image.frombytes( "RGBA", ( w ,h ), buf.tostring( ) ))