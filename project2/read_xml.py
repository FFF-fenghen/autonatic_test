from xml.dom.minidom import parse

dom = parse('file/config.xml')

root = dom.documentElement

tag_name = root.getElementsByTagName('os')

print(tag_name[0].firstChild.data)
print(tag_name[1].firstChild.data)
print(tag_name[2].firstChild.data)

# 获取标签的属性值

login_infos = root.getElementsByTagName('login')

for login_info in login_infos:
    print('uername:' + login_info.getAttribute('username'))
    print('password:' + login_info.getAttribute('password'))
