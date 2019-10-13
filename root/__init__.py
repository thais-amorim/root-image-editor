from root.filter import ImageFilter as filter
from root.filter import ColorFilter as color
from root.converter import ColorConverter as converter
from root.util import ImageUtil as util
from root.util import RgbUtil as rgb


def main():
    img = util.read_image("images/negative/Fig0304a.jpg")
    r, g, b = rgb.get_rgb_layers(img)
    img = converter.rgb_to_gray_via_weighted_average(r, g, b)
    output = filter.apply_negative(img.copy())
    util.save_image("images/geometric-mean/output.jpg", output)


if __name__ == "__main__":
    main()
