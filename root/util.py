import imageio


def read_image(image_path, type="RGB"):
    return imageio.imread(image_path, as_gray=False, pilmode=type)


def save_image(name, image_as_byte):
    imageio.imwrite(name, image_as_byte)


def normalize_image(img):
    min_input = img.min()
    max_input = img.max()

    min_output = _MIN_PIXEL
    max_output = _MAX_PIXEL
    return (img - min_input) * ((max_output - min_output) / (max_input - min_input) + min_output)
