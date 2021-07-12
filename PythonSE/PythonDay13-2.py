"""
双色球
红球范围:01~33
蓝球范围:01~16
每期从33个红球中开出6个号码,从16个蓝球中开出1个号码
"""

# 33个红球开6个,需不重复的 sample
# 红球需要sort排序,个位数需要补零
from random import sample, randint


def display(balls):
    """
    输出列表中的双色球号码
    :param balls:
    :return:
    """
    for index, ball in enumerate(balls):
        if index == len(balls) - 1:
            print('|', end=' ')
        print(f'{ball:0>2d}', end=' ')
    print()


def random_select():
    """随机选择一组号码"""
    # 用生成式生成1到33号的红色球
    red_balls = [x for x in range(1, 34)]
    # 无放回随机抽样的方式选中6个红色球
    selected_balls = sample(red_balls, 6)
    # 对红色球进行排序
    selected_balls.sort()
    # 用1到16的随机数表示选中的蓝色球并追加到列表汇总
    selected_balls.append(randint(1, 16))
    return selected_balls


n = int(input('机选几注: '))
for _ in range(n):
    display(random_select())
