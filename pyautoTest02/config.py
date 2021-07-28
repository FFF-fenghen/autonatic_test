import os
PRO_PATH = os.path.dirname(os.path.abspath(__file__))


class RunConfig:
    cases_path = os.path.join(PRO_PATH, 'test_dir', 'test_baidu.py')
    driver_type = 'chrome'
    url = 'https://www.baidu.com'
    rerun = '1'
    max_fail = "5"
    driver = None  # 说明浏览器驱动不需要修改
    NEW_REPORT = None  # 表示报告路径不需要修改
