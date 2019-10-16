from root.controller import ImageManager
import numpy as np

_max_pixel = 255
_images_path = 'images/'

class  TransformationManager(ImageManager):

    def __init__(self):
        super().__init__()

    def apply_negative(self, img):
        print(img)
        negative = _max_pixel - img
        print(negative)
        return negative
        # self.save_image(img_name, negative)

    def apply_logarithmic(self, img):
        max_obtained = np.max(img)
        c = (_max_pixel/np.log(1+_max_pixel))
        log_img = c * np.log(img.astype(np.double)+1)
        return log_img.astype(np.uint8)
        # self.save_image(img_name, log_img.astype('uint8'))

    def apply_gamma_correction(self,img, gamma):
        c = _max_pixel / (1+ _max_pixel)**gamma
        gamma_correction = c * (img**gamma)
        # gamma_correction = ((img/_max_pixel) ** (1/gamma))
        return gamma_correction
        # self.save_image(img_name, gamma_correction)

