#!/usr/bin/python
import imageio
import matplotlib.pyplot as plt
import numpy as np
from root.util import ImageUtil as util
from PIL import Image

_MIN_PIXEL = 0
_MAX_PIXEL = 255


class ImageFilter():

    @staticmethod
    def isGrayScale(img):
        if len(img.shape) == 2:
            return True
        return False

    @staticmethod
    def isRGB(img):
        if len(img.shape) == 3:
            return True
        return False

    @staticmethod
    def read_image(image_path, type="RGB"):
        return imageio.imread(image_path, as_gray=False, pilmode=type)

    @staticmethod
    def save_image(name, image_as_byte):
        imageio.imwrite(name, image_as_byte)

    @staticmethod
    def normalize_image(img):
        min_input = img.min()
        max_input = img.max()

        min_output = _MIN_PIXEL
        max_output = _MAX_PIXEL
        return (img - min_input) * ((max_output - min_output) / (max_input - min_input) + min_output)

    @staticmethod
    def apply_negative(img):
        if len(img.shape) == 2:
            return _MAX_PIXEL - img
        else:
            i = img.copy()
            i[:,:,0] = _MAX_PIXEL - img[:,:,0]
            i[:,:,1]= _MAX_PIXEL - img[:,:,1]
            i[:,:,2] = _MAX_PIXEL - img[:,:,2]
            return i

    @staticmethod
    def apply_logarithmic(img,c = 0):
        max_obtained = np.max(img)
        if c == 0:
            c = (_MAX_PIXEL/np.log(1+_MAX_PIXEL))
        log_img = c * np.log(img.astype(np.double)+1)
        return log_img.astype(np.uint8)

    @staticmethod
    def apply_gamma_correction(img, gamma):
        c = _MAX_PIXEL / (1+ _MAX_PIXEL)**gamma
        gamma_correction = c * (img**gamma)
        return gamma_correction

    @staticmethod
    def draw_histogram(img, img_name, color="black"):
        data = img.flatten()
        plt.hist(data, _MAX_PIXEL + 1, [0, 256], color=color, ec=color)
        plt.grid(axis='y', alpha=0.75)
        plt.xlabel('Pixel value')
        plt.ylabel('Amount')
        plt.savefig(img_name)
        plt.close()

    @staticmethod
    def histogram(image, bins=256):
        if len(image.shape) == 2:  # Grayscale Image
            hist = np.zeros(bins, dtype=np.int)
            flat = np.asarray(image)
            flat = flat.flatten()

            for pxl in flat:
                hist[int(round(pxl,5))] += 1

            return hist
        else:  # RGB Image
            r, g, b = np.zeros(bins), np.zeros(bins), np.zeros(bins)
            for row in range(image.shape[0]):
                for col in range(image.shape[1]):
                    r[image[row, col][0]] += 1
                    g[image[row, col][1]] += 1
                    b[image[row, col][2]] += 1

            return (r, g, b)

    @staticmethod
    def apply_histogram_equalization(img):
        # Getting the pixel values of the image
        original = np.array(img)
        # Creating a new matrix for the image
        equalized_img = np.copy(original)
        # Getting unique pixels and frequency of the values from the image
        unique_pixels, pixels_frequency = np.unique(
            original, return_counts=True)
        # Image pixels divided by the size of the image
        pk = pixels_frequency / img.size
        pk_length = len(pk)
        # Getting the cummulative frequency of the unique pixel values
        sk = np.cumsum(pk)
        # Multiplying the cummulative frequency by the maximum value of the pixels
        mul = sk * np.max(original)
        roundVal = np.round(mul)
        if len(img.shape) == 2:
            # Mapping the pixels for the equalization
            for i in range(len(original)):
                for j in range(len(original[0])):
                    equalized_img[i][j] = roundVal[np.where(
                        unique_pixels == original[i][j])]
        else:
            R = ImageFilter.apply_histogram_equalization(img[:,:,0])
            G = ImageFilter.apply_histogram_equalization(img[:,:,1])
            B = ImageFilter.apply_histogram_equalization(img[:,:,2])
            output = np.zeros((R.shape[0], R.shape[1], 3), dtype=np.uint8)
            output[:,:,0] = R
            output[:,:,1] = G
            output[:,:,2] = B
            equalized_img = output

        return equalized_img
    
    
    
    # @staticmethod
    # def equalize_hist(image, hist):
    #     if len(image.shape) == 2:  # Grayscale Image
    #         hist = histogram(image)
            
    #         x = iter(hist)
    #         y = [next(x)]

    #         for i in x:
    #             y.append(y[-1] + i)

    #         y = np.array(y)
    #         y = ((y - y.min()) * 255) / (y.max() - y.min())
    #         y = y.astype(np.uint8)
    #         cdf = y

    #         img = (np.asarray(image)).flatten()
    #         flat = np.zeros_like(img, dtype=np.uint8)
    #         for i in range(len(flat)):
    #             flat[i] = int(round(img[i],5))
    #         output = cdf[flat]
    #         output = np.reshape(output, image.shape)
    #         output[np.where(output > MAX_PIXEL)] = MAX_PIXEL

    #         return output.astype(np.uint8)
    #     else:
    #         R = ImageFilter.equalize_hist(hist)
    #         G = ImageFilter.equalize_hist(hist)
    #         B = ImageFilter.equalize_hist(hist)
    #         output = np.zeros((R.shape[0], R.shape[1], 3), dtype=np.uint8)
    #         output[:,:,0] = R
    #         output[:,:,1] = G
    #         output[:,:,2] = B
    #         obtained = output

    #         return obtained


    @staticmethod
    def __get_neighbors_matrix(filter_size, i, j, data):
        mid_position = filter_size // 2
        neighbors = []
        for z in range(filter_size):
            if i + z - mid_position < 0 or i + z - mid_position > len(data) - 1:
                for c in range(filter_size):
                    neighbors.append(0)
            elif j + z - mid_position < 0 or j + mid_position > len(data[0]) - 1:
                neighbors.append(0)
            else:
                for k in range(filter_size):
                    neighbors.append(data[i + z - mid_position]
                                     [j + k - mid_position])

        return neighbors

    @staticmethod
    def get_median(filter_size, i, j, data):
        mid_position = filter_size // 2
        neighbors = ImageFilter.__get_neighbors_matrix(filter_size, i, j, data)
        neighbors.sort()
        return neighbors[len(neighbors) // 2]

    @staticmethod
    def apply_median(img, filter_size):
        filter_size = util.format_filter_size(filter_size)
        obtained, original = util.get_empty_image_with_same_dimensions(
            img)
        if len(img.shape) == 2:
            for i in range(len(original)):
                for j in range(len(original[0])):
                    obtained[i][j] = ImageFilter.get_median(
                        filter_size, i, j, original)
        else:
            R = ImageFilter.apply_median(img[:,:,0],filter_size)
            G = ImageFilter.apply_median(img[:,:,1],filter_size)
            B = ImageFilter.apply_median(img[:,:,2],filter_size)
            output = np.zeros((R.shape[0], R.shape[1], 3), dtype=np.uint8)
            output[:,:,0] = R
            output[:,:,1] = G
            output[:,:,2] = B
            obtained = output
        return obtained

    @staticmethod
    def apply_piecewise_linear(img, coordinates_x, coordinates_y):
        """Apply Piecewise Linear filter on an image basead on an group of coordinates.

        Parameters
        ----------
        img : numpy array
            The target image where the filter would be applied
        coordinates_x : array
            The coordinates X from all points to the interpolated already in the desired order.
        coordinates_y : array
            The coordinates Y from all points to the interpolated already in the desired order.

        Returns
        -------
        numpy array
            an array representing the obtained image after apply the filter
        """
        x = np.array(range(0, _MAX_PIXEL + 1), dtype=np.uint8)
        interp = np.interp(x, coordinates_x, coordinates_y)
        obtained = img.copy()
        height, width = util.get_dimensions(obtained)
        if len(img.shape) == 2:
            for i in range(height):
                for j in range(width):
                    index = int(np.round(obtained[i][j]))
                    obtained[i][j] = interp[index]
        else:
            R = ImageFilter.apply_piecewise_linear(img[:,:,0],coordinates_x, coordinates_y)
            G = ImageFilter.apply_piecewise_linear(img[:,:,1],coordinates_x, coordinates_y)
            B = ImageFilter.apply_piecewise_linear(img[:,:,2],coordinates_x, coordinates_y)
            output = np.zeros((R.shape[0], R.shape[1], 3), dtype=np.uint8)
            output[:,:,0] = R
            output[:,:,1] = G
            output[:,:,2] = B
            obtained = output

        return obtained

    @staticmethod
    def apply_convolution(img, filter_matrix):
        obtained, original = util.get_empty_image_with_same_dimensions(
            img)
        height, width =  util.get_dimensions(img)
        #Se for grayscale
        if len(img.shape) == 2:
            for row in range(1, height - 1):
                for col in range(1, width - 1):
                    value = filter_matrix * \
                        img[(row - 1):(row + 2), (col - 1):(col + 2)]
                    max_obtained_value = max(0, value.sum())
                    obtained[row, col] = min(max_obtained_value, _MAX_PIXEL)
        else:
            channel = img.shape[2]
            for c in range (channel):
                for row in range(1, height - 1):
                    for col in range(1, width - 1):
                        value = filter_matrix * \
                            img[(row - 1):(row + 2), (col - 1):(col + 2),c]
                        max_obtained_value = max(0, value.sum())
                        obtained[row, col,c] = min(max_obtained_value, _MAX_PIXEL)
        return obtained

    @staticmethod
    def apply_laplacian(img):
        kernel = np.array([
            [-1, -1, -1],
            [-1,  8, -1],
            [-1, -1, -1]])

        obtained = ImageFilter.apply_convolution(img, kernel)

        norm_obtained = util.normalize_image(obtained)
        sharpened = img + norm_obtained
        norm_sharpened = util.normalize_image(sharpened)
        return norm_obtained, norm_sharpened

    @staticmethod
    def create_gaussian_kernel(filter_size, sigma):
        """
        Creates a 2D gaussian kernel using filter_size and sigma
        """
        filter_size = util.format_filter_size(filter_size)
        ax = np.linspace(-(filter_size - 1) / 2.,
                         (filter_size - 1) / 2., filter_size)
        xx, yy = np.meshgrid(ax, ax)

        kernel = np.exp(-0.5 * (np.square(xx) +
                                np.square(yy)) / np.square(sigma))

        return kernel / np.sum(kernel)

    @staticmethod
    def apply_gaussian(img, filter_size=3, sigma=1.):
        kernel = ImageFilter.create_gaussian_kernel(filter_size, sigma)
        return ImageFilter.apply_convolution(img, kernel)

    @staticmethod
    def apply_sobel(img):
        # Horizontal sobel matrix
        horizontal = np.array([
            [-1,    0,    1],
            [-2,    0,    2],
            [-1,    0,    1]])

        # Vertical sobel matrix
        vertical = np.array([
            [-1,   -2,    -1],
            [0,     0,     0],
            [1,     2,     1]])

        height, width = util.get_dimensions(img)

        # define images with 0s
        new_horizontal_image = np.zeros((height, width), np.uint8)
        new_vertical_image = np.zeros((height, width), np.uint8)
        new_gradient_image = np.zeros((height, width), np.uint8)
        if len(img.shape) == 2:
            # # define images with 0s
            # new_horizontal_image = np.zeros((height, width), np.uint8)
            # new_vertical_image = np.zeros((height, width), np.uint8)
            # new_gradient_image = np.zeros((height, width), np.uint8)
            for i in range(1, height - 1):
                for j in range(1, width - 1):
                    horizontal_grad = ImageFilter.apply_gradient_core(
                        horizontal, img, i, j)
                    new_horizontal_image[i - 1, j - 1] = abs(horizontal_grad)

                    vertical_grad = ImageFilter.apply_gradient_core(
                        vertical, img, i, j)
                    new_vertical_image[i - 1, j - 1] = abs(vertical_grad)

                    # Edge Magnitude
                    new_gradient_image[i - 1, j - 1] = np.sqrt(
                        pow(horizontal_grad, 2.0) + pow(vertical_grad, 2.0))
        else:
            new_gradient_image = np.zeros((height, width,3), np.uint8)
            channel = img.shape[2]
            for c in range (channel-1):
                for i in range(1, height - 1):
                    for j in range(1, width - 1):
                        horizontal_grad = ImageFilter.apply_gradient_core(
                            horizontal, img[:,:,c], i, j)
                        new_horizontal_image[i - 1, j - 1] = abs(horizontal_grad)

                        vertical_grad = ImageFilter.apply_gradient_core(
                            vertical, img[:,:,c], i, j)
                        new_vertical_image[i - 1, j - 1] = abs(vertical_grad)

                        # Edge Magnitude
                        new_gradient_image[i - 1, j - 1,c] = np.sqrt(
                            pow(horizontal_grad, 2.0) + pow(vertical_grad, 2.0))            

        return new_gradient_image

    @staticmethod
    def apply_gradient(img, filter_matrix):
        '''
        Apply gradient using a single filter_matrix (3x3).
        '''
        filter_height, filter_width = util.get_dimensions(
            filter_matrix)
        assert filter_height != 3, "Filter Matrix must have height = 3 instead of" + \
            string(filter_height)
        assert filter_width != 3, "Filter Matrix must have width = 3 instead of" + \
            string(filter_width)

        height, width = util.get_dimensions(img)

        # define image with 0s
        new_gradient_image = np.zeros((height, width), np.uint8)

        for i in range(1, height - 1):
            for j in range(1, width - 1):
                grad = ImageFilter.apply_gradient_core(
                    filter_matrix, img, i, j)
                new_gradient_image[i - 1, j - 1] = abs(grad)

        return new_gradient_image

    @staticmethod
    def apply_gradient_core(filter_matrix, img, i, j):
        return (filter_matrix[0, 0] * img[i - 1, j - 1]) + \
            (filter_matrix[0, 1] * img[i - 1, j]) + \
            (filter_matrix[0, 2] * img[i - 1, j + 1]) + \
            (filter_matrix[1, 0] * img[i, j - 1]) + \
            (filter_matrix[1, 1] * img[i, j]) + \
            (filter_matrix[1, 2] * img[i, j + 1]) + \
            (filter_matrix[2, 0] * img[i + 1, j - 1]) + \
            (filter_matrix[2, 1] * img[i + 1, j]) + \
            (filter_matrix[2, 2] * img[i + 1, j + 1])

    @staticmethod
    def get_arithmetic_mean(neighbors):
        sum_value = np.sum(neighbors)
        height, width = util.get_dimensions(neighbors)
        return sum_value / (height * width)

    @staticmethod
    def apply_arithmetic_mean(image, filter_size=3):
        kernel = np.ones((filter_size, filter_size))*(1.0/(filter_size**2))
        if len(image.shape) == 2:
            return ImageFilter.apply_convolution(image, kernel)
        else:
            r, g, b = [image[:,:,0],image[:,:,1],image[:,:,2]]
            R = ImageFilter.apply_convolution(r, kernel)
            G = ImageFilter.apply_convolution(g, kernel)
            B = ImageFilter.apply_convolution(b, kernel)
            output = np.zeros((R.shape[0], R.shape[1], 3), dtype=np.uint8)
            output[:,:,0] = R
            output[:,:,1] = G
            output[:,:,2] = B

            return output.astype(np.uint8)
    # def apply_arithmetic_mean(img, filter_size=3):
    #     filter_size = util.format_filter_size(filter_size)
    #     obtained, original = util.get_empty_image_with_same_dimensions(
    #         img)
    #     if len(img.shape) == 2:
    #         for i in range(len(original)):
    #             for j in range(len(original[0])):
    #                 neighbors = ImageFilter.__get_neighbors_matrix(
    #                     filter_size, i, j, original)
    #                 obtained[i][j] = ImageFilter.get_arithmetic_mean(neighbors)
    #     else:
    #         channel = img.shape[2]
    #         for c in range (channel):
    #             for i in range(len(original)):
    #                 for j in range(len(original[0])):
    #                     neighbors = ImageFilter.__get_neighbors_matrix(
    #                         filter_size, i, j, original)
    #                     obtained[i][j][c] = ImageFilter.get_arithmetic_mean(neighbors)

    #     return obtained

    @staticmethod
    def get_geometric_mean(matrix):
        prod_value = np.prod(matrix)
        height, width = util.get_dimensions(matrix)
        counter = height * width
        result = prod_value**(1.0 / counter)
        return np.around(result, decimals=3)

    @staticmethod
    def apply_geometric_mean(img, filter_size):
        filter_size = util.format_filter_size(filter_size)
        obtained, original = util.get_empty_image_with_same_dimensions(
            img)
        for i in range(len(original)):
            for j in range(len(original[0])):
                neighbors = ImageFilter.__get_neighbors_matrix(
                    filter_size, i, j, original)
                obtained[i][j] = ImageFilter.get_geometric_mean(neighbors)

        return obtained

    @staticmethod
    def get_harmonic_mean(matrix):
        float_matrix = np.array(matrix).astype(float)
        sum_value = np.sum(np.reciprocal(float_matrix))
        counter = len(matrix)
        result = counter / sum_value
        return np.around(result, decimals=3)

    @staticmethod
    def apply_harmonic_mean(img, filter_size):
        filter_size = util.format_filter_size(filter_size)
        obtained, original = util.get_empty_image_with_same_dimensions(
            img)
        if len(img.shape) == 2:
            for i in range(len(original)):
                for j in range(len(original[0])):
                    neighbors = ImageFilter.__get_neighbors_matrix(
                        filter_size, i, j, original)
                    obtained[i][j] = ImageFilter.get_harmonic_mean(neighbors)
        else:
            R = ImageFilter.apply_harmonic_mean(img[:,:,0],filter_size)
            G = ImageFilter.apply_harmonic_mean(img[:,:,1],filter_size)
            B = ImageFilter.apply_harmonic_mean(img[:,:,2],filter_size)
            output = np.zeros((R.shape[0], R.shape[1], 3), dtype=np.uint8)
            output[:,:,0] = R
            output[:,:,1] = G
            output[:,:,2] = B
            obtained = output

        return obtained

    @staticmethod
    def get_contra_harmonic_mean(matrix, q):
        float_matrix = np.array(matrix).astype(float)
        denominator = np.sum(float_matrix ** q, where=(float_matrix != 0))
        numerator = np.sum(float_matrix ** (q + 1), where=(float_matrix != 0))
        result = np.where((denominator == 0.0), 0.0, (numerator / denominator))
        
        return np.around(result, decimals=3)

    @staticmethod
    def apply_contra_harmonic_mean(img, filter_size, q):
        filter_size = util.format_filter_size(filter_size)
        obtained, original = util.get_empty_image_with_same_dimensions(
            img)

        if len(img.shape) == 2:
            for i in range(len(original)):
                for j in range(len(original[0])):
                    neighbors = ImageFilter.__get_neighbors_matrix(
                        filter_size, i, j, original)
                    obtained[i][j] = ImageFilter.get_contra_harmonic_mean(
                        neighbors, q)
        else:
            R = ImageFilter.apply_contra_harmonic_mean(img[:,:,0],filter_size,q)
            G = ImageFilter.apply_contra_harmonic_mean(img[:,:,1],filter_size,q)
            B = ImageFilter.apply_contra_harmonic_mean(img[:,:,2],filter_size,q)
            output = np.zeros((R.shape[0], R.shape[1], 3), dtype=np.uint8)
            output[:,:,0] = R
            output[:,:,1] = G
            output[:,:,2] = B
            obtained = output

        return obtained

    @staticmethod
    def apply_highboost(image, c, filter_size):
        blurred = ImageFilter.apply_arithmetic_mean(image, filter_size)
        mask = image - blurred
        result = image + (c * mask)
        return result, mask

    @staticmethod
    def adjust_brightness (img, br):
        """
        0 < br < 1: decrease brightness
        br = 1: no changes
        br >: increase brightness
        """
        height,width = util.get_dimensions(img)
        obtained = np.zeros((height, width, 3), np.uint8)

        for i in range(height):
            for j in range(width):
                for k in range(img.shape[2]):
                    b = img[i][j][k] * br
                    if b > 255:
                        b = 255
                    obtained[i][j][k] = b
        return obtained.astype(np.uint8)
