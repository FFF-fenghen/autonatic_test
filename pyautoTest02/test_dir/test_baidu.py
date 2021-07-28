import sys
from time import sleep

from page.baidu_page import BaiduPage


class Testsearch:
    # 百度搜索类
    def test_baidu_search_case(self, browser, base_url):

        page=BaiduPage(browser)  # 打开BaiduPage类, 启动浏览器，并命名为page(如果命名为driver可能会比较熟悉，但是会冲突，所以这里就直接命名为page)
        page.get(base_url)  # 使用该类打开地址。
        page.search_input = 'pytest132'  # = 之后的内容时输入的内容
        page.search_button.click()
        sleep(2)
        assert browser.title == "pytest_百度搜索"
