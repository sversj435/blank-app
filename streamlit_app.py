def combat_round(player1, player2):

    atk1, def1, action1, predict1, hp1 = player1.values()
    atk2, def2, action2, predict2, hp2 = player2.values()
    if action1.lower() == 'a':
        atk1 *= 2  
        if predict1.lower() == 'a' and action2.lower() == 'a':
            def1 *= 1.5  
        elif predict1.lower() == 'd' and action2.lower() == 'd':
            atk1 *= 2.5 / 2  
    elif action1.lower() == 'd':  
        def1 *= 1.5  
        if predict1.lower() == 'a' and action2.lower() == 'a':
            def1 *= 1.5 
        elif predict1.lower() == 'd' and action2.lower() == 'd':
            atk1 *= 2.5 / 2 
        atk1 = 0 
        
    if action2.lower() == 'a': 
        atk2 *= 2  
        if predict2.lower() == 'a' and action1.lower() == 'a':
            def2 *= 1.5  
        elif predict2.lower() == 'd' and action1.lower() == 'd':
            atk2 *= 2.5 / 2 
    elif action2.lower() == 'd':  
        def2 *= 1.5  
        if predict2.lower() == 'a' and action1.lower() == 'a':
            def2 *= 1.5 
        elif predict2.lower() == 'd' and action1.lower() == 'd':
            atk2 *= 2.5 / 2  
        atk2 = 0  


    damage_to_p1 = max(0, atk2 - def1)
    damage_to_p2 = max(0, atk1 - def2)


    hp1 -= damage_to_p1
    hp2 -= damage_to_p2

    return damage_to_p1, damage_to_p2, max(0, hp1), max(0, hp2)

def main():
    print("====== 回合开始！======")
    

    atk1 = float(input("玩家1的攻击力："))
    def1 = float(input("玩家1的防御力："))
    action1 = input("玩家1的行为（A攻击/D防御）：")
    predict1 = input("玩家1预测对手行为（A攻击/D防御）：")
    hp1 = float(input("玩家1的血量："))


    atk2 = float(input("玩家2的攻击力："))
    def2 = float(input("玩家2的防御力："))
    action2 = input("玩家2的行为（A攻击/D防御）：")
    predict2 = input("玩家2预测对手行为（A攻击/D防御）：")
    hp2 = float(input("玩家2的血量："))


    player1 = {"ATK": atk1, "DEF": def1, "ACTION": action1, "PREDICT": predict1, "HP": hp1}
    player2 = {"ATK": atk2, "DEF": def2, "ACTION": action2, "PREDICT": predict2, "HP": hp2}


    damage_to_p1, damage_to_p2, remaining_hp1, remaining_hp2 = combat_round(player1, player2)


    print("====== 战斗结果 ======")
    print(f"玩家1造成的伤害：{damage_to_p2}")
    print(f"玩家2造成的伤害：{damage_to_p1}")
    print(f"玩家1剩余血量：{remaining_hp1}")
    print(f"玩家2剩余血量：{remaining_hp2}")

if __name__ == "__main__":
    main()
