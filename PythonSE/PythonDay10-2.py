"""
设计一个函数返回给定文件名的后缀名
"""
from os.path import splitext


def get_suffix(filename):
    """
    获取文件名的后缀名
    :param filename: 文件名
    :return: 文件的后缀名
    """
    # 从字符串中逆向找到.出现的位置
    pos = filename.rfind('.')
    # 通过切片操作从文件名中取出后缀名
    return filename[pos + 1:] if pos > 0 else ''


print(get_suffix('xixi.avi'))
print(get_suffix('xixi'))
print(get_suffix('haha.txt'))
print(get_suffix('error.txt.md'))
print(get_suffix('error1.txt。md'))
print(get_suffix('error2。txt.md'))
print('=================')
"""
使用os.path模块的splitext函数
这个函数会将文件名拆分成带路径的文件名和扩展名两个部分，然后返回一个二元组
二元组的第二个元素就是文件的后缀名（包含.）,去掉后缀名中的.，可以做一个字符串的切片操作
"""


def get_suffix1(filename):
    return splitext(filename)[1][1:]


print(get_suffix1('error2。txt.md'))
