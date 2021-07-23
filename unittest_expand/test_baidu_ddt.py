from time import sleep
import unittest
from selenium import webdriver
from ddt import ddt, data, file_data, unpack


@ddt
class TestBaidu(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.url_base = 'https://www.baidu.com'

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def baidu_search(self, serach_key):
        self.driver.get(self.url_base)
        self.driver.find_element_by_id('kw').send_keys(serach_key)
        self.driver.find_element_by_id('su').click()
        sleep(2)

    @data(['case1', 'selenium'],
          ['case2', 'unttest'],
          ['case3', 'parameterized'])
    @unpack
    def test_search1(self, case, search_key):
        print('test class 1:', case)
        self.baidu_search(search_key)
        self.assertEqual(self.driver.title, search_key + '_百度搜索')

    @data(('case1', 'selenium'),
          ('case2', 'unttest'),
          ('case3', 'parameterized')
          )
    @unpack
    def test_search2(self, case, search_key):
        print('test class 2:', case)
        self.baidu_search(search_key)
        self.assertEqual(self.driver.title, search_key + '_百度搜索')

    @data({'search_key': 'selenium'},
          {'search_key': 'unttest'})
    @unpack
    def test_search3(self, search_key):
        print('test class 3:', search_key)
        self.baidu_search(search_key)
        self.assertEqual(self.driver.title, search_key + '_百度搜索')

    @file_data('./test_case2/ddt_data_file.json')
    def test_search4(self, search_key):
        print('test class 4:', search_key)
        self.baidu_search(search_key)
        self.assertEqual(self.driver.title, search_key + '_百度搜索')


if __name__ == '__main__':
    unittest.main(verbosity=2)
