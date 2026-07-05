class Item:
    def __init__(self, name, description, item_level):
        self.name = name
        self.description = description
        self.item_level = item_level
        
    def useItem(self, player):
        if self in player.inventory:
            player.inventory.remove(self)
            return f"{self.name} has been used by {player.name}!"
        