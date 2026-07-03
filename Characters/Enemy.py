from Characters.Character import Character

class Enemy(Character):
    def __init__(self, name, enemy_type):
        super().__init__(name, enemy_type)
        self.enemy_type = enemy_type
        self.xp_reward = 0
        self.defTypeEnemy(enemy_type)
    
    enemy_types = {
        "goblin": {
            "strength": 3,
            "health": 10,
            "mana": -5,
            "xp_reward": 10
        },
        "orc": {
            "strength": 5,
            "health": 20,
            "mana": -10,
            "xp_reward": 20
        },
        "troll": {
            "strength": 7,
            "health": 30,
            "mana": -15,
            "xp_reward": 30
        }
    }

    def defTypeEnemy(self, enemy_type):
        if enemy_type in self.enemy_types:
            attributes = self.enemy_types[enemy_type]
            for attr, value in attributes.items():
                if hasattr(self, attr):
                    setattr(self, attr, getattr(self, attr) + value)
        else:
            print("Tipo de Enemigo invalido.")
