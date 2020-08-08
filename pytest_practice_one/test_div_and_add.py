# 导入模块
import pytest
import yaml

from YujinProject.pytest_practice_one.addition import Addision
from YujinProject.pytest_practice_one.division import Division
# 打开yaml文件
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

# 定义一个测试除法类
class TestDiv:
    # 定义类级别的setup方法，将Division实例化
    def setup_class(self):
        self.mydiv = Division()

    # setup方法，每个测试用例方法执行前打印"开始计算"
    def setup(self):
        print("开始计算")

    # teardown方法，每个测试用例方法执行前打印"开始计算"
    def teardown(self):
        print("结束计算")

    # 参数化，读取yaml文件中对测试数据
    @pytest.mark.parametrize('a, b, expect', divdata, ids=myids)
    # 定义测试用例
    def test_div(self, a, b, expect):
        # 如果除数或被除数为字符串，或被除数为0，实际结果为：ERROR
        if isinstance(a, str) or isinstance(b, str) or b == 0:
            result = 'ERROR'
        # 如果除数或被除数为非字符串，且被除数为非0，实际结果为：调用除法方法，且保留两位小数
        else:
            result = round(self.mydiv.div(a, b), 2)
        # 添加断言
        assert result == expect


# 定义加法测试类
class TestAdd:
    # 定义类级别的setup方法，将加法类Addision实例化
    def setup_class(self):
        self.myadd = Addision()

    # setup方法，每个测试用例方法执行前打印"开始计算"
    def setup(self):
        print("开始计算")

    # teardown方法，每个测试用例方法执行前打印"开始计算"
    def teardown(self):
        print("结束计算")

    # 参数化，读取文件中的加法的测试数据
    @pytest.mark.parametrize('a, b, expect', adddate, ids=myaddids)
    # 定义测试加法方法
    def test_add(self, a, b, expect):
        # 如果两个加数有字符串，则将结果置为ERROR
        if isinstance(a, str) or isinstance(b, str):
            result = 'ERROR'
        #  否则，调用加法方法，并将结果保留两位小数
        else:
            result = self.myadd.addfunc(a, b)
        #  添加断言
        assert result == expect


