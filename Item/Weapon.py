from Item.Item import Item

class Weapon(Item):
    def __init__(self, name, description, damage, weapon_level):
        super().__init__(name, description, weapon_level)
        self.damage = damage
    
    def useWeapon(self, player):
        player.strength += self.damage