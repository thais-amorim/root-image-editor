#!/usr/bin/python
import pytest
from root import image_filter as filter

def test_format_negative_size():
    original_size = -5;
    expected = 3;
    obtained = filter.format_size(original_size)
    assert obtained == expected

def test_format_size_zero():
    original_size = 0;
    expected = 3;
    obtained = filter.format_size(original_size)
    assert obtained == expected

def test_format_low_positive_size():
    original_size = 1;
    expected = 3;
    obtained = filter.format_size(original_size)
    assert obtained == expected

def test_format_min_size():
    original_size = 3;
    expected = 3;
    obtained = filter.format_size(original_size)
    assert obtained == expected

def test_format_even_size():
    original_size = 4;
    expected = original_size + 1;
    obtained = filter.format_size(original_size)
    assert obtained == expected

def test_format_odd_size():
    original_size = 7;
    expected = original_size;
    obtained = filter.format_size(original_size)
    assert obtained == expected
