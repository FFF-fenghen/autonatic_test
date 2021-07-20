with open('file/user_info.txt', 'r') as user_file:
    data = user_file.readlines()

# 格式化处理数据
users = []  #预置一个字符，以实现存储
for line in data:
    user = line[:-1].split(":") # line[:-1]可以对字符串进行切片，以省略最后一个字符，因为最后一个字符往往是换行字符。
    users.append(user)   # 实际上得到一个二维数组，但是这个二维数组是懂得原先表的构造之后才能够懂，是根据实际文本生成的
    # 打印 users 二维数组
    print(users)
