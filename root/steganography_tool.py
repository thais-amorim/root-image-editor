from PIL import Image


class SteganographyTool:
    '''
    Class for hiding text messages within an image.
    Supported image formats: BMP, JPG

    :param message_path: The path of the message that should be hidden, it can be a text or image.
    :param image_path: The path of the image in which to hide the message.
    '''


def __init__(self, message_path=None, image_path=None):
    self.__message_path = message_path
    self.__image_path = image_path
    self.__image_as_bytes = None
    self.__message = None
    self.__file_type = None
    self.__max_image_size = None

    # It is mandatory to have an image as entry
    assert self.__image_path is not None

    # Get the file type from message path
    if self.__message_path is None:
        self.__file_type = None
    else:
        self.__file_type = self.__message_path.split('.')[-1]
    # Analyze image attributes
    self.gather_image_attributes()


def gather_image_attributes(self):
    '''
    Opens the target image file and gathers details.
    '''
    try:
        self.__image_as_bytes = Image.open(self.__image_path)
        # Get the carrier image name and type from the path
        self.__image_type = self.__image_path.split('.')[-1]
        # Get the total number of pixels that can be manipulated
        height = self.__image_as_bytes.size[0]
        width = self.__image_as_bytes.size[1]
        self.__max_image_size = width * height
    except Exception as error:
        raise Exception(
            'Error analyzing image: {} - {}'.format(self.__image_path, str(error)))


def get_LSB(value):
    if value & 1 == 0:
        return '0'
    else:
        return '1'


def Set_LSB(value, bit):
    if bit == '0':
        value = value & 254
    else:
        value = value | 1
    return value


def _select_encode(self):
    '''
    Select encode method based on image mode.
    Supported image modes: L (Black and White), RGB (Colorful)
    '''
    image_mode = ''.join(self.__image_as_bytes.getbands())
    if image_mode == 'L':
        self.L_replace_bits(self.__message_to_hide)
    elif image_mode in ['RGB', 'BGR']:
        self.RGB_replace_bits(self.__message_to_hide)
    else:
        print(image_mode + " is not a supported image mode for encoding :(")


def _select_decode(self):
    '''
    Select decode method based on image mode.
    Supported image modes: L (Black and White), RGB (Colorful)
    '''
    image_mode = ''.join(self.__image_as_bytes.getbands())
    if image_mode == 'L':  # Black or White images
        self.L_replace_bits(self.__message_to_hide)
    elif image_mode in ['RGB', 'BGR']:
        self.RGB_replace_bits(self.__message_to_hide)
    else:
        print(image_mode + " is not a supported image mode for decoding :(")


def encode(img, message):
    self._select_encode()
    return "image with the encoded message"


def decode(img):
    self._select_decode()
    return "secret decoded message"
