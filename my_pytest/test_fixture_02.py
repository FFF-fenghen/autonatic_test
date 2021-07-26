def multiply(a, b):
    return a * b


class TestFixture:
    @classmethod
    def setup_class(cls):
        print('test_class start')

    @classmethod
    def teardown_class(cls):
        print('test_class_end')

    def setup_method(self):
        print('test_method')

    def teardown_method(self):
        print('test_method_end')

    def setup(self):
        print('test_setup')

    def teardown(self):
        print('test_teardown')

    def test_multiply_5_6(self):
        print('test_multiply_5_6')
        assert multiply(5, 6) == 30

    def test_multiply_in(self):
        print('test_multiply_in')
        assert multiply(3, 'a') in 'aaaa'
