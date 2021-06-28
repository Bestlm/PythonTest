"""
字符串应用
"""

s1 = 'hello world'
s2 = '你好世界'
print(s1, s2)
# 三个引号可以折行
s3 = '''
hello,
world
'''
# print函数中的end=''表示输出后不换行，即将默认的结束符\n（换行符）更换为''（空字符)
print(s3, end='')

"""
转义字符和原始字符串
\（反斜杠）标识转义，意思是\后面的字符不再是他原来的意思，如\n标识换行
\t标识制表符
如果要输出有反斜杠的特殊字符，需要加引号
"""

s4 = '\'hello,world!\''
s5 = '\\hello,world!\\'
print(s4, s5)

"""
原始字符串
r,R开头，意思是字符串中的每个字符都是她本来的含义不会转义
如 r'\n'的意思就是\和n，不是换行
"""
s6 = '\time up \now'
s7 = r'\time up \now'
print(s6, s7)

"""
字符串运算
+拼接
*重复
in包含
not in不包含
[]，[:]取值
"""
s8 = 'hello' + 'World'
print(s8)
s9 = 'hello,world' * 2
print(s9)
# 比较运算
s10 = 'hello,world'
print(s10 == 'Hello')
print(s10 != 'Hello')

"""
字符串内存地址位置比较
"""
s11 = 'Hello'
s12 = 'Hello'
s13 = s12
# 比较字符串的内容
print(s11 == s12, s12 == s13)
# 比较内存地址
print(s11 is s12, s12 is s13)

"""
成员运算
in not in
"""
s14 = 'hello,world'
print('wo' in s14)
print('xixi' in s14)
s15 = 'sorry'
print(s15 in s14)
print(s15 not in s14)

"""
获取字符串长度
len
"""
s16 = 'hello,world'
print(len(s16))
print(len('sorry'))

"""
索引和切片
正向索引0,n-1
负向索引-1,-n
"""
s16 = '123456'
N = len(s16)
# 获取第一个字符
print(s16[0], s16[-N])
# 获取最后一个字符
print(s16[N - 1], s16[-1])
# 获取索引为2或4的字符
print(s16[2], s16[4])

"""
切片
字符串中取出多个字符需要切片，运算符[i:j:k]
i是开始索引，索引对应的字符可以取到
j是结束索引，索引对应的字符不能取到
k是步长，默认为1，表示从前向后获取相邻字符的连续切片
例：
字符串长度为N，当k>0时，表示正向切片（从前向后），如果没有给出i和j的值，则i默认为0，j默认为N
当K<0时表示负向切片（从后往前），如果没有给出i和j的值，则i默认为-1，j默认为-N-1
"""
s17 = 'abc123456'
# i = 2 , j = 5, k =1的正向切片
print(s17[2:5])
# i=-7,j=-4,k=1的正向切片
print(s17[-7:-4])
