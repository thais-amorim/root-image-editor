from root.filter import ImageFilter as filter
from root.util import RgbUtil as rgb


class RgbFilter():

    @staticmethod
    def apply_negative(img):
        r, g, b = rgb.get_rgb_layers(img)
        r = filter.apply_negative(r)
        g = filter.apply_negative(g)
        b = filter.apply_negative(b)
        obtained = rgb.merge_rgb_layers(r, g, b)
        return rgb.merge_rgb_layers(r, g, b)

    @staticmethod
    def apply_logarithmic(img):
        r, g, b = rgb.get_rgb_layers(img)
        r = filter.apply_logarithmic(r)
        g = filter.apply_logarithmic(g)
        b = filter.apply_logarithmic(b)
        obtained = rgb.merge_rgb_layers(r, g, b)
        return rgb.merge_rgb_layers(r, g, b)

    @staticmethod
    def apply_gamma_correction(img, gamma):
        r, g, b = rgb.get_rgb_layers(img)
        r = filter.apply_gamma_correction(r, gamma)
        g = filter.apply_gamma_correction(g, gamma)
        b = filter.apply_gamma_correction(b, gamma)
        return rgb.merge_rgb_layers(r, g, b)

    @staticmethod
    def draw_histogram(img, img_name):
        r, g, b = rgb.get_rgb_layers(img)
        r = filter.draw_histogram(r, img_name + "_red" + ".jpg", "r")
        g = filter.draw_histogram(g, img_name + "_green" + ".jpg", "g")
        b = filter.draw_histogram(b, img_name + "_blue" + ".jpg", "b")
