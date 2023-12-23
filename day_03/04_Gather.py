# 集合 ,类似于Java中的set不允许变量重复

# 创建集合的字面量语法
set1 = {1, 2, 3, 3, 3, 2}
print(set1)

print('Length=', len(set1))

# 创建集合的构造器语法(面向对象部分会进行详细讲解)
set2 = set(range(1, 10))
set3 = set((1, 2, 3, 3, 2, 1))
print(set2, set3)

# 创建集合的推导式语法(推导式也可以用于推导集合)
set4 = {num for num in range(1, 100) if num % 3 == 0 or num % 5 == 0}
print(set4)

set1.add(10)
print(set1)

# 在原来集合的基础上增加11，12两个数字
set2.update([11, 12])
print(set2)

# 丢掉第五个元素，也就是下标为4的元素
set2.discard(5)
print(set2)

print('--------------------------------------------------------------------------------------------')

# 集合的成员、交集、并集、差集等运算。

set1 = {1, 2, 3, 3, 3, 2}
set2 = set(range(1, 10))


# 集合的交集、并集、差集、对称差运算
print(set1 & set2)
# print(set1.intersection(set2))

print(set1 | set2)
# print(set1.union(set2))


print(set1 - set2)
# print(set1.difference(set2))
print(set1 ^ set2)
# print(set1.symmetric_difference(set2))



# 判断子集和超集
print(set2 <= set1)
# print(set2.issubset(set1))
print(set3 <= set1)
# print(set3.issubset(set1))
print(set1 >= set2)
# print(set1.issuperset(set2))
print(set1 >= set3)
# print(set1.issuperset(set3))
