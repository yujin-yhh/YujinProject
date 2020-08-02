# 导入模块
from YujinProject.second_practice.task_one_class_define_Pig import BabyPig

# 实例化一个对象pepapig,工作job是student，同学classmate 是Susan
pepapig = BabyPig('student', 'Susan')
# 给pepepig实例赋值，年龄age是4岁，名字name 是Pepa Pig
pepapig.age = 4
pepapig.name = 'Pepa Pig'
# 调用printinfo()打印信息
pepapig.printinfo()
# 调用pint方法和jumpin_pud方法
pepapig.paint('Teddy Bear')
pepapig.jumpin_pud()