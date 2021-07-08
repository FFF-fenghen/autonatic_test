from enviroment import *
driver = webdriver.Chrome()

driver.get("https://www.baidu.com")
cookies=driver.get_cookies()
for cookie in driver.get_cookies():
 a=cookie['name']
 b=cookie['value']
 print(a)
 print(b)
pprint(cookies)
driver.delete_all_cookies()

print('***')
driver.add_cookie({'name': 'key-aaaaaaa', 'value': 'value-bbbbbb', 'expiry': 1626593577})
cookies=driver.get_cookies()
pprint(cookies)
print('***')


# for cookie in cookies:
#     print(cookies['name'])
# names=driver.get_cookie(['name'])
# print(names)

driver.quit()
sleep(1)
