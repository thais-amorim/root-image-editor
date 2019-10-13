import pytest
from root.converter import ColorConverter as converter
from math import *


def test_rgb_to_gray_via_weighted_average():
    r = 200
    g = 133
    b = 96

    expected = (r * 0.2989) + (g * 0.5870) + (b * 0.1140)
    obtained = converter.rgb_to_gray_via_weighted_average(r, g, b)

    assert obtained == expected


def test_rgb_to_gray_via_weighted_average():
    r = 200
    g = 133
    b = 96

    expected = (r + g + b) / 3
    obtained = converter.rgb_to_gray_via_simple_average(r, g, b)

    assert obtained == expected


def test_rgb_to_hsv_check_h():
    r = 200
    g = 133
    b = 96

    h, s, v = converter.rgb_to_hsv(r, g, b)
    assert h == 21


def test_rgb_to_hsv_check_s():
    r = 200
    g = 133
    b = 96

    h, s, v = converter.rgb_to_hsv(r, g, b)
    assert s == 0.52


def test_rgb_to_hsv_check_v():
    r = 200
    g = 133
    b = 96

    h, s, v = converter.rgb_to_hsv(r, g, b)
    assert v == 0.7843137254901961


def test_hsv_to_rgb_check_r():
    h = 21
    s = 0.52
    v = 0.7843137254901961

    r, g, b = converter.hsv_to_rgb(h, s, v)
    assert r == 200


def test_hsv_to_rgb_check_g():
    h = 21
    s = 0.52
    v = 0.7843137254901961

    r, g, b = converter.hsv_to_rgb(h, s, v)
    assert g == 132


def test_hsv_to_rgb_check_b():
    h = 21
    s = 0.52
    v = 0.7843137254901961

    r, g, b = converter.hsv_to_rgb(h, s, v)
    assert b == 96


def test_normalize_to_zero_one_check_interval_r():
    r = 31
    g = 76
    b = 122

    obtained_r, obtained_g, obtained_b = converter.normalize_to_zero_one(
        r, g, b)
    assert obtained_r >= 0
    assert obtained_r <= 1


def test_normalize_to_zero_one_check_r():
    r = 31
    g = 76
    b = 122

    obtained_r, obtained_g, obtained_b = converter.normalize_to_zero_one(
        r, g, b)
    assert obtained_r == 0.12156862745098039


def test_normalize_to_zero_one_check_interval_g():
    r = 31
    g = 76
    b = 122

    obtained_r, obtained_g, obtained_b = converter.normalize_to_zero_one(
        r, g, b)
    assert obtained_g >= 0
    assert obtained_g <= 1


def test_normalize_to_zero_one_check_g():
    r = 31
    g = 76
    b = 122

    obtained_r, obtained_g, obtained_b = converter.normalize_to_zero_one(
        r, g, b)
    assert obtained_g == 0.2980392156862745


def test_normalize_to_zero_one_check_interval_b():
    r = 31
    g = 76
    b = 122

    obtained_r, obtained_g, obtained_b = converter.normalize_to_zero_one(
        r, g, b)
    assert obtained_b >= 0
    assert obtained_b <= 1


def test_normalize_to_zero_one_check_b():
    r = 31
    g = 76
    b = 122

    obtained_r, obtained_g, obtained_b = converter.normalize_to_zero_one(
        r, g, b)
    assert obtained_b == 0.47843137254901963


def test_normalize_rgb_check_interval_r():
    r = 1
    g = 0
    b = 0.5

    obtained_r, obtained_g, obtained_b = converter.normalize_rgb(r, g, b)
    assert obtained_r >= 0
    assert obtained_r <= 255


def test_normalize_rgb_check_r():
    r = 1
    g = 0
    b = 0.5

    obtained_r, obtained_g, obtained_b = converter.normalize_rgb(r, g, b)
    assert obtained_r == 255


def test_normalize_rgb_interval_g():
    r = 1
    g = 0
    b = 0.5

    obtained_r, obtained_g, obtained_b = converter.normalize_rgb(r, g, b)
    assert obtained_g >= 0
    assert obtained_g <= 255


def test_normalize_rgb_check_g():
    r = 1
    g = 0
    b = 0.5

    obtained_r, obtained_g, obtained_b = converter.normalize_rgb(r, g, b)
    assert obtained_g == 0


def test_normalize_rgb_check_interval_b():
    r = 1
    g = 0
    b = 0.5

    obtained_r, obtained_g, obtained_b = converter.normalize_rgb(r, g, b)
    assert obtained_b >= 0
    assert obtained_b <= 255


def test_normalize_rgb_check_b():
    r = 1
    g = 0
    b = 0.5

    obtained_r, obtained_g, obtained_b = converter.normalize_rgb(r, g, b)
    assert obtained_b == 127


def test_rgb_to_hsi_check_h():
    r = 31
    g = 76
    b = 122

    h, s, i = converter.rgb_to_hsi(r, g, b)
    assert h == 210.36


def test_rgb_to_hsi_check_s():
    r = 31
    g = 76
    b = 122

    h, s, i = converter.rgb_to_hsi(r, g, b)
    assert s == 0.59


def test_rgb_to_hsi_check_i():
    r = 31
    g = 76
    b = 122

    h, s, i = converter.rgb_to_hsi(r, g, b)
    assert i == 0.30


def test_hsi_to_rgb_check_r():
    h = 210.36
    s = 0.59
    i = 0.30

    r, g, b = converter.hsi_to_rgb(h, s, i)
    assert r == 31


def test_hsi_to_rgb_check_g():
    h = 210.36
    s = 0.59
    i = 0.30

    r, g, b = converter.hsi_to_rgb(h, s, i)
    assert g == 76


def test_hsi_to_rgb_check_b():
    h = 210.36
    s = 0.59
    i = 0.30

    r, g, b = converter.hsi_to_rgb(h, s, i)
    assert b == 121


def test_hsi_to_rgb_rg_sector():
    h = 80
    s = 0.59
    i = 0.30

    r, g, b = converter.hsi_to_rgb(h, s, i)
    assert r == 84
    assert g == 113
    assert b == 31


def test_hsi_to_rgb_gb_sector():
    h = 210
    s = 0.59
    i = 0.30

    r, g, b = converter.hsi_to_rgb(h, s, i)
    assert r == 31
    assert g == 76
    assert b == 121


def test_hsi_to_rgb_br_sector():
    h = 300
    s = 0.59
    i = 0.30

    r, g, b = converter.hsi_to_rgb(h, s, i)
    assert r == 99
    assert g == 31
    assert b == 99
