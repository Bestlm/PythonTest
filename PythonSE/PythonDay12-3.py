"""
元组和列表的比较
元组是不可变类型，更适合多线程环境
元组是不可变类型，不可变类型在创建时间和占用空间上优于可变类型
"""
import sys
import timeit

a = list(range(100000))
b = tuple(range(100000))
print(sys.getsizeof(a), sys.getsizeof(b))
print(timeit.timeit('[1,2,3,4,5,6,7,8,9]'))
print(timeit.timeit('[1,2,3,4,5,6,7,8,9]'))

# 列表和元组互转

# 将元组转换成列表
info = ('测试', 180, True, '成都')
print(list(info))

# 将列表转换为元组
info2 = ['apple', 'banana', 'orange']
print(tuple(info2))
