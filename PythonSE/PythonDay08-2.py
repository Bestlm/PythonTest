"""
简单封装
三数求和
"""


def add(a=0, b=0, c=0):
    """三个数求和"""
    return a + b + c


# 不传入参数，使用默认值
print(add())
# 传入三个参数
print(add(1, 2, 3))
# 传入一个参数
print(add(1))
# 传入两个参数
print(add(1, 2))
# 无序传参
print(add(c=1, b=2, a=3))

"""
可变参数
"""


def add2(*args):
    total = 0
    '''求和'''
    for num in args:
        total += num
    return total


print(add2(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
