from select import select

from selenium import webdriver
from time import sleep, time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get('https://wwww.baidu.com')
driver.implicitly_wait(10)

#打开搜索设置
link=driver.find_element_by_css_selector('#s-usersetting-top')
link.click()
driver.find_element_by_link_text("搜索设置").click()
sleep(1)

'''
#修改设置
enter=driver.find_element_by_css_selector('span#se-setting-3>span:nth-child(2)')
print(enter.size)
enter.click()
#保存设置
enter=driver.find_element_by_css_selector('.prefpanelgo')
enter.click()
'''
sel=driver.find_element_by_css_selector('span#se-setting-3')
Select(sel).select_by_visible_text('每页50条')

#获取警告框
alert=driver.switch_to.alert
print(alert.text)

#接受警告框
alert.accept()

sleep(122)
driver.quit()