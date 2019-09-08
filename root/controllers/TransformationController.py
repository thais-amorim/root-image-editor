
from TransformationManager import TransformationManager
class TransformationController():

    def __init__(self):
        super().__init__()
        self.original_image = self.current_image = None

        self.transform = TransformationManager()
    
    def getCurrentImage(self):
        return self.current_image

    def loadImage(self,image):
        img = self.transform.read_image(image)
        self.original_image = self.transform.rgb_to_gray(img)
        self.current_image = self.original_image
        return self.current_image

    def negativeTransform(self):
        self.current_image  = self.transform.apply_negative(self.current_image)
        return self.current_image

    def logarithmicTransform(self):
        self.current_image  = self.transform.apply_logarithmic(self.current_image)
        return self.current_image

    def gammaTransform(self,gamma):
        self.current_image  = self.transform.apply_gamma(self.current_image, gamma)
       return self.current_image


