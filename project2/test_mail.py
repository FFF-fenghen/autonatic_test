from pprint import pprint
from time import sleep
from selenium import webdriver
from project2.module import Mail

driver = webdriver.Chrome()
driver.get("https://mail.163.com/")
# 登录
# 调用 Mail 类并接收 driver 驱动
mail = Mail(driver)

# 登录
mail.login('f_archilleus','17e2070y537X@f')

# 退出
mail.logout()

driver.quit()

