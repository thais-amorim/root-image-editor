from root.filter import ImageFilter as filter
from root.filter import ColorFilter as color
from root.converter import ColorConverter as converter
from root.util import ImageUtil as util


def main():
    img = util.read_image("images/geometric-mean/Fig0507b.jpg")
    r, g, b = color.get_rgb_layers(img)
    img = converter.rgb_to_gray_via_weighted_average(r, g, b)
    output = filter.apply_geometric_mean(img.copy(), 3)
    util.save_image("images/geometric-mean/output.jpg", output)


if __name__ == "__main__":
    main()
