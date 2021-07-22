import csv
import codecs
import unittest
from time import sleep, time
from selenium import webdriver
from itertools import islice
from parameterized import parameterized


# @unittest.skip("直接跳过测试")
class TestBaidu(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.base_url = 'https://www.baidu.com'

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def baidu_search(self, search_key):
        self.driver.get(self.base_url)
        self.driver.find_element_by_id('kw').send_keys(search_key)
        self.driver.find_element_by_id('su').click()
        sleep(2)
        self.assertEqual(self.driver.title, search_key + "_百度搜索")

    @parameterized.expand([
        ('case1', 'selenium'),   # 每一个元组可以被认为是一个测试用例
        ('case2', 'unttest'),
        ('case3', 'parameterized'),
    ])
    def test_search(self, name, search_key):
        self.baidu_search(search_key)
        self.assertEqual(self.driver.title, search_key + '_百度搜索')


if __name__ == '__main__':
    unittest.main(verbosity=2)
