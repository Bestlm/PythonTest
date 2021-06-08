"""
占位符的使用
Version: 0.1
Author: Bestlm
"""
# 输入半径计算圆的周长和面积
import math

# radius = float(input('请输入圆的半径：'))
# perimeter = 2 * math.pi * radius
# area = math.pi * radius * radius
# print('周长: %.2f' % perimeter)
# print('面积：%.2f' % radius)

# 判断是否是闰年
# 闰年的标准是能被400整除,或者能被4整除但是不能被100整除
year = int(input('请输入要判断的年份：'))
is_leap = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
print(is_leap)
