"""
函数和模块
x1+x2+x3+x4=8
8个苹果分成4堆，有几种方式
8个苹果的7个缝隙选3个插入隔板，有几种方法  C(7,3)=35
阶乘
"""


# m = int(input('m = '))
# n = int(input('n = '))
# # 计算m的阶乘
# fm = 1
# for num in range(1, m + 1):
#     fm *= num
# # 计算n的阶乘
# fn = 1
# for num in range(1, n + 1):
#     fn *= num
# # 计算m-n的阶乘
# fm_n = 1
# for num in range(1, m - n + 1):
#     fm_n *= num
# # 计算c(m,n)的值
# print(fm // fn // fm_n)


# 复用代码 封装函数
# 函数名 参数 返回值
def function(num):
    """求阶乘"""
    result = 1
    for n in range(1, num + 1):
        result *= n
    # 返回值
    return result


m = int(input('m = '))
n = int(input('n = '))
# 调用函数function，传递参数m,n
print(function(m) // function(n) // function(m - n))
