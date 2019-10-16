import numpy as np

from filter import ImageFilter as filter
from filter import ColorFilter as color
from filter import SteganographyTool as stegano
from converter import ColorConverter as converter
from converter import ScaleConverter as scal
from FourierManager import FourierManager

class TransformationController():

    def __init__(self):
        super().__init__()
        self.original_image = self.current_image = self.undo_image  = self.redo_image = None
        self.complete_fourier  = self.current_complete_fourier = self.fourier_image = self.undo_fourier = self.redo_fourier = None
        self.fourierManager = FourierManager()

    def update_memory_images(self,image):
        self.undo_image = self.current_image
        self.current_image  = image
        self.redo_image = self.current_image.copy()
    
    def update_fourier_memory_images(self,image):
        self.undo_fourier = self.fourier_image
        self.fourier_image  = image
        self.redo_fourier = self.fourier_image.copy()

    def getCurrentImage(self):
        return self.current_image

    def undoAction(self):
        self.current_image = self.undo_image
        return self.current_image

    def redoAction(self):
        self.current_image = self.redo_image
        return self.current_image

    def undoFourierAction(self):
        self.fourier_image = self.undo_fourier
        return self.fourier_image

    def redoFourierAction(self):
        self.fourier_image = self.redo_fourier
        return self.fourier_image

    def openImage(self,image):
        img = filter.read_image(image)
        if len(img.shape) == 2:
            img = converter.rgb_to_gray(self.original_image)
        return img

    def loadImage(self,image):
        self.update_memory_images(self.openImage(image))
        return self.current_image

    def saveImage(self, name,image):
        filter.save_image(name,image)
    
    def save(self, name):
        filter.save_image(name,self.current_image)


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
        # print("RGBA:")
        print(self.current_image.shape)
        # print("Shape é RGBA")
        img =self.current_image
        print(img.shape)
        image = converter.rgb_to_gray(img)
        self.update_memory_images(image)
        return self.current_image

    def rgb_to_hsv(self):
        if len(self.current_image.shape) == 3:
            r,g,b = color.get_rgb_layers(self.original_image)
            image = converter.rgb_to_hsv(r,g,b)
            self.update_memory_images(image)
        return self.current_image
    
    def apply_fourier(self):
        ft = self.fourierManager.fft2(self.current_image)
        shift = self.fourierManager.fftshift(ft)
        self.fourier_image = shift
        self.current_complete_fourier = shift.copy()
        mag = abs(shift)
        mag = np.log(mag)
        mag = filter.normalize_image(mag)
        mag = mag.astype(np.uint8).copy()
        
        self.update_fourier_memory_images(mag)

        return self.fourier_image

    def apply_low_pass(self, radius):
        image = self.fourierManager.lowPassFilter(self.fourier_image,radius)
        # self.current_complete_fourier = self.fourierManager.lowPassFilter(self.current_complete_fourier,radius)
        self.update_fourier_memory_images(image)
        return self.fourier_image
        
    def apply_high_pass(self, radius):
        image = self.fourierManager.highPassFilter(self.fourier_image,radius)
        # self.current_complete_fourier = self.fourierManager.highPassFilter(self.current_complete_fourier,radius)
        self.update_fourier_memory_images(image)
        return self.fourier_image

    def apply_band_pass(self, radius_minor,radius_major):
        image = self.fourierManager.bandPassFilter(self.fourier_image,radius_minor,radius_major)
        self.update_fourier_memory_images(image)
        return self.fourier_image

    def apply_inverse_fourier(self):
        shift = self.current_complete_fourier
        shift[np.where (self.fourier_image  == 0)] = 0
        ishift = self.fourierManager.ifftshift(shift)
        p_img = abs(self.fourierManager.ifft2(ishift))
        # image = self.fourierManager
        return p_img 

    def apply_sepia(self):
        if len(self.current_image.shape) == 3:
            image =  color.apply_sepia(self.current_image)
            self.update_memory_images(image)
            return self.current_image


    def apply_chroma_key(self,background,faixa =30):
        if len(self.current_image.shape) == 3:
            image =  color.apply_chroma_key(background, self.current_image,faixa)
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

    def steganograph_encode(self, image,text):
        return stegano.encode(image, text)

    def steganograph_decode(self, image):
        return stegano.decode(image)

    def apply_scale_nearest(self, scale):
        image = scal.apply_nearest_neighbour(self.current_image,scale)
        self.update_memory_images(image)
        return self.current_image

    def apply_scale_bilinear(self, scale):
        image = scal.apply_bilinear_interpolation(self.current_image,scale)
        self.update_memory_images(image)
        return self.current_image

    def apply_rotation_nearest(self, angle):
        image = scal.apply_rotate_nearest(self.current_image,angle)
        self.update_memory_images(image)
        return self.current_image
        
    def apply_rotate_bilinear(self, angle):
        image = scal.apply_rotate_bilinear(self.current_image,angle)
        self.update_memory_images(image)
        return self.current_image