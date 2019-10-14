
from TransformationManager import TransformationManager
import numpy as np

from filter import ImageFilter as filter
from filter import ColorFilter as color
from converter import ColorConverter as converter


class TransformationController():

    def __init__(self):
        super().__init__()
        self.original_image = self.current_image = self.undo_image = None
    
    def getCurrentImage(self):
        return self.current_image

    def undoAction(self):
        self.current_image = self.undo_image
        return self.current_image

    def loadImage(self,image):
        img = filter.read_image(image)
        self.original_image = converter.rgb_to_gray(img)
        self.current_image = self.original_image
        self.undo_image = self.original_image
        return self.current_image

    def negativeTransform(self):
        self.undo_image = self.current_image
        self.current_image  = (filter.apply_negative(self.current_image)).astype(np.uint8)
        return self.current_image

    def logarithmicTransform(self):
        self.undo_image = self.current_image
        self.current_image  = filter.apply_logarithmic(self.current_image)
        return self.current_image

    def gammaTransform(self,gamma):
        self.undo_image = self.current_image
        self.current_image  = filter.apply_gamma_correction(self.current_image, gamma)
        return self.current_image

    def apply_equalized_histogram(self,img_name, img):
        #TODO
        return None
    def apply_median(self,img, filter_size, img_name):
        #TODO
        return None

    def apply_piecewise_linear(self,img_name, img, coordinates_x, coordinates_y):
        #TODO
        return None
