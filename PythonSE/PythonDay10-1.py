"""
利用random随机抽样函数从字符串中取出指定数量的字符
利用字符串的join方法将选中的字符拼接
"""
import random
import string

ALL_CHARS = string.digits + string.ascii_letters

'''
random模块的sample和choices函数都可以实现随机抽样
sample实现无放回抽样，表示抽样取出的字符是不重复的
choices实现有放回抽样，表示可能会重复选中某些字符
参数：第一个参数表示抽样的总体，参数k表示抽样的数量
'''


def generate_code(code_len=4):
    """
    生成指定长度的验证码
    :param code_len: 验证码的长度（默认4个字符）
    :return: 由大小写英文字母和数字构成的随机验证码字符串
    """
    return ''.join(random.choices(ALL_CHARS, k=code_len))


print(generate_code())
