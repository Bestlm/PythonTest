"""
列表
将一颗色字投掷6000次，统计每个点数出现的次数
"""
import random

f1 = 0
f2 = 0
f3 = 0
f4 = 0
f5 = 0
f6 = 0
for _ in range(6000):
    face = random.randint(1, 6)
    if face == 1:
        f1 += 1
    elif face == 2:
        f2 += 1
    elif face == 3:
        f3 += 1
    elif face == 4:
        f4 += 1
    elif face == 5:
        f5 += 1
    elif face == 6:
        f6 += 1
print(f'1点出现了{f1}次')
print(f'2点出现了{f2}次')
print(f'3点出现了{f3}次')
print(f'4点出现了{f4}次')
print(f'5点出现了{f5}次')
print(f'6点出现了{f6}次')

"""
定义和使用列表
"""
items1 = [12, 35, 99, 68, 55, 87]
items2 = ['Python', 'Java', 'Go', 'Scala']
items3 = list(range(1, 10))
items4 = list('hello')
print(items3)
print(items4)

"""
列表的拼接
"""
items5 = [45, 8, 29, 30]
items6 = items1 + items5
print(items6)

"""
列表的重复
"""
items7 = ['hello'] * 3
print(items7)

"""
列表的成员运算
"""
# 100没在items5中
# hello在items4中
print(100 in items5)
print('hello' in items4)

"""
获取列表长度
"""
size = len(items4)
print(size)

"""
列表的索引
"""
print(items5[1])
print(items5[-1])

"""
列表的切片
"""
print(items5[1::1])
print(items5[:1:1])
print(items5[:2:1])
print(items5[-2::1])
print(items5[::-2])

"""
列表的比较运算
"""
items8 = [1, 2, 3, 4]
items9 = list(range(1, 5))
# 两个列表比较相当性比的是对应索引位置上的元素是否相等
print(items8 == items9)
items10 = [3, 2, 1]
# 两个列表比较大小比的是对应索引位置上元素的大小
print(items8 <= items10)

"""
列表元素的遍历
"""
# items2 = ['Python', 'Java', 'Go', 'Scala']
for index in range(len(items2)):
    print(items2[index])

for item in items2:
    print(item)

"""
掷6000次骰子重构
"""
# count中的六个元素表示各个点数出现的次数，默认为0
Count = [0] * 6
for _ in range(6000):
    faces = random.randint(1, 6)
    Count[faces - 1] += 1
for faces in range(1, 7):
    print(f'{faces}出现了{Count[faces - 1]}次')

"""
添加和删除元素
"""
# items2 = ['Python', 'Java', 'Go', 'Scala']
# 使用append方法在列表尾部添加元素
items2.append('Swift')
print(items2)
# 使用insert方法在列表指定索引位置插入元素
items2.insert(2, 'SQL')
print(items2)
# 删除指定的元素
items2.remove('Java')
print(items2)
# 删除指定索引位置的元素
items2.pop(0)
items2.pop(len(items2) - 1)
print(items2)
# del删除
del items2[1]
print(items2)
# 清空列表中的元素
items2.clear()
print(items2)

"""
元素位置和次数
"""
items11 = ['Python', 'Java', 'Java', 'Go', 'Kotlin', 'Python']

# 查找元素的索引位置
print(items11.index('Python'))
print(items11.index('Python', 2))
# 注：虽然有Java，但是是从索引为3的位置开始查询的
# 报错：ValueError: 'Java' is not in list
# print(items11.index('Java', 3))

# 查找元素出现的次数
print(items11.count('Python'))
print(items11.count('Go'))

"""
元素排序和反转
"""
items12 = ['Python', 'Java', 'Go', 'Kotlin', 'SQL']

# 排序
items12.sort()
print(items12)

# 反转
items12.reverse()
print(items12)

"""
列表生成式
"""
# 创建一个由1到9的数字构成的列表
items13 = []
for x in range(1, 10):
    items13.append(x)
print(items13)

# 创建一个由'hello world'中除空格和元音字母外的字符构成的列表
items14 = []
for x in 'hello world':
    if x not in ' aeiou':
        items14.append(x)
print(items14)

# 创建一个由两个字符串中字符的笛卡尔积构成的列表
items15 = []
for x in 'ABC':
    for y in '12':
        items15.append(x + y)
print(items15)

# 创建一个由1-9的数字构成的列表
items16 = [x for x in range(1, 10)]
print(items16)

# 创建一个由'hello world'中除空格和元音字母外的字符构成的列表
items17 = [x for x in 'hello world' if x not in ' aeiou']
print(items17)

# 创建一个由两个字符串中字符的笛卡尔积构成的列表
items18 = [x + y for x in 'ABC' for y in '12']
print(items18)

"""
嵌套的列表
"""
scores = [[0] * 3 for _ in range(5)]
scores[0][0] = 95
print(scores)
