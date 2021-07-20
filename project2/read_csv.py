import csv
import codecs
from itertools import islice
from pprint import pprint

data = csv.reader(codecs.open('file/cscvFile.csv', "r", 'gb2312'))

users = []

for line in islice(data, 1, 5):  # 第一个参数表示迭代的对象，第二个参数表hi是开始位置，这里的1表示的是第一行，第三个参数表示结束位置。
    users.append(line)

pprint(users)
