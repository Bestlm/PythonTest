"""
性质判断
startswith:判断字符串是否以某个字符串开头
endswith:判断字符串是否以某个字符串结尾
"""
s1 = 'hello,world'
# startswith
print(s1.startswith('he'))
print(s1.startswith('He'))
# endswith
print(s1.endswith('d'))
print(s1.endswith('!'))

print('==================')
s2 = 'abcd123456'
# isdigit:检查字符串是否由数字构成的
print(s2.isdigit())
# isalpha:检查字符串是否以字母构成返回布尔值
print(s2.isalpha())
# isalnum:检查字符串是否以数字和字母构成
print(s2.isalnum())

print('===================')
# 格式化字符串
s3 = 'hello,world'
# center:以宽度20将字符串居中并在两侧填充*
print(s3.center(20, '*'))
# rjust以宽度20将字符串右对齐并在左侧填充空格
print(s3.rjust(20))
# ljust以宽度20将字符串左对齐并在右侧填充
print(s3.ljust(20, '~'))
print('=================')
# 格式化
a = 123
b = 321
print('%d * %d = %d' % (a, b, a * b))
# 字符串的方法完成字符串格式化
print('{0} * {1} = {2} '.format(a, b, a * b))
# 占位符格式化
d = 3.1415926
d1 = -1
d2 = 123
print('d=%f' % d)
print('{:.2f}'.format(d))
# print('d=%.2f' % d)
print('{:+.2f}'.format(d))
# print('d=%+.2f' % d)
print('{:+.2f}'.format(d1))
# print('d1=%+.2f' % d1)
print('{:.0f}'.format(d))
# print('d=%.0f' % d)
print('{:0>8d}'.format(d2))  # 左补零到8位
# print('%08d' % d2)  # 左补零到8位
# 左补x到10位
print('{:x>10d}'.format(d2))
# 右补X到10位
print('{:x<10d}'.format(d2))
# 左补空格到10位
print('{:>10d}'.format(d2))
# 右补空格到10位
print('{:<10d}'.format(d2))
d3 = 1234567892
# 逗号分割格式
print('{:,}'.format(d3))
# 百分比格式 .后面的数字表示保留几位小数
d4 = 0.123
print('{:.2%}'.format(d4))
# 科学记数法
print('{:.2e}'.format(d2))

'''
字符串修剪操作
'''
s = '         bestlm3034@gmail.com    \t\r\n'
print(s)
# strip方法获得字符串修剪左右两侧空格之后的字符串
print(s.strip())
# lstrip
print(s.lstrip())
# rstrip
print(s.rstrip())
