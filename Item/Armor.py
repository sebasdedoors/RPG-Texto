from Item.Item import Item

class Armor(Item):
    def __init__(self, name, description, armor_level):
        super().__init__(name, description, armor_level)
        self.defense = self.armors[armor_level]

    armors = {
        1: 5,
        2: 15,
        3: 30
    }

    def useArmor(self, player):
        if self.item_level in self.armors:
            player.defense += self.armors[self.item_level]