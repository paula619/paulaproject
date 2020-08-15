import pytest
import yaml
from PythonCode.calc import Calculator

# 打开yaml文件
with open('./datas/calcdata.yml') as f:
    data = yaml.safe_load(f)
    # 取出add的测试数据
    adddatas = data['add']['add_datas']
    print(adddatas)
    # 取出add data对应的id名称
    adddata_id = data['add']['add_dataid']
    print(adddata_id)
    # 取出div的测试数据
    divdatas = data['div']['div_datas']
    print(divdatas)
    # 取出div data对应的id名称
    divdata_id = data['div']['div_dataid']
    print(divdata_id)


# 定义一个测试类
class TestCalc:

    # 定义类级别的setup,调用类内的测试用例方法时需做的准备工作
    def setup_class(self):
        print("进行测试用例执行的准备工作")
        # 实例化计算器的Calculator类，用于测试用例中需调用类中的方法
        self.calc = Calculator()

    # 调用每条测试用例前打印“开始计算”
    def setup(self):
        print("开始计算")

    # 调用每条测试用例后打印“结束计算”
    def teardown(self):
        print('计算结束')

    #定义加法参数和测试方法
    @pytest.mark.parametrize('a,b,expect', adddatas, ids=adddata_id)
    def test_add(self, a, b, expect):
        try:
            result = self.calc.add(a, b)
        except TypeError:
            print('输入的值格式有误')
        else:
            if isinstance(result, float):
                result = round(result, 2)
                assert expect == result
            else:
                assert expect == result

    #定义除法参数和测试方法
    @pytest.mark.parametrize('a,b,expect', divdatas, ids=divdata_id)
    def test_div(self, a, b, expect):
        try:
            result = self.calc.div(a, b)
        except TypeError:
            print('输入的值格式有误')
        except ZeroDivisionError:
            print('被除数不能为零')
        else:
            if isinstance(result, float):
                result = round(result, 2)
                assert expect == result
            else:
                assert expect == result



