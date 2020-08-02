# 定义一个鱼类
class Fish:
    # 创建构造方法
    def __init__(self, breed):
        # 传入参数品种：breed
        self.breed = breed
        # 定义属性鱼鳞scale,有鱼鳞：True 没有鱼鳞：False
        self.scale = True
        # 定义属性alive，alive=True表示活的，alive=False表示死的
        self.alive = True
        #定义属性circles，表示鱼一生游泳千米数相当于绕地球的圈数
        self.circles = 0

    # 定义方法breath
    def breath(self, alive):
        # 如果alive==True,表示活着，打印：鱼还呼吸，它还活着
        if self.alive is True:
            print("鱼还呼吸，它还活着")
        # 否则表示鱼死了，打印：鱼不呼吸了，它死了！
        else:
            print("鱼不呼吸了，它死了！")

    # 定义一个游泳类swim,传入参数km表示鱼一生游泳的千米数
    def swim(self, km):
        # 使用while循环，每循环一次千米数-40096，绕地球圈数+1
        while km - 40076 >= 0:
            self.circles += 1
            km -= 40076
        # 剩余千米数不足40096km时跳出循环
        self.alive = False
        # 返回游泳的圈数circles和是否活着alive
        return self.circles, self.alive


# 实例化一个对象fish,传入的参数品种breed为clownfish
fish = Fish('clownfish')
# 调用swim 函数，传入的参数一生游泳次数2000000，获取返回元组第一个参数游泳的圈数赋值给参数circles
circles = fish.swim(2000000)[0]
# 调用swim 函数，传入的参数一生游泳次数2000000，获取返回元组第二个参数是否活着赋值给参数alive
alive = fish.swim(2000000)[1]
# 打印信息
print(f"{fish.breed}一生绕地球至少游了{circles}圈")
fish.breath(alive)
