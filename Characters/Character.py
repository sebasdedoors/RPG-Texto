class Character:
    def __init__(self, name, character_type):
        self.name = name
        self.health = 100
        self.strength = 10
        self.character_type = character_type
        self.mana = 100
        self.level = 1
        self.defense = 0

    def attack(self, target):
        damage = self.strength - target.defense
        damage = max(1, damage)
        target.health -= damage
        print(f"{self.name} attacks {target.name} for {damage} damage.")


    
