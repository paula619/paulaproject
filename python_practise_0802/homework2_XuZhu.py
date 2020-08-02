# 模块化，导入其他模块中的类
from python_practise_0802.homework2_TongLao import TongLao

# 定义一个XuZhu类，继承自天山童姥
class XuZhu(TongLao):
    def read(self):
        print("罪过罪过")

# 将类实例化
xz = XuZhu(2000,200)
# 调用read方法
xz.read()