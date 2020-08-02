"""
定义一个天山童姥类 ，类名为TongLao，属性有血量，武力值（通过传入的参数得到）。
TongLao类里面有2个方法，
1. see_people方法，需要传入一个name参数，如果传入”WYZ”（无崖子），则打印，“师弟！！！！”，如果传入“李秋水”，打印“呸，贱人”，如果传入“丁春秋”，打印“叛徒！我杀了你”
2. fight_zms方法（天山折梅手），调用天山折梅手方法会将自己的武力值提升10倍，血量缩减2倍。需要传入敌人的hp，power，进行一回合制对打，打完之后，比较双方血量。血多的一方获胜。
定义一个XuZhu类，继承于童姥。虚竹宅心仁厚不想打架。所以虚竹只有一个read（念经）的方法。每次调用都会打印“罪过罪过”
加入模块化改造"""


# 定义一个天山童姥类
class TongLao:
    # 定义童姥的属性,血量和武力值
    def __init__(self, tl_hp, tl_power):
        self.tl_hp = tl_hp
        self.tl_power = tl_power

    # 定义童姥的方法一，喊人
    def see_people(self, name):
        # 喊不同的名字，有不同的回答
        if name == "WYZ":
            print("师弟!!!!")
        elif name == "李秋水":
            print("呸，贱人")
        elif name == "丁春秋":
            print("叛徒！我杀了你")

    # 定义童姥的方法二，天山折梅手，并传入敌人的血量和武力值
    def fight_zms(self, en_hp, en_power):
        # 调用该方法，使得武力值增加10倍，血量减半
        self.tl_power = self.tl_power*10
        self.tl_hp = self.tl_hp/2
        # 打印查看调用方法之后童姥的血量和武力值
        print(self.tl_hp)
        print(self.tl_power)
        self.en_hp = en_hp
        self.en_power = en_power
        # 一轮对打之后童姥的剩余血量值
        self.tl_hp = self.tl_hp - self.en_power
        # 一轮对打之后敌人的剩余血量值
        self.en_hp = self.en_hp - self.tl_power

        # 加入判断，谁的剩余血量多
        if self.tl_hp > self.en_hp:
            print("童姥的血量为",self.tl_hp)
            print("敌人的血量为",self.en_hp)
            print("天山童姥赢啦，真厉害！")

        elif self.tl_hp < self.en_hp:
            print("童姥的血量为", self.tl_hp)
            print("敌人的血量为", self.en_hp)
            print("竟然是敌人赢了")

        else:
            print("打平手")

# 将类实例化
tl = TongLao(1000,200)
# 调用喊人方法
tl.see_people("WYZ")
# 调用天山折梅手方法
tl.fight_zms(1000,300)





