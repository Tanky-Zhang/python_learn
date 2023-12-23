# 循环使用

# sum = 0
#
# for x in range(101):
#     print(x)
#
# print(sum)


# for x in range(1, 100, 2):
#     print(x)


# sum = 0
# for x in range(1, 100):
#     if x % 2 == 0:
#         sum += x
#
# print(sum)


# import random
#
# ansawer = random.randint(1, 100)
#
# counter = 0;
#
# while True:
#     counter += 1
#     number = int(input("请输入："))
#     if number < ansawer:
#         print("请大一点！")
#     elif number > ansawer:
#         print("请小一点")
#     else:
#         print('答对了')
#         break


for a in range(1, 10):
    for b in range(1, a + 1):
        print('%d*%d=%d' % (a, b, a * b), end='\t')
    print()
