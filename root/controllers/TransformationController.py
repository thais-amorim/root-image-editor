
from TransformationManager import TransformationManager
import numpy as np
class TransformationController():

    def __init__(self):
        super().__init__()
        self.original_image = self.current_image = self.undo_image = None
        
        self.transform = TransformationManager()
    
    def getCurrentImage(self):
        return self.current_image

    def undoAction(self):
        self.current_image = self.undo_image
        return self.current_image

    def loadImage(self,image):
        img = self.transform.read_image(image)
        self.original_image = self.transform.rgb_to_gray(img)
        self.current_image = self.original_image
        self.undo_image = self.original_image
        return self.current_image

    def normalize(self, img):
        return np.interp(img, (img.min(), img.max()), (0, 255))

    def negativeTransform(self):
        self.undo_image = self.current_image
        self.current_image  = (self.transform.apply_negative(self.current_image)).astype(np.uint8)
        return self.current_image

    def logarithmicTransform(self):
        self.undo_image = self.current_image
        self.current_image  = self.transform.apply_logarithmic(self.current_image)
        return self.current_image

    def gammaTransform(self,gamma):
        self.undo_image = self.current_image
        self.current_image  = self.transform.apply_gamma_correction(self.current_image, gamma)
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
