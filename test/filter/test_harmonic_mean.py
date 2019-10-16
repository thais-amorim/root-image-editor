#!/usr/bin/python
import pytest
import numpy as np
from root.filter import ImageFilter as filter


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
