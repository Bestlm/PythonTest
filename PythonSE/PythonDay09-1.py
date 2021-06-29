"""
大小写切换
capitalize首字母大写
title 单词首字母大写
upper 全部大写
lower 全部小写
"""
s1 = 'hello,world'
# 首字母大写
print(s1.capitalize())
# 单词首字母大写
print(s1.title())
# 全部大写
print(s1.upper())
# 全部小写
print(s1.lower())

"""
查找字符串
find  index
"""
s2 = 'hello,world'
# find方法从字符串中查找另一个字符串所在的位置
# 找到了返回字符串汇总另一个字符串首字符的索引
print(s2.find('or'))
print(s2.find('shit'))
# index方法
# 找到了返回字符串中另一个字符串首字符的索引
print(s2.index('or'))
# 找不到引发异常
#print(s2.index('shit'))

"""
find 和 index 的参数设置
逆向查找 rfind rindex
"""
s3 = 'hello great world'
# 从前向后查找o的位置
print(s3.find('o'))
# 从索引为5的位置开始查找o的位置
print(s3.find('o', 5))
# 从后往前查找o出现的位置
print(s3.rfind('o'))