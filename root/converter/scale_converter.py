from root.util import ImageUtil as util
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
