import unittest


def setUpModule():   # 直接在类外面进行使用，在整个模块的开始与结束时被执行。
    print("module start >>>>>>>>")


def tearDownModule():
    print("module end <<<<<<<<<<<<")


class MyTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('class start ******')

    @classmethod      # 以此声明，讲setUp作为类级别的标记符号来使用，  # 以此声明，讲setUp作为类级别的标记符号来使用，
    def tearDownClass(cls):
        print('test class end ******')

    def setUp(self):       # 在测试用例的开始与结束时被执行。
        print('test case start.....')

    def tearDown(self):
        print('test case end...')

    def test_case1(self):
        print('test case 1')

    def test_case2(self):
        print('test case 2')


if '__init__' == '__main__':
    unittest.main()
