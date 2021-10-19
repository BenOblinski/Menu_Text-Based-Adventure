# Course: CS 30
# Period: 3
# Date created: 20/9/2021
# Date last modified: 
# Name: Ben Oblinski
# Description: Character portion of the game menu 

charcters = {"John Ruth": {"Description": "A grisled bounty hunter with a scar on his right eye",
                           "Health": 120, 
                           "Attack": 45, 
                           "Defense": 30},
             "Austin Maverick":
                          {"Descrpition": "A lawman who deals out justice the way he sees fit",
                           "Health": 100,
                           "Attack": 50,
                           "Defense": 25},
             "Gunner Ace":
                          {"Description": "An outlaw, framed by a coript sheif for murder",
                           "Health": 110,
                           "Attack": 40,
                           "Defense": 35},
             "Jake \"The Snake\" Calloway":
                          {"Descrpition": "A dirty outlaw wanted for robbery across the state",
                           "Health": 95,
                           "Attack": 55,
                           "Defense": 25}}
# list of your characters
# this list can be accsessed by typing 'charc'
# subdivisions of the inv dictonary: characters/person/stats


def playerCharacters():
    print("☠-----☠-----CHARCATERS-----☠-----☠")
     # if the player wants to see character traits...
    for person in charcters:
        print(f"-> {person}")
        # print the characters name
        for stats in charcters[person]:
            print(f"{stats} - {charcters[person][stats]}")
            # print the character descriptions next to the name
        print("")
    print("☠-----☠-----☠-----☠-----☠")
