from PythonCode.calc import Calculator
import os
import pytest
import yaml


yamlfilepath = os.path.dirname(__file__) + './datas/calcdata.yml'
# 打开yaml文件
with open(yamlfilepath) as f:
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
    # 取出sub的测试数据
    subdatas = data['sub']['sub_datas']
    print(subdatas)
    # 取出sub data对应的id名称
    subdata_id = data['sub']['sub_dataid']
    print(subdata_id)
    # 取出mul的测试数据
    muldatas = data['mul']['mul_datas']
    print(muldatas)
    # 取出mul data对应的id名称
    muldata_id = data['mul']['mul_dataid']
    print(muldata_id)

#定义一个scope为class的fixture方法
@pytest.fixture(scope='class')
def get_calc():
    print("进行测试用例执行的准备工作")
    # 实例化计算器的Calculator类，用于测试用例中需调用类中的方法
    calc = Calculator()
    return calc

#定义一个scope为function的fixture方法
@pytest.fixture(scope='function')
def startCase():
    # 调用每条测试用例前打印“开始计算”
    print("开始计算")
    yield
    # 调用每条测试用例后打印“结束计算”
    print('计算结束')

#用fixture方法实现传参
@pytest.fixture(params=adddatas, ids=adddata_id)
def get_adddata(request):
    adddata = request.param
    print(adddata)
    return adddata

@pytest.fixture(params=divdatas, ids=divdata_id)
def get_divdata(request):
    divdata = request.param
    print(divdata)
    return divdata

@pytest.fixture(params=subdatas, ids=subdata_id)
def get_subdata(request):
    subdata = request.param
    print(subdata)
    return subdata

@pytest.fixture(params=muldatas, ids=muldata_id)
def get_muldata(request):
    muldata = request.param
    print(muldata)
    return muldata

