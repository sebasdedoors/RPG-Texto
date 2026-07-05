from Characters import *
from Item import *


def killEnemy(self, player, enemy):
    if enemy.health <= 0:
        player.gainXp(enemy.xp_reward)