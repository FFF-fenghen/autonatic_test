import os
from time import sleep
from selenium import webdriver

driver = webdriver.Chrome()
file_path = os.path.abspath('./')

#打开本地html文件
upload_page =  'file:///'+file_path + r'\upfile.html'
driver.get(upload_page)


# 定位上传按钮，添加本地文件
input= driver.find_element_by_id("inputfile")
print(input.size)
path=r'E:\vedio\hengbna1280_720\5.mp4'
print(path)
input.send_keys(path)

submit=driver.find_element_by_css_selector('.btn-default')
submit.click()

sleep(2)
# ……


'''
input.send_keys(file_path + r'\alert_deal.py')
print(file_path + r'\alert_deal.py')
'''