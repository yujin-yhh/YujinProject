# 定义一个计算器类
class Calculator:
    # 创造重构方法，定义两个参数，第一个数fir和第二个数sec,默认两个参数均为1
    def __init__(self):
        fir = 1
        sec = 1

    # 定义除法方法：
    def div(self, fir, sec):
        # 如果除数或被除数含字符，或被除数为0，打印ERROR
        if isinstance(fir, str) or isinstance(sec, str) or sec == 0:
            return "ERROR"
        # 返回结果等于除数/被除数
        else:
            result = round(fir / sec, 2)
        # 返回结果
        return result

    # 定义加法方法：
    def add(self, fir, sec):
        if isinstance(fir, str) or isinstance(sec, str):
            result = 'ERROR'
        else:
            # 定义加法运算fir + sec
            result = round(fir + sec, 2)
        return result

    # 定义乘法方法，传入两个乘数
    def mul(self, fir, sec):
        # 如果乘数包含字符串，则打印ERROR
        if isinstance(fir, str) or isinstance(sec, str):
            result = 'ERROR'
        else:
            # 如果返回两个乘数对积
            result = round(fir * sec, 2)
        return result

    # 定义减法方法，传入减数fir,被减数sec
    def sub(self, fir, sec):
        # 如果减数sub1,被减数sub2包含字符，报错ERROR
        if isinstance(fir, str) or isinstance(sec, str):
            result = 'ERROR'
        # 否则计算结果result=减数fir-被减数sec
        else:
            result = round(fir - sec, 2)
        # 返回计算结果
        return result