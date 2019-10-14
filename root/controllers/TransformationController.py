
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
        self.original_image = converter.rgb_to_gray(img)
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

    def apply_piecewise_linear(self,img_name, img, coordinates_x, coordinates_y):
        #TODO
        return None
    def apply_convolution(self, filter_matrix):
        
        # import numpy as np
        # filter_matrix = np.array([[0,0.2,0], [0.2,0.2,0.2], [0,0.2,0]])
        # print('array dtype')
        # print(type(filter_matrix.dtype))
        # print(filter_matrix)
        image = filter.apply_convolution(self.current_image,filter_matrix)
        self.update_memory_images(image)
        return self.current_image

    def apply_sobel(self):
        image = filter.apply_sobel(self.current_image)
        self.update_memory_images(image)
        return self.current_image