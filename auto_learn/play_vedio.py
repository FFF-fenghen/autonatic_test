from enviroment import *
driver = webdriver.Chrome()
driver.get("http://videojs.com/")
video = driver.find_element_by_id("preview-player_html5_api")

#返回播放文件的地址
url=driver.execute_script("return arguments[0].currentSrc;",video)
print(url)

args=driver.execute_script("return arguments;",video)
for arg in args:
    pprint(arg)

#播放视频
print('start')
driver.execute_script('arguments[0].play()',video)

#播放15秒
sleep(5)

#暂停视频
print('pause')
driver.execute_script('arguments[0].pause()',video)

driver.quit()

