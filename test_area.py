import math

import pytest

from area import Figure


def test_zero_sides():
    with pytest.raises(Exception):
        Figure()

def test_circle():
    assert Figure(1).get_area() == math.pi
    assert Figure(2.5).get_area() == math.pi * 2.5**2
    assert Figure(0).get_area() == 0
    with pytest.raises(Exception):
        Figure(-1)
    assert Figure(3).__str__() == "круг"

def test_two_sides():
    with pytest.raises(Exception):
        Figure(1, 2)

def test_triangle():
    assert Figure(3, 4, 5).get_area() == 6
    assert Figure(0, 0, 0).get_area() == 0
    with pytest.raises(Exception):
        Figure(1, 2, 3)
    with pytest.raises(Exception):
        Figure(-2, 0, 2)
    assert Figure(4, 3, 5).__str__() == "прямоугольный треугольник"
    assert Figure(4, 4, 4).__str__() == "треугольник"

def test_polyhedron():
    with pytest.raises(Exception):
        Figure(1, 2, 3, 4)