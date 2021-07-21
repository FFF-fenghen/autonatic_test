import unittest


class MyTest(unittest.TestCase):

    @unittest.skip("直接跳过测试")   # 括号内的中文时输出的提示
    def test_skip(self):
        print('test aaa')

    @unittest.skipIf(3 > 2, '结果为真时跳过测试')
    def test_skip_if(self):
        print('test bbb')

    @unittest.skipUnless(3 > 2, "结果为真时执行测试")
    def test_skip_unless(self):
        print('test ccc')

    @unittest.expectedFailure
    def test_expectedFailure(self):
        self.assertEqual(2, 2)


if '__init__' == '__main__':
    unittest.main()
