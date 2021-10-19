# Course: CS 30
# Period: 3
# Date created: 20/9/2021
# Date last modified: 10/20/2021
# Name: Ben Oblinski
# Description: Menu system for a text-based RPG game

inventory = []
# list of items the player is carrying
# list can be accsessed by typing 'inv'


def playerInventory():
    print("")
    print("☠-----☠-----INVENTORY-----☠-----☠")
    if inventory == []:
        print("You are not carryinging any items")
    else:
        for item in inventory:
            print(item)
    print("☠-----☠-----☠-----☠-----☠")
    print("")
