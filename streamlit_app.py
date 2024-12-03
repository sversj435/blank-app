import streamlit as st

def combat_round(player1, player2):
    atk1, def1, action1, predict1, hp1 = player1.values()
    atk2, def2, action2, predict2, hp2 = player2.values()

    # 将行为和预测统一为小写字母，简化后续逻辑
    action1 = "a" if action1 == "攻击" else "d"
    predict1 = "a" if predict1 == "攻击" else "d"
    action2 = "a" if action2 == "攻击" else "d"
    predict2 = "a" if predict2 == "攻击" else "d"

    if action1 == 'a':  # 玩家1选择攻击
        atk1 *= 2
        if predict1 == 'a' and action2 == 'a':
            def1 *= 1.5
        elif predict1 == 'd' and action2 == 'd':
            atk1 *= 2.5 / 2
    elif action1 == 'd':  # 玩家1选择防御
        def1 *= 1.5
        if predict1 == 'a' and action2 == 'a':
            def1 *= 1.5
        elif predict1 == 'd' and action2 == 'd':
            atk1 *= 2.5 / 2
        atk1 = 0

    if action2 == 'a':  # 玩家2选择攻击
        atk2 *= 2
        if predict2 == 'a' and action1 == 'a':
            def2 *= 1.5
        elif predict2 == 'd' and action1 == 'd':
            atk2 *= 2.5 / 2
    elif action2 == 'd':  # 玩家2选择防御
        def2 *= 1.5
        if predict2 == 'a' and action1 == 'a':
            def2 *= 1.5
        elif predict2 == 'd' and action1 == 'd':
            atk2 *= 2.5 / 2
        atk2 = 0

    damage_to_p1 = max(0, atk2 - def1)
    damage_to_p2 = max(0, atk1 - def2)

    hp1 -= damage_to_p1
    hp2 -= damage_to_p2

    return damage_to_p1, damage_to_p2, max(0, hp1), max(0, hp2)


# Streamlit Application
st.title("战斗模拟")

st.header("玩家 1 输入")
atk1 = st.number_input("玩家1的攻击力", min_value=0.0, value=10.0)
def1 = st.number_input("玩家1的防御力", min_value=0.0, value=10.0)
action1 = st.selectbox("玩家1的行为", ["攻击", "防御"])
predict1 = st.selectbox("玩家1预测对手行为", ["攻击", "防御"])
hp1 = st.number_input("玩家1的血量", min_value=0.0, value=100.0)

st.header("玩家 2 输入")
atk2 = st.number_input("玩家2的攻击力", min_value=0.0, value=10.0)
def2 = st.number_input("玩家2的防御力", min_value=0.0, value=10.0)
action2 = st.selectbox("玩家2的行为", ["攻击", "防御"])
predict2 = st.selectbox("玩家2预测对手行为", ["攻击", "防御"])
hp2 = st.number_input("玩家2的血量", min_value=0.0, value=100.0)

if st.button("开始战斗！"):
    st.write("开始计算...")
    player1 = {"ATK": atk1, "DEF": def1, "ACTION": action1, "PREDICT": predict1, "HP": hp1}
    player2 = {"ATK": atk2, "DEF": def2, "ACTION": action2, "PREDICT": predict2, "HP": hp2}

    try:
        damage_to_p1, damage_to_p2, remaining_hp1, remaining_hp2 = combat_round(player1, player2)
        st.header("战斗结果")
        st.write(f"玩家1造成的伤害：{damage_to_p2}")
        st.write(f"玩家2造成的伤害：{damage_to_p1}")
        st.write(f"玩家1剩余血量：{remaining_hp1}")
        st.write(f"玩家2剩余血量：{remaining_hp2}")
    except Exception as e:
        st.error(f"计算出错：{e}")
