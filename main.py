# Course: CS 30
# Period: 3
# Date created: 20/9/2021
# Date last modified: 11/14/2021
# Name: Ben Oblinski
# Description: Start up menu system for a text-based RPG game

# Imports the exernal files and displays
# a warining if there is a problem
import CreateCharacter as create
import Map as gridmap
import time

"""
# Prints welcome menu
print("welcome to Dusk")
time.sleep(3)
print("Dusk is a text based adventure game set in a dark, sci-fi world")
time.sleep(3)
print("as the story begins you are")
print("the lone survior of a mysterious disater")
time.sleep(3)
print('you wake up in an abandonded facility with no memories')
print('and no weapons or items')
time.sleep(3)
print('suddenly, you get the feeling that you are being watched')
time.sleep(3)
print('in the distance, you hear some kind of animal howl...')
time.sleep(5)
x = 

░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░███░░██░█░████░██░░█░░░░░░
░░░░░██░█░██░█░█░░░░██░█░░░░░░░
░░░░░██░█░██░█░░█░░░███░░░░░░░░
░░░░░██░█░██░█░░░█░░██░█░░░░░░░
░░░░░██░█░██░█░░░░█░██░░█░░░░░░
░░░░░███░░████░████░██░░░█░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░

print(x)
time.sleep(5)
"""
# Calls the character creation menu
create.CharacterCreationMenu()

# Prints the tutorial 
print('☠-----☠-----Tutorial-----☠-----☠')
print('The game map is a 2d checker board')
print('You can use comands to move around the map')
time.sleep(2.5)
print('w -> move verticaly up')
print('s -> move verticaly down')
print('d -> move horizontaly left')
print('a -> move horizontaly right\n')
time.sleep(2.5)
print('When you are in combat, type kill to damage an enemy')
print('You can also inspect an enemy to learn more')
print('Type \'examine\' to examine\n')
time.sleep(2.5)
print('To see your own stats and character')
print('Type \'self\'')
print('You can view your inventory at any time')
print('Type \'inv\' to see it\n')
time.sleep(2.5)
print('If you need to see the main menu again')
print('Type \'menu\' to see it\n')
time.sleep(2.5)
print('The map is a 6 x 6 grid.')
print('Spaces you can walk on are blank')
print('Spaces with a \'■\' are walls, and you cannot go through them')
print('Spaces with a \'☠\' are enemies, avoid them, or be ready for a fight')
print('A \'$\' shows that there is an item to pick up here')
print('Your character is represented by a \'🗡\'')
print('The start and end tiles are marked with an \'S\' and \'E\' respectively')
print('☠-----☠-----MAP-----☠-----☠')
time.sleep(2.5)
# Calls the map function. \
#This function controls the majority of the game
gridmap.main()