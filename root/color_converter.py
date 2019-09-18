import numpy as np
import math

def get_rgb_layers(img):
    r = rgb[:, :, 0]
    g = rgb[:, :, 1]
    b = rgb[:, :, 2]

    return r, g, b

def rgb_to_gray_via_weighted_average(r, g, b):
    return (r * 0.2989) + (g * 0.5870) + (b * 0.1140)

def rgb_to_gray_via_simple_average(r, g, b):
    return (r + g + b) / 3

def calculate_hue(r,g,b):
    max_value = max(r, g, b)
    min_value = min(r, g, b)
    diff = max_value-min_value
    if max_value == min_value:
        hue = 0
    elif max_value == r:
        hue = (60 * ((g-b)/diff) + 360) % 360
    elif max_value == g:
        hue = (60 * ((b-r)/diff) + 120) % 360

    return hue

def calculate_saturation(r,g,b):
    max_value = max(r, g, b)
    min_value = min(r, g, b)
    diff = max_value-min_value

    if max_value == 0:
        saturation = 0
    else:
        saturation = diff/max_value

    return saturation

def rgb_to_hsv(r, g, b):
    '''
    Convert a RGB image to HSV image.
    Input: R, G, B values are [0, 255].
    Output: H value is [0, 360]. S, V values are [0, 1].
    '''
    r, g, b = r/255.0, g/255.0, b/255.0

    h = calculate_hue(r,g,b)
    s = calculate_saturation(r,g,b)
    v = max(r, g, b)
    return int(h), s, v

def hsv_to_rgb(h,s,v):
    '''
    Convert a HSV image to RGB image.
    Input: H value is [0, 360]. S, V values are [0, 1].
    Output: R, G, B values are [0, 255].
    '''
    h = float(h)
    s = float(s)
    v = float(v)
    h60 = h / 60.0
    h60f = math.floor(h60)
    hi = int(h60f) % 6
    f = h60 - h60f
    p = v * (1 - s)
    q = v * (1 - f * s)
    t = v * (1 - (1 - f) * s)
    r, g, b = 0, 0, 0
    if hi == 0: r, g, b = v, t, p
    elif hi == 1: r, g, b = q, v, p
    elif hi == 2: r, g, b = p, v, t
    elif hi == 3: r, g, b = p, q, v
    elif hi == 4: r, g, b = t, p, v
    elif hi == 5: r, g, b = v, p, q
    r, g, b = int(r * 255), int(g * 255), int(b * 255)
    return r, g, b
