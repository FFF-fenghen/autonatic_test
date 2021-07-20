import unittest
from unittest1.Calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        print('test start:')

    def tearDown(self):
        print('test end')

    def test_add(self):
        c = Calculator(3, 5)
        result = c.add()
        self.assertEqual(result, 8)

    def test_sub(self):
        c = Calculator(3, 5)
        result = c.sub()
        self.assertEqual(result, -2)

    def test_mul(self):
        c = Calculator(3, 5)
        result = c.mul()
        #self.assertEqual(result, 15)
        self.assertEqual(result, 10)

    def test_div(self):
        c = Calculator(3, 3)
        result = c.div()
        self.assertEqual(result, 1)

if __name__ == '__main__':
    #创建测试套件
    suit = unittest.TestSuite
    suit.addTest(TestCalculator('test_add'))
    suit.addTest(TestCalculator('test_sub'))
    suit.addTest(TestCalculator('test_mul'))
    suit.addTest(TestCalculator('test_div'))

    #创建测试运行器
    runner = unittest.TextTestRunner()
    runner.run(suit)
