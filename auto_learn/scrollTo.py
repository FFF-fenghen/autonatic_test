from time import sleep

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.set_window_size(800, 600)
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()

# 编写脚本，之后自动运行脚本
js = 'window.scrollTo(100,450)'
sleep(13544)
driver.quit()

# vjs_video_3 > button > span.vjs-icon-placeholder
