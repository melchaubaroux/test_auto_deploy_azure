import pytest


def product(*liste):
    total = 1
    for x in liste:
        total *= x
    return total


def test_product():
    assert product(2, 5) == 10


test_product()
