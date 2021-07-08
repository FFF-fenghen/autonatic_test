from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(r'D:\install\chromedriver.exe')
driver.implicitly_wait(5)

driver.set_window_size(800,480)
first_url='https://www.baidu.com'
second_url='https://news.baidu.com'

driver.get('https://www.baidu.com')

above = driver.find_element_by_link_text("更多")
# 对定位到的元素执行鼠标悬停操作
ActionChains(driver).move_to_element(above).perform()

search_text = driver.find_element_by_id('kw')
size=search_text.size
att=search_text.get_attribute('type')
search_text.send_keys('seleniumm')
search_text.send_keys(Keys.BACK_SPACE)
search_text.send_keys(Keys.SPACE)
search_text.send_keys('教程')
search_text.send_keys(Keys.CONTROL,'a')
search_text.send_keys(Keys.CONTROL,'x')
search_text.send_keys(Keys.CONTROL,'v')
search_text.submit()

driver.quit()





''' 
# 通过这个对象来控制浏览器，比如打开浏览器，选择页面等。
driver = webdriver.Chrome(r'D:\install\chromedriver.exe')
# r 表表示后面的反斜杠不存在转义"

#设置最大等待时长为5秒钟。
driver.implicitly_wait(5)

# 使用webDriver的get方法打开网址
# wd.get('https://www.baidu.com')
driver.get('https://www.baidu.com/')

from selenium.webdriver.common.action_chains import ActionChains

ac = ActionChains(driver)

# 鼠标移动到 元素上
ac.move_to_element(driver.find_element_by_css_selector('[name="tj_briicon"]')).perform()
# 通过id选择元素，返回一个webelemnt对象.
#element = driver.find_element_by_id("input1")

#通过CSS 选择器选择元素
#elements = driver.find_elements_by_css_selector('.animal')

#通过任意属性来选择元素。
#element = driver.find_element_by_css_selector('[href="http://www.miitbeian.gov.cn"]')

#print(element.text)

# 清除输入框已有的字符串
#element.clear()

# 输入新字符串
#element.send_keys('你好')

#关闭窗口
driver.quit()

'''



