# 定义一个除法类
class Division:
    # 创建构造函数，传入参数:除数divisor，被除数dividend
    def __init__(self):
        self.divisor = 0
        self.dividend = 1

    # 定义除法方法：
    def div(self, divisor, dividend):
        # if isinstance(self.divisor,
        # result = self.divisor/self.dividend
        # 返回结果等于除数/被除数
        result = divisor / dividend
        return result

