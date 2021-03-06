from typing import List

import pytest
import yaml
from YujinProject.pytest_practice_two.calculator import Calculator

# 在文件中获取测试数据
with open("datas/data.yml") as f:
    # 获取yaml文件中的除法数据
    alldates = yaml.safe_load(f)

    # 获取除法对所有数据
    dates = alldates["divdatas"]
    # 获取除法数据中的除数、被除数、期望值列表
    divdata = dates["divdata"]
    # 获取除法数据中的ids
    myids = dates["divids"]

    # 获得加法对所有数据
    adddatas = alldates["adddatas"]
    # 获取加法对两个加数和期望值列表
    adddate = adddatas["adddata"]
    # 获取加法数据中对ids
    myaddids = adddatas["addids"]

    # 获取减法的所有数据
    subdatas = alldates["subdatas"]
    # 获取减法的测试数据
    subdata = subdatas["subdata"]
    # 获取减法的ids
    subids = subdatas["subids"]

    # 获取乘法的所有数据
    muldatas = alldates["muldatas"]
    # 获取乘法的测试数据
    muldata = muldatas["muldata"]
    # 获取乘法的ids
    mulids = muldatas["mulids"]


# 在测试用例执行前打印开始计算，执行完测试用例后打印结束计算
@pytest.fixture(scope="function")
def comm_func():
    print("开始计算")
    yield
    print("结束计算")

# 获取计算器实例
@pytest.fixture(scope='class')
def getcal():
    cal = Calculator()
    return cal

# 获取并返回减法数据
@pytest.fixture(params=subdata, ids=subids)
def getsubdata(request):
    subdata = request.param
    return subdata

#获取并返回加法数据
@pytest.fixture(params=adddate, ids=myaddids)
def getadddata(request):
    adddate = request.param
    return adddate

# 获取并返沪乘法数据
@pytest.fixture(params=muldata, ids=mulids)
def getmuldata(request):
    muldata = request.param
    return muldata

#获取并返回除法数据
@pytest.fixture(params=divdata, ids=myids, scope='class')
def getdivdata(request):
    divdata = request.param
    return divdata


def pytest_collection_modifyitems(
    session: "Session", config: "Config", items: List["Item"]
) -> None:
    """ called after collection has been performed, may filter or re-order
    the items in-place.

    :param _pytest.main.Session session: the pytest session object
    :param _pytest.config.Config config: pytest config object
    :param List[_pytest.nodes.Item] items: list of item objects
    """
    print(items)
    # 修改编码
    for item in items:
        item.name = item.name.encode("utf-8").decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
        # 添加标签
        if 'add' in item.nodeid:
            item.add_marker(pytest.mark.add)
        elif 'div' in item.nodeid:
            item.add_marker(pytest.mark.div)
        elif 'mul' in item.nodeid:
            item.add_marker(pytest.mark.mul)
        elif 'sub' in item.nodeid:
            item.add_marker(pytest.mark.sub)


def pytest_addoption(parser):
    mygroup = parser.getgroup("hogwarts")  # group 将下面所有的 option都展示在这个group下。
    mygroup.addoption("--env",  # 注册一个命令行选项
                      default='test',  # 默认值
                      dest='sit',  # 存储的变量
                      choices=['sit', 'dev', 'st'],
                      help='set your run env'  # 参数说明
                      )


@pytest.fixture(scope='function')
def cmdoption(request):
         return request.config.getoption("--env", default='test')
