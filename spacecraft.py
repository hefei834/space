class Spacecraft:
    def __init__(self, name, health, speed, position, weapon):
        self.name = name
        self.health = health
        self.speed = speed
        self.position = position
        self.weapon = weapon
    
    def move(self):
        pass
    
    def attack(self, target):
        pass
    
    def take_damage(self, damage_amount):
        pass
    
    def is_alive(self):
        pass

class Fighter(Spacecraft):
    def __init__(self, name, health, speed, position, weapon, shield_strength):
        super().__init__(name, health, speed, position, weapon)
        self.shield_strength = shield_strength
    
    def recharge_shield(self):
        pass
    
    def take_damage(self, damage_amount):
        pass