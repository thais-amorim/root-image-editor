#!/usr/bin/python
import pytest
import numpy as np
from root.filter import ImageFilter as filter


def test_geometric_mean_for_float_array():
    input = np.array([4, 8, 3, 9, 17])
    obtained = filter.get_geometric_mean(input)
    assert obtained == 6.814


def test_geometric_mean_for_int_array():
    input = np.array([2,    3,    6])
    obtained = filter.get_geometric_mean(input)
    assert obtained == 3.302


def test_geometric_mean_for_int_list():
    input = [2,    3,    6]
    obtained = filter.get_geometric_mean(input)
    assert obtained == 3.302


def test_geometric_mean_for_matrix():
    input = np.array([
        [1,    2,    4],
        [7,    9,    6],
        [15,    10,    1]])
    obtained = filter.get_geometric_mean(input)
    assert obtained == 4.251
