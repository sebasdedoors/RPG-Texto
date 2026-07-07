from Characters.Player import Player
from Characters.Enemy import Enemy
from Characters.Character import Character 

from Item.Weapon import Weapon
from Item.Item import *
from Item.Armor import Armor
from Item.Potion import Potion 

from Process.Combat_Handler import *
from Process.Item_Handler import *

import os
import time

username = ""
hero_type = ""
player = ""

def clear_screen():
    os.system("cls")

def menu():
    print("""
    ****** Hero Types ******
    1- Warrior
    2- Mage
    3- Healer
    4- Assassin 
""")

def main():
    print(f"Welcome to my first game!")
    time.sleep(5)
    clear_screen()
    global username
    username = input("Write your namertag: ")
    print("Saving...")
    time.sleep(5)
    clear_screen()
    menu()
    print("")
    global hero_type
    hero_type = input(f"Welcome {username}, now write your hero: ")
    global player
    player = Player(username, hero_type.lower())

    


