class Enemy:
    def __init__(self, name, health, aggression_level):
        self.name = name
        self.health = health
        self.aggression_level = aggression_level
    
    def attack(self, target):
        pass
    
    def take_damage(self, damage_amount):
        pass
    
    def is_alive(self):
        pass

class AlienShip(Enemy):
    def __init__(self, name, health, aggression_level, special_ability):
        super().__init__(name, health, aggression_level)
        self.special_ability = special_ability
    
    def use_special_ability(self):
        pass