from root.filter import ImageFilter as filter
from root.filter import RgbFilter as rgbFilter
from root.filter import ColorFilter as color
from root.converter import ColorConverter as converter
from root.util import ImageUtil as util
from root.util import RgbUtil as rgb


def main():
    img_rgb = util.read_image("images/blurry_moon.bmp")
    r, g, b = rgb.get_rgb_layers(img_rgb)
    img_gray = converter.rgb_to_gray_via_simple_average(r, g, b)

    obtained_gray = filter.apply_highboost(img_gray, 2, 3)
    util.save_image("images/geometric-mean/output_gray.jpg", obtained_gray)

    obtained = rgbFilter.apply_highboost(img_rgb, 2, 3)
    util.save_image("images/geometric-mean/output_color.jpg", obtained)


if __name__ == "__main__":
    main()
