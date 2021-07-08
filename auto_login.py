from selenium import webdriver
from time import ctime, sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
driver = webdriver.Chrome(r'D:\install\chromedriver.exe')
driver.implicitly_wait(10)

first_url = 'https://sso-test.topsky.com/'
driver.get(first_url)

change = driver.find_element_by_css_selector('.qyCode')
change.click()
phone = driver.find_element_by_css_selector('[placeholder="手机号码"]')
phone.send_keys('13764100640')
password = driver.find_element_by_css_selector('[placeholder="密码"]')
password.send_keys('666666')
enter = driver.find_element_by_css_selector('#submit')
sleep(0.5)
enter.send_keys(Keys.ENTER)

# 进入skytree素材库
enter = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div[4]")
enter.click()

# 进入智能投放
intelligent_delivery = driver.find_element_by_xpath("/html/body/div/div/div/div/ul/li[5]")
print(driver.title)
intelligent_delivery.click()
sleep(1)

#切换窗口到智能投放窗口
windows = driver.window_handles
driver.switch_to.window(windows[1])

# 进入管理后台
print(driver.title)
#点击智能投放
intelligent_delivery = driver.find_element_by_xpath("/html/body/div/div/div/div/div/div/ul/div[2]")
ActionChains(driver).move_to_element(intelligent_delivery).perform()

#进入智能投放
enter_kuaihsou=driver.find_element_by_xpath("/html/body/div/div/div[2]/section/div/div/div[3]/button")
enter_kuaihsou.send_keys(Keys.ENTER)

#切换窗口到快手投放窗口
windows = driver.window_handles
driver.switch_to.window(windows[2])
print(driver.title)

delivery_manage=driver.find_element_by_css_selector('.el-submenu__title')
ActionChains(driver).move_to_element(delivery_manage).perform()
delivery_manage.click()
sleep(1000)
driver.quit()
#https://skytree-test.topsky.com/?token=f8c42e5a771945edbea0281a1c8bad21
#https://skyads-test.topsky.com/?token=8d2346ff4cfe424c8b7b3fa7b5ce50b5