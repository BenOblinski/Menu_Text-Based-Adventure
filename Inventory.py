# Course: CS 30
# Period: 3
# Date created: 20/9/2021
# Date last modified: 10/20/2021
# Name: Ben Oblinski
# Description: Inventory portion of the game menu

inventory = []
# list of items the player is carrying
# list can be accsessed by typing 'inv'


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
            print(item)
    print("☠-----☠-----☠-----☠-----☠\n")
