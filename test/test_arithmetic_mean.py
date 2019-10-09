#!/usr/bin/python
import pytest
import numpy as np
from root.filter import ImageFilter as filter


def test_get_arithmetic_mean_int_list():
    input = [1,    2,    3]
    obtained = filter.get_arithmetic_mean(input)
    assert obtained == 2.0

def test_get_arithmetic_mean_float_list():
    input = [1.0,    2.0,    3.0]
    obtained = filter.get_arithmetic_mean(input)
    assert obtained == 2.0

def test_get_arithmetic_mean_with_broken_number():
    input = [1.0,    2.0,    0.6]
    obtained = filter.get_arithmetic_mean(input)
    assert obtained == 1.2

def test_get_arithmetic_mean_with_negative_number():
    input = [1,    2,    -6]
    obtained = filter.get_arithmetic_mean(input)
    assert obtained == -1.0

def test_get_arithmetic_mean_for_matrix():
    input = np.array([
        [1,    1,    1],
        [1,    1,    1],
        [1,    1,    10]])
    obtained = filter.get_arithmetic_mean(input)
    assert obtained == 2.0
