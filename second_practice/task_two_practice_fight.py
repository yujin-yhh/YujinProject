# 导入Tonglao模块
from YujinProject.second_practice.task_two_class_define_TongLao import TongLao
# 导入XuZhu模块
from YujinProject.second_practice.task_two_class_define_XuZhu import XuZhu

# 实例化一个TongLao类的对象tonglaofir，传入血量20000，武力值1040
tonglaofir = TongLao(20000, 1040)
# 调用tonglaofir的see_people方法，传入名字WYZA,打印你是何门何派，报上名来
tonglaofir.see_people('WYZA')
# 调用tonglaofir的see_people方法，传入名字WYZ,打印：师弟！！！！
tonglaofir.see_people('WYZ')
# 调用tonglaofir的see_people方法，传入名字李秋水,打印：呸，贱人
tonglaofir.see_people('李秋水')
# 调用tonglaofir的see_people方法，传入名字丁春秋,打印：叛徒，我杀了你
tonglaofir.see_people('丁春秋')
# 将tonglaofir的血量20000，武力值1040和敌人的血量20000，战斗值4000一回合对打：敌人获胜，打印"不，敌人获胜了"
tonglaofir.fight_zms(20000, 4000)

# 重新实例化一个对象tonglaosec,传入血量20000，武力值1040
# 将toglao的血量20000，武力值1000和敌人的血量20000，战斗值1000一回合对打：我获胜，打印"耶，我获胜了"
tonglaosec = TongLao(20000, 1040)
tonglaosec.fight_zms(20000, 200)

# 重新实例化一个对象tonglaothird,传入血量20000，武力值1040
# 将tonglaothird的血量20000，武力值1040和敌人的血量20000，战斗值1000一回合对打：我获胜，打印"耶，我获胜了"
tonglaothird = TongLao(20000, 1040)
tonglaothird.fight_zms(20000, 400)

# 实例化一个对象xuzhu,传入血量20000，战斗值1040
xuzhu = XuZhu(20000, 1040)
# 调用父类的方法see_people,传入WYZ，打印虚竹
xuzhu.see_people('WYZ')
# 调用父类的方法fight_zms,传入敌人的血量20000，战斗之10000，一回合对打，打印：不，敌人获胜了
xuzhu.fight_zms(20000, 10000)
# 调用子类的方法read，打印：罪过罪过
xuzhu.read()