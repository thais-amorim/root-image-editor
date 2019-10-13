import numpy as np


class RgbUtil():

    @staticmethod
    def get_rgb_layers(rgb):
        r = rgb[:, :, 0]
        g = rgb[:, :, 1]
        b = rgb[:, :, 2]

        return r, g, b

    @staticmethod
    def merge_rgb_layers(red_layer, green_layer, blue_layer):
        return np.stack([red_layer, green_layer, blue_layer], axis=2)
