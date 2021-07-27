import sys
from time import sleep

from page.baidu_page import BaiduPage


class Testsearch:
    # 百度搜索类
    def test_baidu_search_case(self, browser, base_url):

        page=BaiduPage(browser)
        page.get(base_url)
        page.search_input = 'pytest'  # = 之后的内容时输入的内容
        page.search_button.click()
        sleep(2)
        assert browser.title == "pytest_百度搜索"
