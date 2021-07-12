"""
元组的应用场景
"""
# 打包和解包操作
# 打包 --把多个逗号分隔的值赋给一个变量时，多个值会打包成一个元组类型
a = 1, 10, 100
print(type(a), a)
# 解包 --把一个元组赋值给多个变量时，元组会解包成多个值然后分别赋给对应的变量
i, j, k = a
print(i, j, k)
# 变量数与元组解包出来的元素个数不等
a1 = 1, 10, 100, 1000
# i, j, k = a1
# ValueError: too many values to unpack (expected 3)
# i, j, k = a1
# print(i, j ,k)
# ValueError: not enough values to unpack (expected 6, got 4)
# i, j, k, l, n, m = a1
# print(i, j, k, l, n, m)

# 星号表达式 ----解决变量个数少于元素个数的方法
# 星号表达式可以让一个变量接收多个值，但是会使该变量变成一个列表
a1 = 1, 10, 100, 1000
i, j, *k = a1
print(i, j, k)

i, *j, k = a1

print(i, j, k)

*i, j, k = a1
print(i, j, k)

*i, j = a1
print(i, j)

i, j, k, *l = a1
print(i, j, k, l)

i, j, k, l, *m = a1
print(i, j, k, l, m)

# 解包操作
a, b, *c = range(1, 10)
print(a, b, c)
a, b, c = [1, 10, 100]
print(a, b, c)
a, *b, c = 'hello'
print(a, b, c)


# 可变参数--将多个参数打包成了一个元组
def add(*args):
    print(type(args), args)
    total = 0
    for val in args:
        total += val
    return total


add(1, 10, 20)
print(add(1, 10, 20))
add(1, 2, 3, 4, 5)

# 交换两个变量的值
a, b = b, a
# 交换三个变量的值
a, b, c = c, b, a
