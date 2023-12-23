# list操作
import sys

list1 = [1, 3, 5, 7, 10]

print(list1)

# 乘号表示列表元素的重复
list2 = ['hello'] * 3
print(list2)

# 计算列表的元素个数

print(len(list2))

print(list2[0])
# 取倒数第一个
print(list1[-1])
print(list1[-3])

list1[2] = 300
print(list1)

for e in list1:
    print(e)

for index, e in enumerate(list1):
    print(index, e)

print('--------------------------------------------------------------------------------------------')

list1.append(200)
print(list1)
# 会往后挤一个
list1.insert(1, 400)
print(list1)

list1.extend([1000, 2000])
list1 += [8000, 9000]
print(list1)

print('--------------------------------------------------------------------------------------------')

# 好爽啊，不用像Java一般
if 9000 in list1:
    list1.remove(9000)

print(list1)

list1.pop(0)

print('--------------------------------------------------------------------------------------------')

# 切片

fruits = ['grape', 'apple', 'strawberry', 'waxberry']
fruits += ['pitaya', 'pear', 'mango']

fruits2 = fruits[1:4]
print(fruits2)

fruits3 = fruits[:]
print(fruits3)

fruits4 = fruits[-3:-1]
print(fruits4)

# 反转
fruits4 = fruits[::-1]
print(fruits4)

print('--------------------------------------------------------------------------------------------')

# 排序

list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']

# 首字母排序
list2 = sorted(list1)
print(list2)

# 排序反转
list3 = sorted(list1, reverse=True)
print(list3)

list4 = sorted(list1, key=len, reverse=True)
print(list4)

# 自排序
list1.sort()
print(list1)

print('--------------------------------------------------------------------------------------------')

# 生成式和生成器

f = [x for x in range(0, 100)]
print(f)

# 好叼啊，这个糖快把我甜死了
f = [x + y for x in 'ABCD' for y in '123456']
print(f)

# 用列表的生成表达式语法创建列表容器
# 用这种语法创建列表之后元素已经准备就绪所以需要耗费较多的内存空间
f = [x ** 2 for x in range(1, 1000)]
print(sys.getsizeof(f))  # 查看对象占用内存的字节数
print(f)

# 请注意下面的代码创建的不是一个列表而是一个生成器对象
# 通过生成器可以获取到数据但它不占用额外的空间存储数据
# 每次需要数据的时候就通过内部的运算得到数据(需要花费额外的时间)
f = (x ** 2 for x in range(1, 1000))
print(sys.getsizeof(f))
print(f)


# for val in f:
#     print(val)


# 除了上面提到的生成器语法，Python中还有另外一种定义生成器的方式，就是通过yield关键字将一个普通函数改造成生成器函数


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a;


def main():
    for val in fib(20):
        print(val)


if __name__ == '__main__':
    main()

