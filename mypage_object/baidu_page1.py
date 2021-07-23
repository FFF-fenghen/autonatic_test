from mypage_object.base1 import BasePage
from poium import Page, Element  # 这个标红是因为书写包的时候，包名导入不规范导致的，不影响程序的运行，只是无法跳转到被引用的文件当中


class BaiduPage(Page):  # 这个类负责查询百度页面之内的元素
    url = 'https://www.baidu.com'

    search_input = Element(id_="kw")
    search_button = Element(id_="su")
