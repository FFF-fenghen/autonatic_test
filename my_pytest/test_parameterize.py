import pytest
import math


@pytest.mark.parametrize(
    'base, exponent, expected',
    [(1, 4, 1),
     (2, 2, 4),
     (2, 4, 16)],
    ids=['case1', 'case2', 'case3']
    )
def test_pow(base, exponent, expected):
    assert math.pow(base, exponent) == expected


if __name__ == '__main__':
    pytest.main()  # 这个pytest.main() 会运行锁头mytest里面test开头的函数，或者说方法。
