import pytest
from calculator import Calculator

calc = Calculator()


def test_add_1():
    assert calc.add(2, 3) == 5

def test_add_2():
    assert calc.add(-1, 5) == 4

def test_add_3():
    assert calc.add(0, 0) == 0

def test_subtract_1():
    assert calc.subtract(10, 5) == 5

def test_subtract_2():
    assert calc.subtract(5, 10) == -5

def test_multiply_1():
    assert calc.multiply(2, 4) == 8

def test_multiply_2():
    assert calc.multiply(-2, 3) == -6

def test_multiply_3():
    assert calc.multiply(0, 10) == 0

def test_divide_1():
    assert calc.divide(10, 2) == 5

def test_divide_2():
    assert calc.divide(9, 3) == 3

def test_divide_by_zero():
    with pytest.raises(ValueError):
        calc.divide(10, 0)

def test_square_1():
    assert calc.square(4) == 16

def test_square_2():
    assert calc.square(-5) == 25

def test_cube_1():
    assert calc.cube(3) == 27

def test_cube_2():
    assert calc.cube(-2) == -8

def test_power_1():
    assert calc.power(2, 3) == 8

def test_power_2():
    assert calc.power(5, 0) == 1

def test_even_1():
    assert calc.is_even(10) is True

def test_even_2():
    assert calc.is_even(7) is False

def test_odd_1():
    assert calc.is_odd(7) is True

def test_odd_2():
    assert calc.is_odd(8) is False

def test_maximum():
    assert calc.maximum(10, 20) == 20

def test_minimum():
    assert calc.minimum(10, 20) == 10