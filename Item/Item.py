class Item:
    def __init__(self, name, description, item_level):
        self.name = name
        self.description = description
        self.item_level = item_level
        
    def useItem(self, player):
        for name in player.inventory:
            if name == self.name:
                player.inventory.remove(name)
                return f"{self.name} has been used by {player.name}!"
        
    