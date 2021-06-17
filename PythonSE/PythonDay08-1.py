"""
玩家第一次摇骰子如果摇出了7点或11点，玩家胜；
玩家第一次如果摇出2点、3点或12点，庄家胜；
玩家如果摇出其他点数则玩家继续摇骰子，如果玩家摇出了7点，庄家胜；
如果玩家摇出了第一次摇的点数，玩家胜；
其他点数玩家继续摇骰子，直到分出胜负。
"""
# 骰子游戏重构
from random import randint


# 封装摇骰子方法
def roll(n=2):
    """摇骰子返回的总点数"""
    total = 0
    for _ in range(n):
        total += randint(1, 6)
    return total


# 玩家本金
money = 1000
while money > 0:
    print(f'你的总资产为：{money}元')
    go_on = False
    # 下注的金额限制
    while True:
        bet = int(input('请下注：'))
        if 0 < bet <= money:
            break

    # 第一次摇骰子
    first = roll(2)
    if first == 7 or first == 11:
        print(f'玩家第一次摇出来的点数是：{first},玩家胜利')
        money += bet
    elif first == 2 or first == 3 or first == 12:
        print(f'玩家摇出的点数是：{first},庄家胜利')
        money -= bet
    else:
        go_on = True
    # 第二次摇骰子
    while go_on:
        go_on = False
        second = roll(2)
        if second == 7:
            print(f'玩家摇出的点数是: {second},庄家胜')
            money -= bet
        elif second == first:
            print(f'玩家摇出的点数是: {second},玩家胜')
            money += bet
        else:
            go_on = True
print('你没钱了')
