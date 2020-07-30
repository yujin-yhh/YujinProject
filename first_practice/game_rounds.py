# 定义一个函数game_fight，实现回合制游戏对打
def game_fight():
# 定义变量及默认值：my_hp：我的血量，your_hp：敌人血量，my_fight：我的战斗值，your_fight：敌人的战斗值
    my_hp = 1000
    your_hp = 1000
    my_fight = 200
    your_fight = 100
# while循环，在我和敌人血量有一个为0前一直对打
    while True:
        # 如果血量不足敌人战斗值，对打完成后我的血量为0，否则 我的血量 = 我的血量 - 敌人战斗值，
        # 防止出现打印的战斗值为负的情况
        if my_hp < your_fight:
            my_hp = 0
        else:
            my_hp = my_hp - your_fight

        # 如果敌人血量不足我的战斗值，对打完成后敌人的血量为0，否则敌人血量= 敌人血量 - 我的战斗值
        # 防止出现打印的战斗值为负的情况
        if your_hp < my_fight:
            your_hp = 0
        else:
            your_hp = your_hp - my_fight
        # 如果我的血量先为0，敌人获胜。结束循环，游戏终止，打印提示语
        if my_hp == 0:
            print(f"我的剩余血量{my_hp}，敌人的剩余血量{your_hp}")
            print("敌人赢了")
            break
        # 如果敌人的血量为0，结束循环，游戏终止，打印提示语
        elif your_hp == 0:
            print(f"我的剩余血量{my_hp}，敌人的剩余血量{your_hp}")
            print("我赢了")
            break

#开始进行对打
game_fight()