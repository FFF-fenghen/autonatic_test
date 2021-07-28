# import os
#
# import pytest
# from py.xml import html
# from selenium import webdriver
# from selenium.webdriver import Remote
# from selenium.webdriver.chrome.options import Options as CH_Options
# from selenium.webdriver.firefox.options import Options as FF_Options
# from config import RunConfig
#
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# REPORT_DIR = BASE_DIR + '/test_report/'
#
#
# @pytest.fixture(scope='function')
# def base_url():
#     return RunConfig.url
#
#
# def pytest_html_results_table_header(cells):
#     cells.insert(2, html.th('description'))  # description 具体引用方式，显示位置在哪里？
#     cells.pop()
#
#
# def pytest_html_results_table_row(report, cells):
#     cells.insert(2, html.td(report.description))  # report参数表示含义要搞清楚
#     cells.pop()
#
#
# def description_html(desc):
#     if desc is None:
#         return 'no case description'
#     desc_ = ''
#     for i in range(len(desc)):
#         if i == 0:
#             pass
#         elif i == '\n':
#             desc_ = desc_ + ';'
#         else:
#             desc_ = desc_ + desc[i]
#
#     desc_lines = desc.split(';')
#     desc_html = html.html(
#         html.head(
#             html.meta(name='Content-Type', value='test/html; charset=latin1')),  # charset设置位置不详
#         html.body(
#             [html.p(line) for line in desc_lines]))
#     return desc_html
#
#
# def capture_screenshots(case_name):
#     global driver
#     file_name = case_name.split('/')[-1]
#     if RunConfig.NEW_REPORT is None:
#         raise NameError('没有初始化测试报告目录')
#     else:
#         image_dir = os.path.join(RunConfig.NEW_REPORT, 'image', file_name)
#         RunConfig.driver.save_screenshot(image_dir)
#
#
# @pytest.mark.hookwrapper
# def pytest_runtest_makereport(item, call):
#     pytest_html = item.config.pluginmanager.getplugin('html')  # item调用的什么东西，为什么会有这么多的类？
#     outcome = yield  # 这个关键字表示什么含义
#     report = outcome.get_result()  # outcome 哪里来的
#     report.description = description_html(item.function.__doc__)  # 必须找到item
#     extra = getattr(report, 'extra', [])
#     if report.when == 'call' or report.when == 'setup':
#         xfail = hasattr(report, 'wasxfail')
#         if (report.skipped and xfail) or (report.fail and not xfail):
#             case_path = report.nodeid.replace('::', '_') + '.png'
#             if '[' in case_path:
#                 case_name = case_path.split('-')[0] + '].png'
#             else:
#                 case_name = case_path
#             capture_screenshots(case_name)
#             img_path = 'image/' + case_name.split('/')[-1]
#             if img_path:
#                 html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
#                        'onclick="window.open(this.src)" align="right"/></div>' % img_path
#                 extra.append(pytest_html.extras.html(html))
#         report.extra = extra
#
#
# @pytest.fixture(scope='session', autouse=True)
# def browser():
#     global driver
#
#     if RunConfig.driver_type == "chrome":
#         # 本地chrome浏览器
#         driver = webdriver.Chrome()
#         driver.maximize_window()
#     RunConfig.driver = driver
#
#     return driver
#
#
# @pytest.fixture(scope='session', autouse=True)
# def browser_close():
#     yield driver
#     driver.quit()
#     print('test end!')


import os
import pytest
from py.xml import html
from selenium import webdriver
from selenium.webdriver import Remote
from selenium.webdriver.chrome.options import Options as CH_Options
from selenium.webdriver.firefox.options import Options as FF_Options
from config import RunConfig

# 项目目录配置
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # 定位到 pyautoTest 文件
REPORT_DIR = BASE_DIR + "/test_report/"  # 定位存放报告路径


# 定义基本测试环境
@pytest.fixture(scope='function')  # 可以直接调用钩子函数
def base_url():
    return RunConfig.url  # 返回类里面的写定参数，目前基本测试环境只有地址，暂不知道还能够配置些什么


# 设置用例描述表头
def pytest_html_results_table_header(cells):
    cells.insert(2, html.th('Description'))  # 引用的时py.xml里面的html
    cells.pop()


# 设置用例描述表格
def pytest_html_results_table_row(report, cells):
    cells.insert(2, html.td(report.description))  # 采用html语法编写报告格式
    cells.pop()


@pytest.mark.hookwrapper  # 判断每条测试用例的运行情况，出错或者失败时，调用capture_screenshot()函数进行截图。
def pytest_runtest_makereport(item):
    """
    用于向测试用例中添加用例的开始时间、内部注释，和失败截图等.
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')  # ???
    outcome = yield
    report = outcome.get_result()
    report.description = description_html(item.function.__doc__)
    extra = getattr(report, 'extra', [])    # getattr 是python内置函数，返回对象的一个属性值
    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')  # python内置函数，判断对象是否包含对应的属性。
        # 这个语句用来判断：测试用例是否运行错误，错误返回真
        if (report.skipped and xfail) or (report.failed and not xfail):
            case_path = report.nodeid.replace("::", "_") + ".png"  # 生成截图地址
            if "[" in case_path:
                case_name = case_path.split("-")[0] + "].png"  # 生成图片名称
            else:
                case_name = case_path
            capture_screenshots(case_name)  # 截屏并保存到文件夹中
            img_path = "image/" + case_name.split("/")[-1]
            if img_path:  # 绘制div格子载入图片
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % img_path
                extra.append(pytest_html.extras.html(html))  # html文档中载入图片
        report.extra = extra


def description_html(desc):
    """
    将用例中的描述转成HTML对象
    :param desc: 描述
    :return:
    """
    if desc is None:
        return "No case description"
    desc_ = ""
    for i in range(len(desc)):
        if i == 0:
            pass
        elif desc[i] == '\n':
            desc_ = desc_ + ";"
        else:
            desc_ = desc_ + desc[i]

    desc_lines = desc_.split(";")
    desc_html = html.html(
        html.head(
            html.meta(name="Content-Type", value="text/html; charset=latin1")),  # html语法规则，将用例描述转换成HTML对象
        html.body(
            [html.p(line) for line in desc_lines]))
    return desc_html


def capture_screenshots(case_name):
    """
    配置用例失败截图路径
    :param case_name: 用例名
    :return:
    """
    global driver
    file_name = case_name.split("/")[-1]
    if RunConfig.NEW_REPORT is None:
        raise NameError('没有初始化测试报告目录')
    else:
        image_dir = os.path.join(RunConfig.NEW_REPORT, "image", file_name)
        RunConfig.driver.save_screenshot(image_dir)


# 启动浏览器
@pytest.fixture(scope='session', autouse=True)
def browser():
    """
    全局定义浏览器驱动
    :return:
    """
    global driver

    if RunConfig.driver_type == "chrome":
        # 本地chrome浏览器
        driver = webdriver.Chrome()
        driver.maximize_window()

    elif RunConfig.driver_type == "firefox":
        # 本地firefox浏览器
        driver = webdriver.Firefox()
        driver.maximize_window()

    elif RunConfig.driver_type == "chrome-headless":
        # chrome headless模式
        chrome_options = CH_Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument('--disable-gpu')
        # chrome_options.add_argument("--window-size=1920x1080")
        driver = webdriver.Chrome(options=chrome_options)

    elif RunConfig.driver_type == "firefox-headless":
        # firefox headless模式
        firefox_options = FF_Options()
        firefox_options.headless = True
        driver = webdriver.Firefox(firefox_options=firefox_options)

    elif RunConfig.driver_type == "grid":
        # 通过远程节点运行
        driver = Remote(command_executor='http://localhost:4444/wd/hub',
                        desired_capabilities={
                            "browserName": "chrome",
                        })
        driver.set_window_size(1920, 1080)

    else:
        raise NameError("driver驱动类型定义错误！")

    RunConfig.driver = driver

    return driver


# 关闭浏览器
@pytest.fixture(scope="session", autouse=True)
def browser_close():
    yield driver  # 进入driver， 然后暂停，挂着，知道driver执行完，再进行这个任务
    driver.quit()
    print("test end!")


if __name__ == "__main__":
    capture_screenshots("test_dir/test_baidu_search.test_search_python.png")
