"""
斐波那契数列
1,1,2,3,5,8,13,21,34,55
"""
# 打印斐波那契数列的前20个
a = 1
b = 1
# 结尾加换行end=' '意思是末尾不换行，加空格
print(a, b, end=' ')
# 递推公示
for _ in range(18):
    a, b = b, a + b
    print(b, end=' ')
print()
"""
打印素数
素数指的是只能被1和自身整除的正整数（不包括1）
"""
for num in range(2, 100):
    is_prime = True
    for factor in range(2, num):
        if num % factor == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=' ')
