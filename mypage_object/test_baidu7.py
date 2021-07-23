import unittest
from time import sleep
from selenium import webdriver
from mypage_object.baidu_page1 import BaiduPage
from poium import webdriver as we

class TestBaidu(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.base_url = 'https://www.baidu.com'

    def test_search_case1(self):
        page = BaiduPage(self.driver)  # 用驱动器驱动这个类
        page.get(self.base_url)
        page.search_input = 'selenium'  # 这里的等号表示的是输入的内容
        page.search_button.click()
        sleep(2)
        aa = we.Page(self.driver)  # poium/webdriver里面有一个类，是Page，驱动器self.driver去运行这个类
        # print(123546879)         # 这个类里面有一个方法是get_title,返回运行界面的主题
        # title = aa.get_title
        self.assertEqual(aa.get_title, 'selenium_百度搜索')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
