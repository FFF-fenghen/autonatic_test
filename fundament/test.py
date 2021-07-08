from project2.calculator import add
import sys
from os.path import dirname,abspath
project_path = dirname(dirname(abspath(__file__)))     #dirname()用于获取上一级目录的路径。
print(project_path)
print(add(1,2))
