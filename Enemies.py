# Course: CS 30
# Period: 3
# Date created: 20/9/2021
# Date last modified: 10/25/2021
# Name: Ben Oblinski
# Description: Menu system for a text-based RPG game
from random import choice
enemies = ['BullBerserker', 'CrazySkeleton', 'Arachnind',
           'PumpkinFace', 'HeadlessSoldier', 'CaveDemon', 'BioPod']


class enemy(object):
    """genetic enemy class"""
    def __init__(self):
        self.name = ''
        self.description = ''
        self.hp = 1
        self.hpMAX = 1
        self.damage = 2

    def resetHP(self):
        """resets the enemies hp to its max after a battle"""
        self.hp = self.hpMAX


class BullBerserker(enemy):
    """A cyborg bull"""
    def __init__(self):
        self.name = 'Bull Berserker'
        self.description = 'A red skinned, bipedal\
bull with lazer canons on it\'s arms'
        self.hp = 15
        self.hpMAX = 15
        self.damage = 4


class CrazySkeleton(enemy):
    """A cyborg skeleton"""
    def __init__(self):
        self.name = 'Crazy Skeleton'
        self.description = 'A human skeleton covered in electronic \
motors and weapons'
        self.hp = 4
        self.hpMAX = 4
        self.damage = 2


class Arachnind(enemy):
    """A robot human spider scorpion"""
    def __init__(self):
        self.name = 'Arachnind MK1'
        self.description = 'A half human, half spider,\
half scorpioin that seems to be covered in robotic parts. '
        self.hp = 24
        self.hpMAX = 24
        self.damage = 6


class HeadlessSoldier(enemy):
    """A headless soldier with 2 big guns"""
    def __init__(self):
        self.name = 'Headless Soldier'
        self.description = 'Despite Having no mouth,\
he sreams very loudly'
        self.hp = 7
        self.hpMAX = 7
        self.damage = 8


class PumpkinFace(enemy):
    """A pumpkin faced giant"""
    def __init__(self):
        self.name = 'Pumpkin Faced Giant'
        self.description = 'A giant, bulbous man wearing a pumpkin \
on his head'
        self.hp = 30
        self.hpMAX = 30
        self.damage = 7


class CaveDemon(enemy):
    """A lizard monsters that dwells in caves"""
    def __init__(self):
        self.name = 'Cave Demon'
        self.description = 'A giant, lizard like monster.\
It has two front legs, a long tail, and 100\'s of teeth'
        self.hp = 30
        self.hpMAX = 30
        self.damage = 7

class BioPod(enemy):
    """A brain in a robotic body"""
    def __init__(self):
        self.name = 'Bio-Pod'
        self.description = 'A floating brain in a jar with\
roboic spider legs'
        self.hp = 6
        self.hpMAX = 6
        self.damage = 12


def fight_scene():
    """When the player moves onto a space occupied by an enemy
    this code chooses a random enemy to fight and controls the battler
    """
    monster_defeated = False
    enemy = choice(enemies)
    if enemy == 'BullBerserker':
        combat_enemy = BullBerserker()

    elif enemy == 'CrazySkeleton':
        combat_enemy = CrazySkeleton()

    elif enemy == 'Arachnind':
        combat_enemy = Arachnind()

    elif enemy == 'HeadlessSoldier':
        combat_enemy = HeadlessSoldier()

    elif enemy == 'PumpkinFace':
        combat_enemy = PumpkinFace()

    elif enemy == 'CaveDemon':
        combat_enemy = CaveDemon()

    elif enemy == 'BioPod':
        combat_enemy = BioPod()

    print(f'There is a {combat_enemy.name} here!')
    print('What would you like to do?')
    while monster_defeated == False:
        combat_choice = input('Kill, Examine\n')
        if combat_choice.lower() == 'kill':
            print('You have killed the monster!')
            monster_defeated = True
        elif combat_choice.lower() == 'examine':
            print(combat_enemy.description)
