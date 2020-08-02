# 定义一个类
class Dog:
    # 定义属性: 狗的颜色，一条尾巴，两只耳朵
    color = "white"
    tail = 1
    ear = 2

    # 定义方法：狗在跑，狗在睡觉
    def run(self):
        print("狗在跑")

    def sleep(self):
        print("狗在睡觉")


# 定义一个类
class Car:
    # 定义属性: 车的颜色，四个车轮
    color = "Red"
    wheel = 4

    # 定义方法：车会开，车会响喇叭
    def drive(self):
        print("车在驾驶")

    def ring(self):
        print("车喇叭在响")


# 定义一个类
class Phone:
    # 定义属性: 手机的颜色，手机的品牌
    color = "Black"
    brand = "Apple"

    # 定义方法：手机打电话，手机放音乐
    def call(self):
        print("手机在打电话")

    def play(self):
        print("手机在播放音乐")


# 定义一个类
class YiYangQianXi:
    # 定义属性: 身高，性别
    height = 178
    gender = "male"

    # 定义方法：会跳舞，会唱歌
    def dance(self):
        print("易烊千玺会跳舞")

    def sing(self):
        print("易烊千玺会唱歌")


# 定义一个类
class Computer:
    # 定义属性: 品牌，价格
    price = 4600
    brand = "华硕"

    # 定义方法：敲代码，看视频
    def coding(self):
        print("电脑用来敲代码")

    def watch(self):
        print("电脑用来看视频")
