# 定义一个类:猪
class Pig:
    # 创建构造方法，
    def __init__(self, job):
        # 定义属性，国家country，默认值为UK；语言language，默认值为English，
        # 工作job,可以通过参数传入，定义性别gender默认为男，年龄age默认为0岁
        self.country = 'UK'
        self.language = 'English'
        self.job = job
        self.gender = 'F'
        self.age = 0
        self.name = 'default'

    # 定义一个方法，跳泥坑
    def jumpin_pud(self):
        # 调用跳泥坑方法时打印：下雨啦，快来跳泥坑！！！
        print("下雨啦，快来跳泥坑！！！")

    # 定义一个方法，打印个猪信息
    def printinfo(self):
        # 判断：如果是输入的工作是tester，抛出异常：哎呀，技术过硬吗？？？来Hogwarts深造吧！！！
        if self.job == 'tester':
            raise ValueError("哎呀，技术过硬吗？？？来Hogwarts深造吧！！！")
        # 如果输入的工作不是tester，打印个猪信息
        else:
            print(f"Hello everyone! My name is {self.name}, I come from {self.country}, I speak {self.language},\n"
                f"I am {self.age} years old, I am a {self.job}.")


# 定义一个类BabyPig，继承于Pig类
class BabyPig(Pig):
    # 创建构造方法
    def __init__(self, job, classmate):
        # 继承父类的构造方法
        super().__init__(job)
        # 定义参数同学classmate，可以通过参数传入
        self.classmate = classmate

    def paint(self, paintings):
        print(f"{self.classmate},一起来画一个{paintings}吧")




