"""
一个回合制游戏，每个角色都有hp 和power，
hp代表血量，power代表攻击力，hp的初始值为1000，
power的初始值为200。打斗多个回合
定义一个fight方法：
my_hp = hp - enemy_power
enemy_final_hp = enemy_hp - my_power
谁的hp先为0，那么谁就输了
"""

# 定义一个fight函数
def fight():
    #定义四个变量，分别为我的血量，攻击力和你的血量，攻击力
    my_hp = 1000
    my_power = 200
    your_hp = 1000
    your_power = 180

#定义一个while循环，对打多轮，谁的血量小于等于0，就输了
    while True:
        #定义我的剩余血量
        my_hp = my_hp - your_power
        #定义你的剩余血量
        your_hp = your_hp - my_power
        #定义一个if判断，我的血量小于等于0
        if my_hp <= 0:
            print("我的剩余血量为", my_hp)
            print("你的剩余血量为", your_hp)
            print("我输了")
            break
        #你的血量小于等于0
        elif your_hp <=0:
            print("我的剩余血量为", my_hp)
            print("你的剩余血量为", your_hp)
            print("你输了")
            break

#调用fight函数
fight()



