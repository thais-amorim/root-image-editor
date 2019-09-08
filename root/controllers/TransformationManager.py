    
from ImageManager import ImageManager

_max_pixel = 255
_images_path = 'images/'

class  TransformationManager(ImageManager):

    def __init__(self):
        super().__init__()

    def apply_negative(self,img_name, img):
        negative = _max_pixel - img
        self.save_image(img_name, negative.astype('uint8'))

    def apply_logarithmic(self,img_name, img):
        max_obtained = np.max(img)
        c = (_max_pixel/np.log(1+max_obtained))
        log_img = c * np.log(1+img)
        self.save_image(img_name, log_img.astype('uint8'))

    def apply_gamma_correction(self,img_name, img, gamma):
        gamma_correction = ((img/_max_pixel) ** (1/gamma))
        self.save_image(img_name, gamma_correction)



f = TransformationManager()
img = f.read_image("images/einstein.jpg")
img = f.rgb_to_gray(img)
#save_image("save_test.jpg", img.copy())
f.apply_negative("results/negative_test.jpg", img.copy())
#apply_logarithmic("log_test.jpg", img.copy())
#apply_gamma_correction("gamma_test.jpg", img.copy(), 1.5)
#draw_histogram("histogram_test.jpg", img.copy())
#apply_equalized_histogram("eq_test.jpg", img.copy())
#apply_median(img.copy(), -5, "median2.jpg")

# coordinates_x = np.array([0,10,11,13,14,255])
# coordinates_y = np.array([0,10,11,100,101,255])
# apply_piecewise_linear("piecewise_linear.jpg",img.copy(),coordinates_x,coordinates_y)