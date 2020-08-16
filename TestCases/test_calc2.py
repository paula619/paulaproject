
# 定义一个测试类
class TestCalc():

    #定义加法参数和测试方法
    def test_add(self, get_adddata, get_calc, startCase):
        try:
            result = get_calc.add(get_adddata[0], get_adddata[1])
        except TypeError:
            print('输入的值格式有误')
        else:
            if isinstance(result, float):
                result = round(result, 2)
                assert get_adddata[2] == result
            else:
                assert get_adddata[2] == result

    #定义除法参数和测试方法
    def test_div(self, get_divdata, get_calc, startCase):
        try:
            result = get_calc.div(get_divdata[0], get_divdata[1])
        except TypeError:
            print('输入的值格式有误')
        except ZeroDivisionError:
            print('被除数不能为零')
        else:
            if isinstance(result, float):
                result = round(result, 2)
                assert get_divdata[2] == result
            else:
                assert get_divdata[2] == result

    #定义减法参数和测试方法
    def test_sub(self, get_subdata, get_calc, startCase):
        try:
            result = get_calc.sub(get_subdata[0], get_subdata[1])
        except TypeError:
            print('输入的值格式有误')
        else:
            if isinstance(result, float):
                result = round(result, 2)
                assert get_subdata[2] == result
            else:
                assert get_subdata[2] == result

    #定义乘法参数和测试方法
    def test_mul(self, get_muldata, get_calc, startCase):
        try:
            result = get_calc.mul(get_muldata[0], get_muldata[1])
        except TypeError:
            print('输入的值格式有误')
        else:
            if isinstance(result, float):
                result = round(result, 2)
                assert get_muldata[2] == result
            else:
                assert get_muldata[2] == result