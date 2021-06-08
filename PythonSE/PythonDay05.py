"""
用户身份验证
Version: 0.1
Author: Bestlm
"""
username = input('请输入用户名：')
password = input('请输入密码: ')
# # 用户名为admin且密码为12345则验证成功否则失败
if username == 'admin' and password == '12345':
    print('登录成功')
else:
    print('登录失败')
"""
分段函数求值
"""
a = float(input('a='))
if a > 1:
    b = a + 10
elif a > 2:
    b = a * 2
else:
    b = a * 5
print(f'f({a})={b}')
print('==========')

a1 = int(input("a1="))
if a1 > 1:
    b1 = a1 * 3 - 1
elif a1 >= -1:
    b1 = a1 + 2
else:
    b1 = a1 * 5 + 3
print('a1的值是%d，运算之后b1的值为: %d' % (a1, b1))
print('==========')
"""
嵌套分段函数求值
"""
a2 = float(input('a2='))
if a2 > 1:
    b2 = 3 * a2 + 1
else:
    if a2 == 0:
        b2 = a2 + 1
    else:
        b2 = 5 * a2 + 1
print(f'f({a2})={b2}')
print('a2的值是%.1f,运算后的结果b2的值为：%.1f' % (a2, b2))
print('==========')
"""
英制单位和公制单位互换
"""
value = float(input('请输入长度:'))
unit = input('请输入单位:')
if unit == 'in' or unit == '英寸':
    print('%2.f英寸=%f厘米' % (value, value * 2.54))
elif unit == 'cm' or unit == '厘米':
    print('%2.f厘米=%f英寸' % (value, value / 2.54))
else:
    print('请输入有效的单位')
"""
成绩转化为评级
"""
score = float(input('请输入成绩:'))
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = "D"
else:
    grade = 'E'
print('对应的评级是:', grade)
