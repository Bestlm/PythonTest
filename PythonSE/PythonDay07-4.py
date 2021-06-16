"""
玩家第一次摇骰子如果摇出了7点或11点，玩家胜；
玩家第一次如果摇出2点、3点或12点，庄家胜；
玩家如果摇出其他点数则玩家继续摇骰子，如果玩家摇出了7点，庄家胜；
如果玩家摇出了第一次摇的点数，玩家胜；
其他点数玩家继续摇骰子，直到分出胜负。
"""
from random import randint

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
    # 均匀随机数
    first = randint(1, 6) + randint(1, 6)
    print(f'玩家摇出来了{first}')
    if first == 7 or first == 11:
        print('玩家胜')
        money += bet
    elif first == 2 or first == 3 or first == 12:
        print('庄家胜')
        money -= bet
    else:
        go_on = True
    while go_on:
        go_on = False
        current = randint(1, 6) + randint(1, 6)
        print(f'玩家摇出了{current}点')
        if current == 7:
            print('庄家胜')
            money -= bet
        elif current == first:
            print('玩家胜')
            money += bet
        else:
            go_on = True
print('你没钱了')
