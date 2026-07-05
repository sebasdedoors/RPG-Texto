from Item.Item import Item

class Potion(Item):
    def __init__(self, name, description, effect_type, potion_level):
        super().__init__(name, description, potion_level)
        self.effect_type = effect_type
        self.effect_value = 0
        
    effects = {
        "heal": {
            1: 5,
            2: 10,
            3: 20
        },
        "mana": {
            1: 10,
            2: 15,
            3: 25
        },
        "strength_boost": {
            1: {
                "value": 3,
                "time": 5
            },
            2: {
                "value": 5,
                "time": 10
            },
            3: {
                "value": 10,
                "time": 15
            }
        }
    }

    def use(self, player):
        if self.effect_type in self.effects:
            if self.effect_type == "heal":
                for level, value in self.effects[self.effect_type].items():
                    if self.item_level == level:
                        health_max = player.health
                        player.health = min(player.health + value, health_max)
                        print(f"{player.name} has used {self.name}, restoring {value} health.")
                        return 
            elif self.effect_type == "mana":
                for level, value in self.effects[self.effect_type].items():
                    if self.item_level == level:
                        mana_max = player.mana
                        player.mana = min(player.mana + value, mana_max)
                        print(f"{player.name} has used {self.name}, restoring {value} mana.")
                        return
            elif self.effect_type == "strength_boost":
                for level, effect in self.effects[self.effect_type].items():
                    if self.item_level == level:
                        player.strength += effect["value"]
                        print(f"{player.name} has used {self.name}, gaining {effect['value']} strength for {effect['time']} turns.")
                        return effect["time"], effect["value"]