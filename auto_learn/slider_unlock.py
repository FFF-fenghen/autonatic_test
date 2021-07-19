from pprint import pprint

from selenium import webdriver
from time import ctime, sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import UnexpectedAlertPresentException

driver = webdriver.Chrome()
driver.implicitly_wait(10)

current_url = r'https://agent.e.kuaishou.com'
driver.get(current_url)
# 以最大窗口播放
driver.maximize_window()
sleep(1)
phone = driver.find_element_by_xpath('//*[@id="login"]/div/form/div[1]/div[1]/div/input')
phone.send_keys('18361272556')
password = driver.find_element_by_xpath('//*[@id="login"]/div/form/div[2]/div/div/input')
password.send_keys('tian18361272556')
agree = driver.find_element_by_xpath('//*[@id="login"]/div/form/div[3]/div/label')
agree.click()
enter = driver.find_element_by_xpath('//*[@id="login"]/div/form/div[3]/button')
enter.click()
sleep(1)

login_frame = driver.find_element_by_xpath('/html/body/div[4]/iframe')
# 进入内嵌的表单。
driver.switch_to.frame(login_frame)

# 定位表单内的滑动块
slider = driver.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/div')
sleep(1)
action = ActionChains(driver)

dis = 230
for index in range(200):
    if dis > 300:
        dis = 220
    # 但滑动解锁成功，页面URL发生变化，当前url作为是非跳转的判断依据
    current_url = driver.current_url
    action.click_and_hold(slider).perform()
    action.move_by_offset(dis, 0).perform()
    action.release()
    action.reset_actions()
    sleep(10)
    dis = dis + 5
    if current_url != driver.current_url:
        print(driver.current_url)
        break
    else:
        current_url = driver.current_url

# 打印警告框提示
success_text = driver.switch_to.alert.text
print(success_text)

from pprint import pprint

from selenium import webdriver
from time import ctime, sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import UnexpectedAlertPresentException

driver = webdriver.Chrome()
driver.implicitly_wait(10)

current_url = r'https://agent.e.kuaishou.com'
driver.get(current_url)
# 以最大窗口播放
driver.maximize_window()
sleep(1)
phone = driver.find_element_by_xpath('//*[@id="login"]/div/form/div[1]/div[1]/div/input')
phone.send_keys('18361272556')
password = driver.find_element_by_xpath('//*[@id="login"]/div/form/div[2]/div/div/input')
password.send_keys('tian18361272556')
agree = driver.find_element_by_xpath('//*[@id="login"]/div/form/div[3]/div/label')
agree.click()
enter = driver.find_element_by_xpath('//*[@id="login"]/div/form/div[3]/button')
enter.click()
sleep(1)

login_frame = driver.find_element_by_xpath('/html/body/div[4]/iframe')
# 进入内嵌的表单。
driver.switch_to.frame(login_frame)

# 定位表单内的滑动块
slider = driver.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/div')
sleep(1)
action = ActionChains(driver)

dis = 230
for index in range(200):
    if dis > 300:
        dis = 220
    # 但滑动解锁成功，页面URL发生变化，当前url作为是非跳转的判断依据
    current_url = driver.current_url
    action.click_and_hold(slider).perform()
    action.move_by_offset(dis, 0).perform()
    action.release()
    action.reset_actions()
    sleep(10)
    dis = dis + 5
    if current_url != driver.current_url:
        print(driver.current_url)
        break
    else:
        current_url = driver.current_url

# 打印警告框提示
success_text = driver.switch_to.alert.text
print(success_text)

