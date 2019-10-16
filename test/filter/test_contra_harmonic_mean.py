#!/usr/bin/python
import pytest
import numpy as np
from root.filter import ImageFilter as filter


def test_contra_harmonic_mean_for_float_array():
    input = np.array([1.0,    2.0,    4.0])
    q = 2
    obtained = filter.get_contra_harmonic_mean(input, q)
    assert obtained == 3.476


def test_contra_harmonic_mean_for_int_array():
    input = np.array([1,    2,    4])
    q = 1
    obtained = filter.get_contra_harmonic_mean(input, q)
    assert obtained == 3.0


def test_contra_harmonic_mean_for_int_list():
    input = [1,    1,    1]
    q = 1
    obtained = filter.get_contra_harmonic_mean(input, q)
    assert obtained == 1.0


def test_contra_harmonic_mean_for_matrix():
    input = np.array([
        [1,    2,    4],
        [1,    1,    1],
        [15,    10,    1]])
    q = 3
    obtained = filter.get_contra_harmonic_mean(input, q)
    assert obtained == 13.680


def test_contra_harmonic_mean_for_not_int_expoent():
    input = np.array([1.0,    2.0,    4.0])
    q = 1.5
    obtained = filter.get_contra_harmonic_mean(input, q)
    assert obtained == 3.268


def test_contra_harmonic_mean_for_negative_expoent():
    input = np.array([1.0,    2.0,    4.0])
    q = -1
    obtained = filter.get_contra_harmonic_mean(input, q)
    assert obtained == 1.714


def test_contra_harmonic_mean_with_zeros():
    input = np.array([0.0,    2.0,    0.0])
    q = 1
    obtained = filter.get_contra_harmonic_mean(input, q)
    assert obtained == 2.0
