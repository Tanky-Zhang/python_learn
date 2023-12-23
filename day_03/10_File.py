# 文件操作
import time


# 比Java的读取不知方便多少倍！！！！！！太甜了！！！！

# 整个读取
def main():
    f = open("../files/test01.txt", 'r', encoding='utf-8')
    print(f.read())
    f.close()


# 一行行读取
def main2():
    with open("../files/test01.txt", 'r', encoding='utf-8') as f:
        for line in f:
            # 如果不用‘’来结尾，会默认用换行来结尾
            print(line, end='')
            time.sleep(0.5)


lines = []


def main3():
    with open("../files/test01.txt", 'r', encoding='utf-8') as f:
        # 给全局变量赋值要声明global
        global lines
        lines = f.readlines()
    print(lines)


print('--------------------------------------------------------------------------------------------')


# 写入

def write1():
    with open('../files/test02.txt', 'w', encoding='utf-8') as f:
        for line in lines:
            f.write(line)


# if __name__ == '__main__':
#     main3()
#     write1()

print('--------------------------------------------------------------------------------------------')


# 读二进制

def bin_read():
    with open('../files/dog01.jpg', 'rb') as f1:
        data = f1.read()
        print(type(data))
    with open('../files/dog02.jpg', 'wb') as f2:
        f2.write(data)


# if __name__ == '__main__':
#     bin_read()

print('--------------------------------------------------------------------------------------------')

# 读取Json

import json


def json_write():
    mydict = {
        'name': '骆昊',
        'age': 38,
        'qq': 957658,
        'friends': ['王大锤', '白元芳'],
        'cars': [
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 320}
        ]
    }
    with open('../files/json.txt', 'w', encoding='utf-8') as fs:
        # fs.write(str(mydict))
        json.dump(mydict, fs)


if __name__ == '__main__':
    json_write()
