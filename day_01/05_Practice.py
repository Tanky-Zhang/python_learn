# 一些练习题

# 水仙花数
for num in range(100, 1000):
    low = num % 10
    mid = num // 10 % 10
    hig = num // 100
    if low ** 3 + mid ** 3 + hig ** 3 == num:
        print(num)
        print()


