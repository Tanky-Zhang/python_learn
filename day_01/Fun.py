# 函数和模块

def add():
    return 1 + 2


def add(a, b):
    return a + b


print(add(3, 4))


def add(a=0, b=0, c=9):
    return a + b + c


print(add(1, c=8, b=2))


