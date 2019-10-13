from root.filter import ImageFilter as filter
from root.filter import RgbFilter as rgbFilter
from root.filter import ColorFilter as color
from root.converter import ColorConverter as converter
from root.util import ImageUtil as util
from root.util import RgbUtil as rgb


def main():
    img_rgb = util.read_image("images/aranha_trevosa.jpeg")
    #r, g, b = rgb.get_rgb_layers(img_rgb)
    #img_gray = converter.rgb_to_gray_via_weighted_average(r, g, b)
    rgbFilter.draw_histogram(img_rgb, "images/results/aranha_hist")
    #util.save_image("images/negative/output_color.jpg", output_color)


if __name__ == "__main__":
    main()
