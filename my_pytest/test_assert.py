import pytest

def add(a, b):
    return a + b


def is_prime(n):
    for i in (2, n):
        if n % i == 0:
            return False
        else:
            return True

def test_add_1():
    assert add(3, 4) == 7


def test_add2():
    assert add(3, 4) != 7


def test_add3():
    assert add(3, 4) <= 9


def test_add4():
    assert add(3, 4) >= 9


def test_in():
    a = 'hello world'
    b = 'hello'
    assert b in a


def test_not_in():
    a = 'hello'
    b = 'hi'
    assert b not in a


def test_true1():
    assert is_prime(7) is True


def test_true2():
    assert is_prime(8) is False


if __name__ == '__main__':
    pytest.main()
