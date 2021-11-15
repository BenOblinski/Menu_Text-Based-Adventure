# Course: CS 30
# Period: 3
# Date created: 20/9/2021
# Date last modified: 10/25/2021
# Name: Ben Oblinski
# Description: Inventory portion of the game menu
from random import choice, randint

# List of items you have
inventory = []

# List of items that can be otained
items = ['crowbar', 'knife', 'spiked bat', 'club', 'lead pipe',
         'rubber chicken', 'broken bottle', 'frying pan', 'katana', 
         'hammer']

# Dictionary of the stats of all the weapons
item_stats = {'crowbar': {'Damage': 3, 'Handling': 2},
              'knife': {'Damage': 1, 'Handling': 4},
              'spiked bat': {'Damage': 2, 'Handling': 5},
              'club': {'Damage': 3, 'Handling': 1},
              'lead pipe': {'Damage': 5, 'Handling': 2},
              'rubber chicken': {'Damage': 7, 'Handling': 5},
              'broken bottle': {'Damage': 3, 'Handling': 4},
              'frying pan': {'Damage': 6, 'Handling': 4},
              'katana': {'Damage': 4, 'Handling': 6},
              'hammer': {'Damage': 3, 'Handling': 5}
              }


def playerInventory():
    """ This function prints out the list of items being
    carried by the player.
    Prints out the contents of the inventory list.
    This function can be called by typing 'inv'
    """
    print("\n☠-----☠-----INVENTORY-----☠-----☠")
    if inventory == []:
        print("You are not carryinging any items")
    else:
        for item in inventory:
            x = item
            print(f"{item.title()}| Damage:{item_stats[x]['Damage']}\
 Handling:{item_stats[x]['Handling']}")
    print("☠-----☠-----☠-----☠-----☠\n")


def pick_up_item(item):
    """When the player moves onto a space occupied by an item
    this code chooses a random item to display
    """
    print(f"There is a {item} here!")
    take_item = input("Would you like to pick it up? Y/N\n")
    if take_item.lower() == 'y':
        inventory.append(item)
        playerInventory()
    else:
        playerInventory()
