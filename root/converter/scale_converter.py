from util import ImageUtil as util
import numpy as np


class ScaleConverter():
    @staticmethod
    def get_nearest_neighbour_pixel_interpolation(img, posX, posY):
        out = []

        # Get integer parts of positions
        modXi = int(posX)
        modYi = int(posY)
        # Get fractional parts of positions
        modXf = posX - modXi
        modYf = posY - modYi
        # To avoid going over image bounderies
        height, width = util.get_dimensions(img)
        modXiPlusOneLim = min(modXi + 1, width - 1)
        modYiPlusOneLim = min(modYi + 1, height - 1)

        for channel in range(img.shape[2]):
            target = img[modYi, modXi, channel]
            out.append(int(target + 0.5))
        return out

    @staticmethod
    def apply_nearest_neighbour(img, scale):
        if scale <= 0:
            return img

        imHeight, imWidth = util.get_dimensions(img)
        enlargedShape = list(
            map(int, [imHeight * scale, imWidth * scale, img.shape[2]]))
        enlargedImg = np.empty(enlargedShape, dtype=np.uint8)
        enlargedHeight, enlargedWidth = util.get_dimensions(enlargedImg)
        rowScale = float(imHeight) / float(enlargedHeight)
        colScale = float(imWidth) / float(enlargedWidth)
        for row in range(enlargedHeight):
            for col in range(enlargedWidth):
                # Find position in original image
                oriRow = row * rowScale
                oriCol = col * colScale
                enlargedImg[row, col] = ScaleConverter.get_nearest_neighbour_pixel_interpolation(
                    img, oriCol, oriRow)

        return enlargedImg

    @staticmethod
    def get_bilinear_pixel_interpolation(img, posX, posY):
        out = []

        # Get integer parts of positions
        modXi = int(posX)
        modYi = int(posY)
        # Get fractional parts of positions
        modXf = posX - modXi
        modYf = posY - modYi
        # To avoid going over image bounderies
        height, width = util.get_dimensions(img)
        modXiPlusOneLim = min(modXi + 1, width - 1)
        modYiPlusOneLim = min(modYi + 1, height - 1)

        # Get pixels in four corners
        for channel in range(img.shape[2]):
            bottom_left = img[modYi, modXi, channel]
            bottom_right = img[modYi, modXiPlusOneLim, channel]
            top_left = img[modYiPlusOneLim, modXi, channel]
            top_right = img[modYiPlusOneLim, modXiPlusOneLim, channel]

            # Calculate interpolation
            obtained_bottom = modXf * bottom_right + (1. - modXf) * bottom_left
            obtained_top = modXf * top_right + (1. - modXf) * top_left
            new_channel = modYf * obtained_top + (1. - modYf) * obtained_bottom
            out.append(int(new_channel + 0.5))

        return out

    @staticmethod
    def apply_bilinear_interpolation(img, scale):
        if scale <= 0:
            return img

        imHeight, imWidth = util.get_dimensions(img)
        enlargedShape = list(
            map(int, [imHeight * scale, imWidth * scale, img.shape[2]]))
        enlargedImg = np.empty(enlargedShape, dtype=np.uint8)
        enlargedHeight, enlargedWidth = util.get_dimensions(enlargedImg)
        rowScale = float(imHeight) / float(enlargedHeight)
        colScale = float(imWidth) / float(enlargedWidth)
        for row in range(enlargedHeight):
            for col in range(enlargedWidth):
                oriRow = row * rowScale  # Find position in original image
                oriCol = col * colScale
                enlargedImg[row, col] = ScaleConverter.get_bilinear_pixel_interpolation(
                    img, oriCol, oriRow)

        return enlargedImg

<<<<<<< HEAD
    
    @staticmethod
    def apply_rotate_nearest(image, angle):
=======

    #TODO
    def nnrotate(image, angle):
>>>>>>> merge_frontend_develop
        height, width = image.shape[:2]
        output = np.zeros_like(image, dtype=np.uint8)
        angle = angle * np.pi / 180

        for x in range(width):
            for y in range(height):
                i = int(x+angle)
                j = int(y+angle)
                print(i,j)
                output[x,y] = image[i,j]

        return output


    # RGB and Grayscale Image
    @staticmethod
    def apply_rotate_bilinear(image, angle):
        width, height = image.shape[:2]
        output = np.zeros_like(image, dtype=np.uint8)
        angle = angle * np.pi / 180
        center_x = width / 2
        center_y = height / 2

        for x in range(width):
            for y in range(height):
                xp = int((x - center_x) * np.cos(angle) - (y - center_y) * np.sin(angle) + center_x)
                yp = int((x - center_x) * np.sin(angle) + (y - center_y) * np.cos(angle) + center_y)
                if 0 <= xp < width and 0 <= yp < height:
                    output[x, y] = image[xp, yp]

        return output
