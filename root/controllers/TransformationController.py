
from TransformationManager import TransformationManager
import numpy as np

from filter import ImageFilter as filter
from filter import ColorFilter as color
from converter import ColorConverter as converter


class TransformationController():

    def __init__(self):
        super().__init__()
        self.original_image = self.current_image = self.undo_image  = self.redo_image = None
    
    def update_memory_images(self,image):
        self.undo_image = self.current_image
        self.current_image  = image
        self.redo_image = self.current_image

    def getCurrentImage(self):
        return self.current_image

    def undoAction(self):
        self.current_image = self.undo_image
        return self.current_image

    def redoAction(self):
        self.current_image = self.redo_image
        return self.current_image


    def loadImage(self,image):
        img = filter.read_image(image)
        self.original_image = img
        if len(img.shape) == 2:
            self.original_image = converter.rgb_to_gray(self.original_image)
        self.current_image = self.original_image
        self.undo_image = self.original_image
        self.redo_image = self.original_image
        return self.current_image

    def negativeTransform(self):
        image  = (filter.apply_negative(self.current_image)).astype(np.uint8)
        self.update_memory_images(image)
        return self.current_image

    def logarithmicTransform(self):
        image  = filter.apply_logarithmic(self.current_image)
        self.update_memory_images(image)
        return self.current_image

    def gammaTransform(self,gamma):
        image  = filter.apply_gamma_correction(self.current_image, gamma)
        self.update_memory_images(image)
        return self.current_image

    def apply_equalized_histogram(self):
        image = filter.apply_equalized_histogram(self.current_image)
        self.update_memory_images(image)
        return self.current_image

    def apply_median(self,filter_size):
        image = filter.apply_median(self.current_image, filter_size)
        self.update_memory_images(image)
        return self.current_image


    def apply_convolution(self, filter_matrix):
        image = filter.apply_convolution(self.current_image,filter_matrix)
        self.update_memory_images(image)
        return self.current_image

    def apply_sobel(self):
        image = filter.apply_sobel(self.current_image)
        self.update_memory_images(image)
        return self.current_image

    def apply_gradient(self, filter_matrix):
        image = filter.apply_gradient(self.current_image, filter_matrix)
        self.update_memory_images(image)
        return self.current_image
    def apply_arithmetic_mean(self, filter_size=3):
        image = filter.apply_arithmetic_mean(self.current_image,filter_size)
        self.update_memory_images(image)
        return self.current_image

    def apply_geometric_mean(self, filter_size=3):
        image = filter.apply_geometric_mean(self.current_image,filter_size)
        self.update_memory_images(image)
        return self.current_image

    def apply_harmonic_mean(self, filter_size):
        image = filter.apply_harmonic_mean(self.current_image,filter_size)
        self.update_memory_images(image)
        return self.current_image

    def apply_contra_harmonic_mean(self, filter_size,q):
        image = filter.apply_contra_harmonic_mean(self.current_image,filter_size,q)
        self.update_memory_images(image)
        return self.current_image

    def apply_highboost(self, filter_size,c):
        image = filter.apply_contra_harmonic_mean(self.current_image,c,filter_size)
        self.update_memory_images(image)
        return self.current_image

    def rgb_to_gray(self):
        if len(self.current_image.shape) == 3:
            image = converter.rgb_to_gray(self.original_image)
            self.update_memory_images(image)
        return self.current_image

    def rgb_to_hsv(self):
        if len(self.current_image.shape) == 3:
            r,g,b = color.get_rgb_layers(self.original_image)
            image = converter.rgb_to_hsv(r,g,b)
            self.update_memory_images(image)
        return self.current_image
    
    def apply_sepia(self):
        if len(self.current_image.shape) == 3:
            image =  color.apply_sepia(self.current_image)
            self.update_memory_images(image)
            return self.current_image


    # def rgb_to_hsv(self):
    #     if len(self.current_image.shape) == 3:
    #         image = converter.rgb_to_hsv(self.original_image)
    #         self.update_memory_images(image)
    #     return self.current_image

    def apply_piecewise_linear(self,img_name, img, coordinates_x, coordinates_y):
        #TODO
        return None

  
