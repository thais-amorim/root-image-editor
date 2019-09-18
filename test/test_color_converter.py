import pytest
from root import color_converter as converter

def test_rgb_to_gray_via_weighted_average():
    r = 200
    g = 133
    b =  96

    expected = (r * 0.2989) + (g * 0.5870) + (b * 0.1140)
    obtained = converter.rgb_to_gray_via_weighted_average(r,g,b)

    assert obtained == expected

def test_rgb_to_gray_via_weighted_average():
    r = 200
    g = 133
    b =  96

    expected = (r + g + b) / 3
    obtained = converter.rgb_to_gray_via_simple_average(r,g,b)

    assert obtained == expected


def test_rgb_to_hsv_check_h():
    r = 200
    g = 133
    b =  96

    h,s,v = converter.rgb_to_hsv(r,g,b)
    assert h == 21

def test_rgb_to_hsv_check_s():
    r = 200
    g = 133
    b =  96

    h,s,v = converter.rgb_to_hsv(r,g,b)
    assert s == 0.52

def test_rgb_to_hsv_check_v():
    r = 200
    g = 133
    b =  96

    h,s,v = converter.rgb_to_hsv(r,g,b)
    assert v == 0.7843137254901961

def test_hsv_to_rgb_check_r():
    h = 21
    s = 0.52
    v = 0.7843137254901961

    r,g,b = converter.hsv_to_rgb(h,s,v)
    assert r == 200

def test_hsv_to_rgb_check_g():
    h = 21
    s = 0.52
    v = 0.7843137254901961

    r,g,b = converter.hsv_to_rgb(h,s,v)
    assert g == 132

def test_hsv_to_rgb_check_b():
    h = 21
    s = 0.52
    v = 0.7843137254901961

    r,g,b = converter.hsv_to_rgb(h,s,v)
    assert b ==  96
