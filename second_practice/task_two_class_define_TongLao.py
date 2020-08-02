# 定义一个TongLao类，my_hp:血量，my_fight:武力值，方法有see_people,fight_zms
class TongLao:

    # 定一个构造函数,参数传入属性my_hp:我的血量，my_fight:我的武力值
    def __init__(self, my_hp, my_fight):
        self.my_hp = my_hp
        self.my_fight = my_fight

    # see_people方法，需要传入一个name参数:
    def see_people(self, name):

        # 如果传入”WYZ”（无崖子），则打印，“师弟！！！！”，
        if name == 'WYZ':
            print("师弟！！！！")
        # 如果传入“李秋水”，打印“呸，贱人”
        elif name == '李秋水':
            print("呸，贱人")
        # 如果传入“丁春秋”，打印“叛徒！我杀了你”
        elif name == "丁春秋":
            print("叛徒，我杀了你")
        # 如果传入的非WYZ、李秋水、丁春秋，则打印"你是何门何派，报上名来"
        else:
            print("你是何门何派，报上名来")

    # fight_zms方法（天山折梅手）
    def fight_zms(self, enemy_hp, enemy_power):

        # 调用天山折梅手方法会将自己的武力值提升10倍，血量缩减2倍
        self.my_fight = self.my_fight * 10
        self.my_hp = self.my_hp / 2
        # 参数传入敌人的血量enemy_hp和敌人的战斗值：power
        enemy_hp = enemy_hp
        enemy_power = enemy_power
        # 进行一回合对打，定义变量my_final_hp：表示对打完成后我剩余的血量，enemy_final_hp:表示对打完成后敌人剩余的血量
        my_final_hp = self.my_hp - enemy_power
        enemy_final_hp = enemy_hp - self.my_fight
        # 打完之后，比较双方血量。血多的一方获胜。
        # 如果我最后剩余的血量多，则打印我获胜
        if my_final_hp > enemy_final_hp:
            print("耶，我获胜了")
        # 如果敌人剩余血量多，则敌人获胜，打印：不，敌人获胜了
        elif my_final_hp < enemy_final_hp:
            print("不，敌人获胜了")
        # 如果我和敌人剩余血量相同，则平局，打印：平局，换个地方再约一架
        else:
            print("平局，换个地方再约一架")



