import unittest
import time

import yagmail

from unittest_expand.HTMLTestRunner import HTMLTestRunner

# test_dir = './test_case2'
# suit = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')
#
# if __name__ == '__main__':
#     # 生成HTML格式报告
#     now_time = time.strftime('%Y-%m-%d %H_%M_%S')
#     fp = open('./test_report/'+now_time+'result.html', 'wb') # 如果没有这个文件，就会自己创建一个文件
#     runner = HTMLTestRunner(stream=fp, title='百度搜索测试报告', description='win:10,chrome')
#     runner.run(suit)
#     fp.close()


def send_email(report):
    receiver = '961977053@qq.com'
    subject = 'auto_test report'
    contents = 'more detail, open attachment'
    yag = yagmail.SMTP(user = 'f_archilleus@163.com',
                       host='smtp.163.com',
                       password='LCKXCECJCEGGBWSX'
                       )
    yag.send(receiver, subject, contents, report)


if __name__ == '__main__':
    test_dir = './test_case2'
    suit = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')
    now_time = time.strftime('%Y-%m-%d %H_%M_%S')
    report = './test_report'+now_time+'result.html'
    fp = open(report, 'wb')
    runner = HTMLTestRunner(stream=fp, title='百度自动测试报告', description='win10,chrome')  # stream 指生成报告的文件，必填
    runner.run(suit)
    fp.close()
    send_email(report)



