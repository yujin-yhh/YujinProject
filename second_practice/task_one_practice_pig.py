# 实例化一个对象dadypig，传入参数job通过提示输入
from YujinProject.second_practice.task_one_class_define_Pig import Pig

dadypig = Pig(input("请输入工作："))
# 给dadypig实例赋值，年龄age = 30, 姓名name = DdayPig
dadypig.age = 30
dadypig.name = 'Dady Pig'
# 打印dadypig的信息：
print(dadypig.printinfo())
