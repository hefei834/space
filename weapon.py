class Weapon:
    def __init__(self, name, damage, range, ammo):
        self.name = name
        self.damage = damage
        self.range = range
        self.ammo = ammo
    
    def fire(self, target):
        pass
    
    def reload(self):
        pass

class LaserCannon(Weapon):
    def __init__(self, name, damage, range, energy_consumption):
        super().__init__(name, damage, range, 0)
        self.energy_consumption = energy_consumption
    
    def fire(self, target):
        pass