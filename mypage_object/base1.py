import time


class BasePage:   # 这个类封装了查找元素的方式，使得查找元素语句变得简单

    def __init__(self, driver):
        self.driver = driver

    def open(self, url=None):
        if url is None:
            self.driver.get(self.url)
        else:
            self.driver.get(url)

    def by_id(self, id1):
        return self.driver.find_element_by_id(id1)

    def by_name(self, name):
        return self.driver.find_element_by_name(name)

    def by_class(self, name):
        return self.driver.find_element_by_className(name)

    def by_Xpath(self, path):
        return self.driver.find_element_by_Xpath(path)

    def by_css(self, css):
        return self.driver.find_element_by_css_selector(css)

    def get_title(self):
        return self.driver.title

    def get_text(self, path):
        return self.driver.by_Xpath(path).text

    def js(self, script):
        self.driver.execute_script(script)