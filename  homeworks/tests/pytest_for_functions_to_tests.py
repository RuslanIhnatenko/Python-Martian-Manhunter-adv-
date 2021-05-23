import pytest
from functions_to_test import Calculator


def test_add():
    assert Calculator.add(1, 2) == 3


def test_substract():
    assert Calculator.subtract(5, 4) == 1


def test_multiply():
    assert Calculator.multiply(5, 10) == 50


def test_divide():
    assert Calculator.divide(20, 2) == 10
    with pytest.raises(ValueError, match="Can not divide by zero!"):
        Calculator.divide(1, 0)
