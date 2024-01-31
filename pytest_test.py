"""
pytest test_your_module.py  # замените на имя вашего тестового файла

"""

import pytest
from 8_kyu.century import century


def test_century():
    assert century(100) == 1
    assert century(101) == 2
    assert century(200) == 2
    assert century(201) == 3
    assert century(1700) == 17
    assert century(1801) == 19


@pytest.mark.parametrize("year, expected", [
    (100, 1),
    (101, 2),
    (200, 2),
    (201, 3),
    (1700, 17),
    (1801, 19),
])
def test_century_parametrized(year, expected):
    assert century(year) == expected
