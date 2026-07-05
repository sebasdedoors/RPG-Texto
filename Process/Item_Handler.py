from Item import *
from Characters import *

def useWeapon(player, weapon):
    if weapon in player.inventory:
        if verifyWeapon(player):
            player.strength -= player.weapon.damage
            player.strength += weapon.damage
            player.weapon = weapon.name
            weapon.useItem(player)
            return f"{player.name} has equipped {weapon.name}, increasing strength base by {weapon.damage}."
        else:
            player.strength += weapon.damage
            player.weapon = weapon.name
            weapon.useItem(player)
            return f"{player.name} has equipped {weapon.name}, increasing strength base by {weapon.damage}."

def useArmor(player, armor):
    if armor in player.inventory:
        if verifyArmor(player):
            player.defense -= player.armor.defense
            player.defense += armor.defense
            player.armor = armor.name
            armor.useItem(player)
            return f"{player.name} has equipped {armor.name}, increasing defense by {armor.defense}."
        else:
            player.defense += armor.defense
            player.armor = armor.name
            armor.useItem(player)
            return f"{player.name} has equipped {armor.name}, increasing defense by {armor.defense}."

def usePotion(player, potion):
    if potion in player.inventory:
        potion.use(player)
        potion.useItem(player)

def verifyWeapon(player):
    if player.weapon != None:
        return True
    else:
        return False

def verifyArmor(player):
    if player.armor != None:
        return True
    else:
        return False