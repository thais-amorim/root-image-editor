from root.filter import ImageFilter as filter
from root.filter import RgbFilter as rgbFilter
from root.filter import ColorFilter as color
from root.converter import ColorConverter as converter
from root.converter import ScaleConverter as scale
from root.util import ImageUtil as util
from root.util import RgbUtil as rgb


def main():
    img_rgb = util.read_image("images/laplacian/Fig0338a.bmp")
    r, g, b = rgb.get_rgb_layers(img_rgb)
    img_gray = converter.rgb_to_gray_via_weighted_average(r, g, b)
    obtained, sharpened = filter.apply_laplacian(img_gray)
    util.save_image("images/laplacian/output.jpg", obtained)
    util.save_image("images/laplacian/sharpened.jpg", sharpened)


if __name__ == "__main__":
    main()
