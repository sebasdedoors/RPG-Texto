from Characters.Player import Player
from Characters.Enemy import Enemy

from Item.Weapon import Weapon


def killEnemy(player, enemy):
    if enemy.health <= 0:
        player.gainXp(enemy.xp_reward)
        print(f"{player.name} gains {enemy.xp_reward} XP. Total XP: {player.xp}")
        return True
    return False