import pytest
import math


@pytest.mark.parameteriz(
    [
        'base, exponent, expected',
        ('1','4','1'),
        ('2','2','4'),
        ('2','4','16')],
       dis = ['case1','case2','case3']
)
def test_pow(base,exponent,expected):
    assert math.pow(base,exponent) == expected

