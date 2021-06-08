# -*- coding: UTF-8 -*- #
"""
@author:Bestlm
@file:PythonDay07.py
@time:2021/06/09/02/38
"""
import random

"""
猜数字游戏
规则：计算机出一个1到100之间的随机数，玩家输入自己猜的数字，
计算机给出对应的提示信息（大一点、小一点或猜对了），如果玩家猜中了数字，
计算机提示用户一共猜了多少次，游戏结束，否则游戏继续。
"""
answer = random.randint(1, 100)
counters = 0
while True:
    counters += 1
    number = int(input('请输入：'))
    if number < answer:
        print('大一点')
    elif number > answer:
        print('小一点')
    else:
        print('猜对了')
        break
print(f'总共猜了{counters}次')
