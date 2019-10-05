#!/usr/bin/python
import pytest
import numpy as np
from root import image_filter as filter


def test_format_negative_size():
    original_size = -5
    expected = 3
    obtained = filter.format_size(original_size)
    assert obtained == expected


def test_format_size_zero():
    original_size = 0
    expected = 3
    obtained = filter.format_size(original_size)
    assert obtained == expected


def test_format_low_positive_size():
    original_size = 1
    expected = 3
    obtained = filter.format_size(original_size)
    assert obtained == expected


def test_format_min_size():
    original_size = 3
    expected = 3
    obtained = filter.format_size(original_size)
    assert obtained == expected


def test_format_even_size():
    original_size = 4
    expected = original_size + 1
    obtained = filter.format_size(original_size)
    assert obtained == expected


def test_format_odd_size():
    original_size = 7
    expected = original_size
    obtained = filter.format_size(original_size)
    assert obtained == expected


def test_harmonic_mean_for_float_array():
    input = np.array([1.0,    2.0,    4.0])
    obtained = filter.get_harmonic_mean(input)
    assert obtained == 1.714


def test_harmonic_mean_for_int_array():
    input = np.array([1,    2,    4])
    obtained = filter.get_harmonic_mean(input)
    assert obtained == 1.714


def test_harmonic_mean_for_int_list():
    input = [1,    2,    4]
    obtained = filter.get_harmonic_mean(input)
    assert obtained == 1.714


def test_harmonic_mean_for_matrix():
    input = np.array([
        [1,    2,    4],
        [7,    9,    6],
        [15,    10,    1]])
    obtained = filter.get_harmonic_mean(input)
    assert obtained == 0.899
