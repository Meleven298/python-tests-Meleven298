from math_utils import *

import pytest


@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (-3, 2, -1),
    (2.9, 3, 5.9)
])
@pytest.mark.feature('add')
def test_add(a, b ,expected):
    assert add(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (2,3, -1),
    (-3,2, -5),
    (2.9, 3, -0.1)
])
@pytest.mark.feature('substract')
def test_substract(a,b,expected):
    round(substract(a, b), 10) == round(expected, 10)

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 6),
    (-3, 2, -6),
    (2.9, 3, 8.7)
])
@pytest.mark.feature('multiply')
def test_multiply(a, b, expected):
    assert multiply(a,b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (3, 2, 1.5),
    (-3, 2, -1.5),
    (2, 2.5, 0.8)
])
@pytest.mark.feature('divide')
def test_divide(a ,b, expected):
    assert divide(a, b) == expected

    with pytest.raises(ZeroDivisionError):
        divide(3,0)


@pytest.mark.parametrize('func', [add, substract, multiply, divide])
def test_raises(func):
    with pytest.raises(TypeError):
        func(2, "2")

    with pytest.raises(TypeError):
        func([], ())
    