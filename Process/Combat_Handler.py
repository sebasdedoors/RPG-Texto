from Characters import *
from Item import *


def killEnemy(player, enemy):
    if enemy.health <= 0:
        player.gainXp(enemy.xp_reward)
        print(f"{player.name} gains {enemy.xp_reward} XP. Total XP: {player.xp}")
        return True
    return False