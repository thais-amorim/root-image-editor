import numpy as np
from math import floor, cos, radians, degrees, acos


def get_rgb_layers(rgb):
    r = rgb[:, :, 0]
    g = rgb[:, :, 1]
    b = rgb[:, :, 2]

    return r, g, b


def rgb_to_gray_via_weighted_average(r, g, b):
    return (r * 0.2989) + (g * 0.5870) + (b * 0.1140)


def rgb_to_gray_via_simple_average(r, g, b):
    return (r + g + b) / 3


def calculate_hsv_hue(r, g, b):
    max_value = max(r, g, b)
    min_value = min(r, g, b)
    diff = max_value - min_value
    if max_value == min_value:
        hue = 0
    elif max_value == r:
        hue = (60 * ((g - b) / diff) + 360) % 360
    elif max_value == g:
        hue = (60 * ((b - r) / diff) + 120) % 360

    return hue


def calculate_hsv_saturation(r, g, b):
    max_value = max(r, g, b)
    min_value = min(r, g, b)
    diff = max_value - min_value

    if max_value == 0:
        saturation = 0
    else:
        saturation = diff / max_value

    return saturation


def rgb_to_hsv(r, g, b):
    '''
    Convert a RGB image to HSV image.
    Input: R, G, B values are [0, 255].
    Output: H value is [0, 360]. S, V values are [0, 1].
    '''
    r, g, b = r / 255.0, g / 255.0, b / 255.0

    h = calculate_hsv_hue(r, g, b)
    s = calculate_hsv_saturation(r, g, b)
    v = max(r, g, b)
    return int(h), s, v


def hsv_to_rgb(h, s, v):
    '''
    Convert a HSV image to RGB image.
    Input: H value is [0, 360]. S, V values are [0, 1].
    Output: R, G, B values are [0, 255].
    '''
    h = float(h)
    s = float(s)
    v = float(v)
    h60 = h / 60.0
    h60f = floor(h60)
    hi = int(h60f) % 6
    f = h60 - h60f
    p = v * (1 - s)
    q = v * (1 - f * s)
    t = v * (1 - (1 - f) * s)
    r, g, b = 0, 0, 0
    if hi == 0:
        r, g, b = v, t, p
    elif hi == 1:
        r, g, b = q, v, p
    elif hi == 2:
        r, g, b = p, v, t
    elif hi == 3:
        r, g, b = p, q, v
    elif hi == 4:
        r, g, b = t, p, v
    elif hi == 5:
        r, g, b = v, p, q
    return normalize_rgb(r, g, b)


def rgb_to_hsi(r, g, b):
    '''
    Convert a RGB image to HSI image.
    Input: R, G, B values are [0, 255].
    Output: H value is [0, 360]. S, I values are [0, 1].
    '''
    r, g, b = normalize_to_zero_one(r, g, b)

    # Hue
    numerator = 0.5 * ((r - g) + (r - b))
    denominator = ((r - g) ** 2 + ((r - b) * (g - b))) ** 0.5
    # A small number was added in the donominator to avoid dividing by 0
    theta = degrees(acos(numerator / (denominator + 0.000001)))
    if b <= g:
        h = theta
    else:
        h = 360 - theta

    # Saturation
    s = 1 - ((3 / (r + g + b)) * min([r, g, b]))

    # Intensity
    i = (r + g + b) / 3

    return np.round(h, 2), np.round(s, 2), np.round(i, 2)


def hsi_to_rgb(h, s, i):
    '''
    Convert a HSI image to RGB image.
    Input: H value is [0, 360]. S, I values are [0, 1].
    Output: R, G, B values are [0, 255].
    '''
    r, g, b = [0, 0, 0]

    # RG sector (0 degrees <= hue < 120 degrees)
    if 0 <= h < 120:
        b = i * (1 - s)
        r = i * (1 + ((s * cos(radians(h))) / (cos(radians(60 - h)))))
        g = 3 * i - (r + b)

    # GB sector (120 degrees <= hue < 240 degrees)
    elif 120 <= h < 240:
        h = h - 120
        r = i * (1 - s)
        g = i * (1 + ((s * cos(radians(h))) / (cos(radians(60 - h)))))
        b = 3 * i - (r + g)

    # BR sector (240 degrees <= hue <= 360 degrees)
    elif 240 <= h <= 360:
        h = h - 240
        g = i * (1 - s)
        b = i * (1 + ((s * cos(radians(h))) / (cos(radians(60 - h)))))
        r = 3 * i - (b + g)

    return normalize_rgb(r, g, b)


def normalize_to_zero_one(r, g, b):
    '''
    Convert RGB values from [0, 255] to [0, 1] range.
    '''
    r = float(r) / 255.0
    g = float(g) / 255.0
    b = float(b) / 255.0

    return r, g, b


def normalize_rgb(r, g, b):
    '''
    Convert RGB values from [0, 1] to [0, 255] range.
    '''
    r = int(r * 255)
    g = int(g * 255)
    b = int(b * 255)

    return r, g, b
