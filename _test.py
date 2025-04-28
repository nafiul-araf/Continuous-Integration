import pytest
import math

def circle(r):
    return round(math.pi * r ** 2, 2)

def triangle(b, h):
    return round(0.5 * b * h, 2)

def ractangle(l, w):
    return round(l * w, 2)

def test_circle():
    assert circle(3.45) == 37.39, "Test Failed: the area of the circle for radius 3.45 should be 37.39"
    assert circle(9.14) == 262.45, "Test Failed: the area of the circle for radius 9.14 should be 262.45"

def test_triangle():
    assert triangle(5.60, 2.30) == 6.44, "Test Failed: the area of the triangle for base 5.60 and heigth 2.30 should be 6.44"
    assert triangle(6.98, 2.34) == 8.17, "Test Failed: the area of the triangle for base 6.98 and heigth 2.34 should be 8.17"

def test_ractangle():
    assert ractangle(10.23, 7.12) == 72.84, "Test Failed: the area of the ractangle for length 10.23 and width 7.12 should be 72.84"
    assert ractangle(3.45, 4.54) == 15.66, "Test Failed: the area of the ractangle for length 3.45 and width 4.54 should be 15.66"


def test_invalid_input():
    with pytest.raises(TypeError):
        circle("string")
        triangle("string", "string")
        ractangle("string", "string")