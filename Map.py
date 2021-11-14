# Course: CS 30
# Period: 3
# Date created: 20/9/2021
# Date last modified: 10/25/2021
# Name: Ben Oblinski
# Description: map system for the game menu
import CreateCharacter as create
import Inventory as inv
import Enemies as badguys
from random import choice, randint
import sys

# Created list of coords of all walls
walls = []
# List of where there can be no walls
no_wall = [[4, 5], [5, 4], [1, 0], [0, 1], [0, 0], [5, 5]]
# List of wher there cannot be any tiles other that Start and End tiles
no_things = [[0, 0], [5, 5]]
# Created list of coords of all items
treasure = []
# Created list of coords of all monsters
monsters = []


class GridMap:
    """Class builds a map to the spcified dimesions"""
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.player = [0, 0]
        self.start_tile = [0, 0]
        self.end_tile = [5, 5]

    def move_player(self, d, q):
        """Takes an input from the player and outputs the 
        desired result
        """
        # Move player right
        if d == 'd':
            self.player[0] = self.player[0] + 1

        # Move player left
        elif d == 'a':
            self.player[0] = self.player[0] - 1

        # Move player up
        elif d == 'w':
            self.player[1] = self.player[1] - 1

        # Move player down
        elif d == 's':
            self.player[1] = self.player[1] + 1

        # Show player inventory
        elif d == 'inv':
            inv.playerInventory()

        # If the playe asks to see the menu, show this menu
        elif d == 'menu':
            print("☠-----☠-----☠-----☠-----☠-----☠")
            print('Actions:')
            print('w -> move verticaly up')
            print('s -> move verticaly down')
            print('a -> move horizontaly left')
            print('d -> move horizontaly right')
            print('inv -> show the items you have\n')
            print('examine -> learn more about an enemy')
            print('kill -> fight off an enemy')
            print('self -> see your own stats and character')
            print('You can type \'menu\' at any time to see this menu')
            print("☠-----☠-----☠-----☠-----☠-----☠")

        # If the player asks to see their stats, display this menu
        elif d == 'self':
            print("☠-----☠-----YOUR CHARACTER-----☠-----☠")
            x = open('CharacterName.txt', 'r')
            nameChoice = str(x.read())
            x.close()
            print(f'Name: {nameChoice.title()}')
            create.printChosenClass()

        # If the player is in a wall
        if self.player in walls:
            # Revert back to the preivous position
            self.player = q

        # If the player is on a treasure tile
        if self.player in treasure:
            # Ask the player if they want to pick up the item
            item = choice(inv.items)
            inv.pick_up_item(item)
            treasure.remove(self.player)

        # If the player is on a til with a monster
        if self.player in monsters:
            badguys.fight_scene()

            # remove all monsters on this tile
            try:
                while True:
                    monsters.remove(self.player)
            except ValueError:
                pass

        # If the player is on the end tile, turn the game off
        if self.player == self.end_tile:
            print("You Win!")
            sys.exit()

        # Keeps player from goin off the map
        if self.player[0] > 5:
            self.player[0] = 5

        if self.player[0] < 0:
            self.player[0] = 0

        if self.player[1] < 0:
            self.player[1] = 0

        if self.player[1] > 5:
            self.player[1] = 5


def draw_grid(g, width=2.4):
    """Draws the map with walls, monsters and other tile types"""
    for y in range(g.height):
        for x in range(g.width):
            # Wall tile type
            if [x, y] in walls:
                symbol = ' ■ '

            # Player tile type
            elif [x, y] == g.player:
                symbol = ' 🗡 '

            # Monster tile type
            elif [x, y] in monsters:
                symbol = ' ☠ '

            # Treasure tile type
            elif [x, y] in treasure:
                symbol = ' $ '

            # Start tile type
            elif [x, y] == g.start_tile:
                symbol = ' S '

            # End tile type
            elif [x, y] == g.end_tile:
                symbol = ' E '

            # Blank tile type
            else:
                symbol = '   '
            print("%%-%ds" % width % symbol, end="")
        print()


def get_walls():
    """makes a list of the coordiantes of all the walls"""
    for i in range(1, 8):

        x = randint(0, 5)
        y = randint(0, 5)
        if [x, y] in no_wall:
            x = 3
            y = 3
        walls.append([x, y])


def get_monsters():
    """makes a list of the coordiantes of all the monsters"""
    for i in range(1, 13):

        x = randint(0, 5)
        y = randint(0, 5)

        if x == 5 and y == 5:
            x = 4
            y = 5

        if x == 0 and y == 0:
            x = 1
            y = 0
        monsters.append([x, y])


def get_items():
    """makes a list of the coordiantes of all the treasure items"""
    for i in range(1, 4):

        x = randint(0, 5)
        y = randint(0, 5)
        if x == 5 and y == 5:
            x = 4
            y = 5

        if x == 0 and y == 0:
            x = 1
            y = 0
        if [x, y] not in monsters:
            if [x, y] not in no_things:
                treasure.append([x, y])
        else:
            pass


def main():
    """The main function that controls the whole game"""
    # Create the first map and lists of items, walls and monsters
    g = GridMap(6, 6)
    get_walls()
    get_monsters()
    get_items()
    draw_grid(g)
    while True:
        # The main game loop
        q = g.player.copy()
        # Record players current location
        d = input("> ")
        # Take user input
        g.move_player(d, q)
        # Move the player, if the new position in a wall
        #revert to the recorded previous position 'q'
        draw_grid(g)
        # Draw the new map
