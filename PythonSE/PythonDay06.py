# -*- coding: UTF-8 -*- #
"""
@author:Bestlm
@file:PythonDay06.py
@time:2021/06/09/02/22
"""
"""
for in循环
"""
total = 0
for x in range(1, 100):
    total += x
print(total)

# range的使用 range(101) 产生0~100范围的整数，不包括101
a = 0
for x1 in range(101):
    a += x
print(a)
# range(1,101)产生1~100范围的整数
a1 = 0
for x2 in range(1, 101):
    a1 += x2
print(a1)
# range(1,101,2)产生1~100的奇数，2是步长意为每次数值递增的值
a2 = 0
for x3 in range(1, 101, 2):
    a2 += x3
print(a2)
# range(100, 0, -2)：可以用来产生100到1的偶数，其中-2是步长，即每次数字递减的值
a3 = 0
for x4 in range(100, 0, -2):
    a3 += x4
print(a3)

# 习题 1~100之间的偶数求和
a4 = 0
for x5 in range(2, 101, 2):
    a4 += x5
print(a4)
