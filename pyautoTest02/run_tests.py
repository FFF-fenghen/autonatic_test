import os
import time
import logging
import click
import pytest
from conftest import REPORT_DIR
from config import RunConfig

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def init_env(new_report):
    os.mkdir(new_report)  # 新建文件夹
    os.mkdir(new_report + '/image')  # 在新建的文件夹下面再新建一个子文件夹。


@click.command()
@click.option('-m', default=None, help='输入运行模式： run 或debug.')
def run(m):
    if m is None or m == 'run':
        logger.info("回归模式，开始执行✈✈")  # logging 指的是运行系统的日志，写在运行界面里面。
        now_time = time.strftime('%Y_%m_%d_%H_%M_%S')
        RunConfig.NEW_REPORT = os.path.join(REPORT_DIR, now_time)  # 调用类里面的方法，生成文件夹地址。
        init_env(RunConfig.NEW_REPORT)  # 调用函数，根据设定的地址新建两个文件夹
        html_report = os.path.join(RunConfig.NEW_REPORT, 'report.html')  # html报告文档的地址
        xml_report = os.path.join(RunConfig.NEW_REPORT, 'junit-xml.xml')  # xml报告文档的地址
        pytest.main(['-s', '-v', RunConfig.cases_path, # 这一行命令表示打开运行RunConfig.NEW_REPORT的文件
                     # 调用了pytest,就会调动运行RunConfig.cases_path里面所有测试文件
                     '--html=' + html_report,  # 生成html命令
                     '--junit-xml=' + xml_report,  # 生成xml文件命令
                     '--self-contained-html',  #
                     '--maxfail', RunConfig.max_fail,  # 载入最大失败数命令
                     '--reruns', RunConfig.rerun])  # 载入实拍重跑次数命令
        logger.info('运行结束，生成测试报告！')
    elif m == 'debug':
        print("debug模式，开始执行！")
        pytest.main(["-v", "-s", RunConfig.cases_path])
        print("运行结束！！")


if __name__ == '__main__':
    run()
