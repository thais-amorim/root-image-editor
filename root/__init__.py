from root.filter import ImageFilter as filter
from root.filter import RgbFilter as rgbFilter
from root.filter import ColorFilter as color
from root.converter import ColorConverter as converter
from root.converter import ScaleConverter as scale
from root.util import ImageUtil as util
from root.util import RgbUtil as rgb


def main():
    img_rgb = util.read_image("images/median/Fig0335a.jpg")
    #r, g, b = rgb.get_rgb_layers(img_rgb)
    #img_gray = converter.rgb_to_gray_via_weighted_average(r, g, b)
    obtained = scale.apply_bilinear_interpolation(img_rgb, 2)
    util.save_image("images/median/output_size.jpg", obtained)


if __name__ == "__main__":
    main()
