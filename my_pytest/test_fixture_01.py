def multiply(a, b):
    return a * b


def setup_module(module):
    print('module_test_start*******')


def teardown_module(module):
    print('module_test_end*****')


def setup_function(function):
    print('function_test_start***')


def teardown_function(function):
    print('function_test_end')


def setup():
    print('setup_start')


def teardown():
    print('teardown_end')


def test_mutiply_3_4():
    assert multiply(3, 4) == 12
    print('test_334')


def test_mutiply_3_a():
    assert multiply(3, 'a') == 'aaa'
    print('test_3a')

    


