"""
跑马灯
把当前字符串的第一个字符放到要输出的内容的最后面
把从第二个字符开始后面的内容放到要输出的内容的最前面
"""
import os
import time

content = '跑马灯测试'
while True:
    # Windows清楚屏幕上的输出
    # os.system('cls')
    os.system('cls')
    print(content)
    time.sleep(0.2)
    content = content[1:]+content[0]