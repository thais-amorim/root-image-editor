from root.filter import ImageFilter as filter
from root.filter import RgbFilter as rgbFilter
from root.filter import ColorFilter as color
from root.converter import ColorConverter as converter
from root.converter import ScaleConverter as scale
from root.util import ImageUtil as util
from root.util import RgbUtil as rgb


def main():
    img_rgb = util.read_image("images/aranha_trevosa.jpeg")
    obtained = color.adjust_intensity(img_rgb,0.1)
    util.save_image("images/laplacian/output_br.jpg", obtained)


if __name__ == "__main__":
    main()
