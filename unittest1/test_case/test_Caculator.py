import unittest
from unittest1.test_case.Calculator import Calculator


class TestCalculator(unittest.TestCase):
    # 测试用例前置动作
    def setUp(self):
        print('test start:')

    # 测试用例后置动作
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
        # self.assertEqual(result, 15)
        self.assertEqual(result, 10)

    def test_div(self):
        c = Calculator(3, 3)
        result = c.div()
        self.assertEqual(result, 1)


# 断言函数使用
class TestAssert(unittest.TestCase):
    def test_equal(self):
        self.assertEqual(2 + 2, 4)
        self.assertEqual("python", "python")
        self.assertNotEqual("hello", 'python')

    def test_in(self):
        self.assertIn('hello', 'hello world')

    def test_true(self):
        self.assertTrue(True)
        self.assertFalse(True)


if __name__ == '__main__':
    # 创建测试套件
    suit = unittest.TestSuite()
    suit.addTest(TestCalculator('test_add'))
    suit.addTest(TestCalculator('test_sub'))
    suit.addTest(TestCalculator('test_mul'))
    suit.addTest(TestCalculator('test_div'))

    # 创建测试运行器
    runner = unittest.TextTestRunner()
    runner.run(suit)
    print("************")
    unittest.main()
