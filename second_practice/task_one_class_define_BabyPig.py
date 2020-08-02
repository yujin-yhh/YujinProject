# 导入模块
from YujinProject.second_practice.task_one_class_define_Pig import Pig

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