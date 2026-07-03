class Item:
    def __init__(self, name, description, item_level):
        self.name = name
        self.description = description
        self.item_level = item_level
        
    def use(self, player):
        pass