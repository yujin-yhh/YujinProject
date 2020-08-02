# 定义一个车类
class Car:
    # 创建构造方法
    def __init__(self, km):
        # 定义属性颜色color,默认为白色
        self.color = 'white'
        # 定义属性长度默认为0米
        self.length = 0
        # 接收传入参数km,表示已经行驶的千米数
        self.km = km
        # 定义参数upkeeps表示已经保养的次数
        self.upkeeps = 0

    # 创建一个方法upkeep,传入参数km表示已经行驶的千米数，
    def upkeep(self):
        # while 循环，每行驶5000km保养一次，upkeeps记录已经保养的次数
        while self.km - 5000 >= 0:
            self.upkeeps += 1
            self.km -= 5000

        # 结束循环，返回保养的次数upkeeps
        return self.upkeeps


# 定义一个Bus类，继承于Car类
class Bus(Car):
    # 定义一个方法scrap报废，传入参数max_km
    def scrap(self, max_km):
        if max_km >= self.km:
            print("已经行驶到最大里程数，车辆该报废了")
        else:
            print(f"车辆还未行驶到极限值，再行驶{max_km - self.km}车辆就该报废了，请注意保养")


# 实例化一个对象smart,传入参数已经行驶到千米数7000
smart = Car(7000)
# 设置参数upkeeps 接收方法upkeep返回到保养次数
print(smart.upkeep())

# 实例化一个对象bus，传入参数已经行驶到千米数120000
bus = Bus(120000)
# 调用upkeep方法，打印对象bus的保养次数
print(bus.upkeep())
# 调用scrap方法，传入参数最大行驶的历程数是10000，打印车辆是否该报废信息，
bus.scrap(10000)




