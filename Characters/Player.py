from Characters.Character import Character

class Player(Character):
    def __init__(self, name, player_type):
        super().__init__(name, player_type)
        self.player_type = player_type
        self.defTypePlayer(player_type)
        self.inventory = []
        self.xp = 0
        self.weapon = None
        self.armor = None
        
    player_types = {
        "warrior": {"strength": 5, "health": 20, "mana": -10},
        "mage": {"strength": -2, "mana": 20},
        "healer": {"strength": -5, "health": 10, "mana": 15},
        "assassin": {"strength": 10, "health": -10, "mana": -10}
    }

    def defTypePlayer(self, player_type):
        if player_type in self.player_types:
            attributes = self.player_types[player_type]
            for attr, value in attributes.items():
                if hasattr(self, attr):
                    setattr(self, attr, getattr(self, attr) + value)
        else:
            print("Tipo de Jugador invalido.")
    
    def gainXp(self, amount):
        self.xp += amount

        while self.xp >= 100:
            self.levelUp()
            self.xp -= 100
            print(f"{self.name} has leveled up! Current level: {self.level}")
        else:
            print(f"{self.name} gains {amount} XP. Total XP: {self.xp}")
        
    def levelUp(self):
        self.level += 1
        self.strength += 2
        self.health += 5
        self.mana += 3
    
    def addItem(self, item):
        self.inventory.append(item)
        print(f"{self.name} has obtained {item.name}. Check it in your inventory!")
    
    
