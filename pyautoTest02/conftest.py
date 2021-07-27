import os

import pytest
from py.xml import html
from selenium import webdriver
from selenium.webdriver import Remote
from selenium.webdriver.chrome.options import Options as CH_Options
from selenium.webdriver.firefox.options import Options as FF_Options
from config import RunConfig

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REPORT_DIR = BASE_DIR + '/test_report/'


@pytest.fixture(scrope='function')
def base_url():
    return RunConfig.url


def pytest_html_result_table_header(cells):
    cells.insert(2, html.th('description'))  # description 具体引用方式，显示位置在哪里？
    cells.pop()


def pytest_html_result_table_row(report, cells):
    cells.insert(2, html.td(report.description))  # report参数表示含义要搞清楚
    cells.pop()


def description_html(desc):
    if desc is None:
        return 'no case description'
    desc_ = ''
    for i in range(len(desc)):
        if i == 0:
            pass
        elif i == '\n':
            desc_ = desc_ + ';'
        else:
            desc_ = desc_ + desc[i]

    desc_lines = desc.split(';')
    desc_html = html.html(
        html.head(
            html.meta(name='Content-Type', value='test/html; charset=latin1')),  # charset设置位置不详
        html.body(
            [html.p(line) for line in desc_lines]))
    return desc_html


def capture_screenshots(case_name):
    global driver
    file_name = case_name.split('/')[-1]
    if RunConfig.NEW_REPORT is None:
        raise NameError('没有初始化测试报告目录')
    else:
        image_dir = os.path.join(RunConfig.NEW_REPORT, 'image', file_name)
        RunConfig.driver.save_screenshot(image_dir)


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin('html')  # item调用的什么东西，为什么会有这么多的类？
    outcome = yield  # 这个关键字表示什么含义
    report = outcome.get_result()  # outcome 哪里来的
    report.description = description_html(item.function.__doc__)  # 必须找到item
    extra = getattr(report, 'extra', [])
    if report.when == 'call' or report.when == 'setup':
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.fail and not xfail):
            case_path = report.nodeid.replace('::', '_') + '.png'
            if '[' in case_path:
                case_name = case_path.split('-')[0] + '].png'
            else:
                case_name = case_path
            capture_screenshots(case_name)
            img_path = 'image/' + case_name.split('/')[-1]
            if img_path:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % img_path
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


@pytest.fixture(scope='session', autouse=True)
def browser():
    global driver

    if RunConfig.driver_type == "chrome":
        # 本地chrome浏览器
        driver = webdriver.Chrome()
        driver.maximize_window()

    RunConfig.driver = driver

    return driver

@pytest.fixture(scope='session', autouse=True)
def browser_close():
    yield driver
    driver.quit()
    print('tst end!')