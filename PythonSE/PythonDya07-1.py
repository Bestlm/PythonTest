# -*- coding: UTF-8 -*- #
"""
@author:Bestlm
@file:PythonDya07-1.py
@time:2021/06/09/02/48
嵌套的循环结构-99乘法表
"""
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f'{i} * {j}', end='\t')
    print()

"""
判断一个数是不是素数
素数是只能被1和自身整除的大于1的数
"""
num = int(input('请输入一个整数：'))
# 只能被自身整除
# 素数>1
if num >= 2:
    # 素数的判断
    for x in range(2, num):
        if (num % x) == 0:
            print(f'输入的数字{num}不是素数')
            print(x, "乘", num//x, "是", num)
            # print(f'{num}以内的数字{i}是素数')
            break
    else:
        print(f'输入的数字{num}是素数')
# 输入的数字<=1,不是素数
else:
    print(f'输入的数字{num}不是素数')
