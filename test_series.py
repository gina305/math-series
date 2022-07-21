from series import sum_series,lucas,fibonacci
import pytest

sum_series(3)


def test_one():
    actual = sum_series(3,2,5)
    expected = 7
    assert actual == expected


def test_two():
    actual = sum_series(8)
    expected = 26
    assert actual == expected


def test_three():
    actual = sum_series(5)
    expected = 6
    assert actual == expected
