from src.spacecraft import Spacecraft, Fighter
from src.weapon import Weapon, LaserCannon
from src.enemy import Enemy, AlienShip
from src.gamestate import GameState

def main():
    # 获取游戏状态单例
    game_state = GameState.get_instance()
    game_state.start_game()
    print("游戏开始！当前关卡：", game_state.level)
    
    # 使用工厂模式创建战斗机
    fighter = Spacecraft.create_fighter("星际守护者")
    print(f"已创建太空船：{fighter.name}，生命值：{fighter.health}")
    
    # 创建激光炮武器
    laser = LaserCannon(damage=30, range=800, energy_cost=15)
    fighter.weapon = laser
    print(f"{fighter.name}已装备激光炮，伤害：{laser.damage}，能量消耗：{laser.energy_cost}")
    
    # 创建敌舰
    alien = AlienShip(aggression_level=7, species="Zerg", special_ability="分裂")
    print(f"发现敌舰：{alien.species}，攻击等级：{alien.aggression_level}，特殊能力：{alien.special_ability}")
    
    # 模拟游戏过程
    print("\n===== 战斗开始 =====")
    # 太空船移动
    fighter.move()
    print(f"{fighter.name}正在移动...")
    
    # 太空船攻击
    fighter.attack()
    print(f"{fighter.name}使用激光炮攻击！")
    
    # 敌舰攻击
    alien.attack()
    print(f"{alien.species}发动攻击！")
    
    # 太空船承受伤害
    fighter.take_damage(20)
    print(f"{fighter.name}受到20点伤害！")
    
    # 恢复护盾
    fighter.recharge_shield()
    print(f"{fighter.name}正在恢复护盾...")
    
    # 敌舰生成小兵
    alien.spawn_minions()
    print(f"{alien.species}生成了小兵！")
    
    # 更新游戏状态
    game_state.score += 100
    game_state.level += 1
    game_state.update()
    print(f"游戏状态更新 - 分数：{game_state.score}，当前关卡：{game_state.level}")
    
    # 游戏结束
    game_state.game_over("玩家成功击败敌舰！")
    print("===== 游戏结束 =====")

if __name__ == "__main__":
    main()