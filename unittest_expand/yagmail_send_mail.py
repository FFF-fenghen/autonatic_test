import yagmail

# 链接邮箱服务器
yag = yagmail.SMTP(user='f_archilleus@163.com', password='LCKXCECJCEGGBWSX', host='smtp.163.com')

# 邮件正文
contents = ['this is the pasage,and here is just text http']

# 发送邮件
yag.send('f_archilleus@163.com', 'subject', contents)
