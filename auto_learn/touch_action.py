from selenium.webdriver.chrome.options import Options

from enviroment import *

opt = Options()
opt.add_experimental_option('w3c', False)
driver = webdriver.Chrome(options=opt)
driver.get("http://www.jq22.com/yanshi4976")
sleep(2)

# 切换到内嵌的表格
driver.switch_to.frame("iframe")
driver.find_element_by_id("appDate").click()

# 定位需要的年、月、日
dwwos = driver.find_elements_by_class_name("dwwo")
year = dwwos[0]
print(year.size)
month = dwwos[1]
day = dwwos[2]

action = webdriver.TouchActions(driver)

action.scroll_from_element(year, 0, 5).perform()
action.scroll_from_element(month, 0, 30).perform()
action.scroll_from_element(day, 0, 30).perform()

driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[2]/div[3]/span[1]").click()

sleep(20)


