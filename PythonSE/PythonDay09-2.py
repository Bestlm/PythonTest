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
