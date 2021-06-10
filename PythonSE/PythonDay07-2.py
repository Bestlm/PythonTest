"""
水仙花数
它是一个3位数，该数字每个位上数字的立方之和正好等于它本身，例如：13 + 53 + 33 = 153。
"""
# 打印1000以内所有的水仙花数
for num in range(100, 1000):
    low = num % 10
    mid = num // 10 % 10
    high = num // 100
    if num == low ** 3 + mid ** 3 + high ** 3:
        print(num)
