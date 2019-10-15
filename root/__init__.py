from root.filter import ImageFilter as filter
from root.filter import RgbFilter as rgbFilter
from root.filter import ColorFilter as color
from root.converter import ColorConverter as converter
from root.converter import ScaleConverter as scale
from root.util import ImageUtil as util
from root.util import RgbUtil as rgb


def main():
    img_rgb = util.read_image("images/laplacian/Fig0338a.bmp")
    obtained = color.adjust_brightness(img_rgb,-0.5)
    util.save_image("images/laplacian/output2.jpg", obtained)


if __name__ == "__main__":
    main()
