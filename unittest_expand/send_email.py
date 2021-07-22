import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header

# 发送邮件主题
subject = 'welcome'

# 编写HTML 类型的邮件正文
with open('log.txt', 'rb') as f:
    send_att = f.read()

att = MIMEText(send_att, 'text', 'utf-8')  # 调用MIMEText模块定义文件正文，格式，编码
att['Content-Type'] = 'application/octet-stream'  # 指定附件内容类型，这里的内容类型是你二进制流
att['Content-Disposition'] = "attachment; filename='log.txt'"  # Disposition 指定显示附件的文件  attachment；filename='log.txt'指定附件的文件名。

msg = MIMEMultipart()  # 定义邮件的的主题
msg['subject'] = subject
msg.attach(att)  #

# 发送邮件
smtp = smtplib.SMTP()
smtp.connect('smtp.163.com')
smtp.login('f_archilleus@163.com', 'LCKXCECJCEGGBWSX')  # 这里用的是授权密码
smtp.sendmail('f_archilleus@163.com', 'f_archilleus@163.com', msg.as_string())
smtp.quit()
