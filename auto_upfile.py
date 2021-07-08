import os
from selenium import webdriver
from time import ctime, sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(r'D:\install\chromedriver.exe')
#driver.maximize_window()
driver.implicitly_wait(10)

'''
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
'''

driver.get(r'https://skytree-test.topsky.com/?token=f7884e48346b4523953a22566087a278')
# 进入素材管理
matirial_manage = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[1]/ul/li[1]/span')
matirial_manage.click()

# 进入需求制作
demand_make = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/ul/li[3]')
demand_make.click()
sleep(0.5)

# 点击文件自动上传
driver.find_element_by_xpath(
    '//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[3]/div[3]/table/tbody/tr[1]/td[8]/div/div/button/span/span').click()
sleep(0.5)

# 点击“上传”
driver.find_element_by_xpath(
    '//*[@id="app"]/div/div[2]/div[2]/div/div[5]/div[1]/div/div/div[2]/div/div[3]/div[4]/div[2]/table/tbody/tr/td[11]/div/div/span[1]/button').click()
sleep(0.5)

# 选择文件上传,弹出选择文件提示框
upfile = driver.find_element_by_xpath(
    '//*[@id="app"]/div/div[2]/div[2]/div/div[5]/div[2]/div/div/div[2]/form/div/div/div/div/div/div[1]/ul/li/div/div[1]/div/button')
upfile.click()
sleep(0.5)

#使用dutoit自动上传功能
com = r"C:\Users\achilleus\Desktop\script.exe"
d = os.popen(com)
sleep(15)

# 点击“视频上传”中的“保存”
storage = driver.find_element_by_xpath(
    '//*[@id="app"]/div/div[2]/div[2]/div/div[5]/div[2]/div/div/div[3]/span/button[2]')
storage.click()
sleep(455)

# 点击“保存”
storage = driver.find_element_by_xpath(
    '//*[@id="app"]/div/div[2]/div[2]/div/div[5]/div[1]/div/div/div[3]/span/button[2]')
storage.click()
sleep(0.5)


sleep(1233)

# "C:\Users\achilleus\Desktop\script.exe" "chrome" "C:\Users\achilleus\Desktop\5.mp4"
#https://skytree-test.topsky.com/?token=aaaeea231b904737a0494956902ab3e5
