import yagmail

# 链接邮箱服务器
yag = yagmail.SMTP(user='f_archilleus@163.com', password='LCKXCECJCEGGBWSX', host='smtp.163.com')

# 邮件正文
contents = ['this is the pasage,and here is just text http,this time i will send to many people']

# 发送邮件
yag.send(['f_archilleus@163.com', '961977053@qq.com'], 'subject', contents, ["E:/auto_learn/autonatic_test/unittest_expand/log.txt"])
