from Item import *
from Characters import *

def useWeapon(player, weapon):
    if weapon in player.inventory:
        if verifyWeapon(player):
            player.strength -= player.weapon.damage
            weapon.useWeapon(player)
            player.weapon = weapon
            weapon.useItem(player)
            return f"{player.name} has equipped {weapon.name}, increasing strength base by {weapon.damage}."
        else:
            weapon.useWeapon(player)
            player.weapon = weapon
            weapon.useItem(player)
            return f"{player.name} has equipped {weapon.name}, increasing strength base by {weapon.damage}."

def useArmor(player, armor):
    if armor in player.inventory:
        if verifyArmor(player):
            player.defense -= player.armor.defense
            armor.useArmor(player)
            player.armor = armor
            armor.useItem(player)
            return f"{player.name} has equipped {armor.name}, increasing defense by {armor.defense}."
        else:
            armor.useArmor(player)
            player.armor = armor
            armor.useItem(player)
            return f"{player.name} has equipped {armor.name}, increasing defense by {armor.defense}."

def usePotion(player, potion):
    if potion in player.inventory:
        if potion.use(player):
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
    
def boostDuration(player, potion):
    if potion.effect_type == "strength_boost":
        time, value = potion.use(player)
        for turno in range(time, 0, -1):
            pass
        player.strength -= value