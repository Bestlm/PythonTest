"""
算数运算符
Version: 0.1
Author: Besltm
"""
print(123 + 321)  # 加法运算
print(123 - 321)  # 减法运算
print(123 * 321)  # 乘法运算
print(123 / 321)  # 除法运算
print(123 % 321)  # 求模运算
print(123 // 321)  # 整除运算
print(123 ** 321)  # 求幂运算
print('================')
"""
赋值运算符和复合赋值运算符
"""
a = 10
b = 3
a += b  # 相当于：a=a+b
a *= a + 2  # 相当于：a=a*(a+2)
print(a)
print('================')
"""
比较运算符和逻辑运算符
"""
flag0 = 1 == 1
flag1 = 3 > 2
flag2 = 2 < 1
flag3 = flag1 and flag2  # and:而且 有一个False就是False，两个为True才为True
flag4 = flag1 or flag2  # or:或者 有一个为True就是True
flag5 = not (1 != 2)
print('flag0', flag0)
print('flag1', flag1)
print('flag2', flag2)
print('flag3', flag3)
print('flag4', flag4)
print('flag5', flag5)
print('=================')
"""
运算符使用
"""
# 将华氏温度转为摄氏温度
# %.1f是占位符，表示稍后会有一个float类型的变量值替换
f = float(input('请输入华氏温度：'))
c = (f - 32) / 1.8
#两种输出方式
print('%.1f华氏度=%1.f摄氏度' % (f, c))
print(f'{f:.1f}华氏度={c:.1f}摄氏度')
print('=================')
# %d表示稍后会有一个int类型的变量值替换
f1 = int(input('请输入一个整数f1: '))
c1 = f1 - 10
print('%d是输入的数字,减10之后的值是%d' % (f1, c1))
print('=================')
# %s表示稍后会有一个字符串类型的变量值替换
f2 = str(input('请输入狗狗的名字：'))
c2 = '屎'
print('%s是狗的名字，喜欢吃%s' % (f2, c2))
