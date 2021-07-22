import unittest
import time
from unittest_expand.HTMLTestRunner import HTMLTestRunner

test_dir = './test_case2'
suit = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')

if __name__ == '__main__':
    # 生成HTML格式报告
    now_time = time.strftime('%Y-%m-%d %H_%M_%S')
    fp = open('./test_report/'+now_time+'result.html', 'wb')
    runner = HTMLTestRunner(stream=fp, title='百度搜索测试报告', description='win:10,chrome')
    runner.run(suit)
    fp.close()
