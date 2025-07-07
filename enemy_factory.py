class EnemyFactory:
    @staticmethod
    def create_enemy(enemy_type, *args, **kwargs):
        if enemy_type == "AlienShip":
            return AlienShip(*args, **kwargs)
        # 可扩展其他敌舰类型的创建逻辑