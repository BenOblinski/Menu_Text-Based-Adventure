# Course: CS 30
# Period: 3
# Date created: 20/9/2021
# Date last modified: 10/25/2021
# Name: Ben Oblinski
# Description: Menu system for a text-based RPG game
from random import choice
enemies = ['BullBerserker', 'CrazySkeleton', 'Arachnind',
           'PumpkinFace', 'HeadlessSoldier', 'CaveDemon', 
           'BioPod', 'BrainSucker', 'Cyberwolf', 
           'GiantKillerLeech', 'ChainSawManiac', 'ExplodingMushroom', 
           'Fishman', 'RoboMammoth', 'CrazyRobotClown', 
           'NervousChicken', 'KarateZombie', 'BloodyXyloid', 
           'Gnash']


class enemy(object):
    """genetic enemy class"""
    def __init__(self):
        self.name = ''
        self.description = ''
        self.hp = 1
        self.hpMAX = 1
        self.armour = 1
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
        self.armour = 9
        self.damage = 4


class CrazySkeleton(enemy):
    """A cyborg skeleton"""
    def __init__(self):
        self.name = 'Crazy Skeleton'
        self.description = 'A human skeleton covered in electronic \
motors and weapons'
        self.hp = 4
        self.hpMAX = 4
        self.armour = 0
        self.damage = 2


class Arachnind(enemy):
    """A robot human spider scorpion"""
    def __init__(self):
        self.name = 'Arachnind MK1'
        self.description = 'A half human, half spider,\
half scorpioin that seems to be covered in robotic parts. '
        self.hp = 24
        self.hpMAX = 24
        self.armour = 18
        self.damage = 6


class HeadlessSoldier(enemy):
    """A headless soldier with 2 big guns"""
    def __init__(self):
        self.name = 'Headless Soldier'
        self.description = 'Despite Having no mouth,\
he sreams very loudly'
        self.hp = 7
        self.hpMAX = 7
        self.armour = 2
        self.damage = 8


class PumpkinFace(enemy):
    """A pumpkin faced giant"""
    def __init__(self):
        self.name = 'Pumpkin Faced Giant'
        self.description = 'A giant, bulbous man wearing a pumpkin \
on his head'
        self.hp = 30
        self.hpMAX = 30
        self.armour = 14
        self.damage = 7


class CaveDemon(enemy):
    """A lizard monsters that dwells in caves"""
    def __init__(self):
        self.name = 'Cave Demon'
        self.description = 'A giant, lizard like monster.\
It has two front legs, a long tail, and 100\'s of teeth'
        self.hp = 30
        self.hpMAX = 30
        self.armour = 12
        self.damage = 7


class BioPod(enemy):
    """A brain in a robotic body"""
    def __init__(self):
        self.name = 'Bio-Pod'
        self.description = 'A floating brain in a jar with\
roboic spider legs'
        self.hp = 6
        self.hpMAX = 6
        self.armour = 1
        self.damage = 12


class BrainSucker(enemy):
    """A brain with squid tentacles"""
    def __init__(self):
        self.name = 'Brainsucker'
        self.description = 'A flying Brain with squid tentacles\
that sucks your brain out'
        self.hp = 3
        self.hpMAX = 3
        self.armour = 2
        self.damage = 4


class Cyberwolf(enemy):
    """A Cyborg wolf"""
    def __init__(self):
        self.name = 'Cyberwolf'
        self.description = 'A tall, lanky wolf-man with a robotic eye\
and lazer canon'
        self.hp = 3
        self.hpMAX = 3
        self.armour = 3
        self.damage = 4


class GiantKillerLeech(enemy):
    """Giant Swarms of leeches"""
    def __init__(self):
        self.name = 'Giant Killer Leech'
        self.description = 'A giant leech that sucks gallons of\
blood at a time'
        self.hp = 1
        self.hpMAX = 1
        self.armour = 1
        self.damage = 3


class ChainSawManiac(enemy):
    """A crazy dude with a chainsaw"""
    def __init__(self):
        self.name = 'Chain Saw Maniac'
        self.description = 'Is that his face, or someone elses...'
        self.hp = 18
        self.hpMAX = 18
        self.armour = 5
        self.damage = 14


class ExplodingMushroom(enemy):
    """Explodes deeling damage when a player comes near it"""
    def __init__(self):
        self.name = 'Exploding Mushroom'
        self.description = 'A humongous fungus that explodes\
 when touched'
        self.hp = 1
        self.hpMAX = 1
        self.armour = 0
        self.damage = 10


class Fishman(enemy):
    """A pretty fishy enemy"""
    def __init__(self):
        self.name = 'Fishman'
        self.description = 'He breathes water, has 5 rows of sharp teeth,\
and shoots at you with his ray gun'
        self.hp = 15
        self.hpMAX = 15
        self.armour = 3
        self.damage = 5


class RoboMammoth(enemy):
    """Attacks twice in a row"""
    def __init__(self):
        self.name = 'Robo Mammoth'
        self.description = 'It shoots exploding bullets AND charges with its horns?\
Thats not fair'
        self.hp = 37
        self.hpMAX = 37
        self.armour = 17
        self.damage = 8
        self.ExtraDamage = 6


class CrazyRobotClown(enemy):
    """Killer Clown"""
    def __init__(self):
        self.name = 'Gong-go The Clown'
        self.description = 'He rides a tiny unicylce,\
and has an endless supply of bombs. Also he\'s a cyborg'
        self.hp = 21
        self.hpMAX = 21
        self.armour = 6
        self.damage = 10


class NervousChicken(enemy):
    """Boss Fight"""
    def __init__(self):
        self.name = 'Nervous Chicken'
        self.description = 'A Giant, robotic, T. Rex that is pure evil'
        self.hp = 50
        self.hpMAX = 50
        self.armour = 13
        self.damage = 26


class KarateZombie(enemy):
    """These are getting ridiculous"""
    def __init__(self):
        self.name = 'Karate Zombie'
        self.description = 'A decaying coprse capable of black-belt karate.\
It also has power saws for hands'
        self.hp = 17
        self.hpMAX = 17
        self.armour = 8
        self.damage = 7


class BloodyXyloid(enemy):
    """These are getting ridiculous"""
    def __init__(self):
        self.name = 'Bloody Xyloid'
        self.description = 'A lovecraftian horror of a creature.\
It has 913 tentacles and 13 mouths, all with 103 teeth.\
It is also small enough to fit in a purse.'
        self.hp = 15
        self.hpMAX = 15
        self.armour = 6
        self.damage = 4


class Gnash(enemy):
    """These are getting ridiculous"""
    def __init__(self):
        self.name = 'G\'Nash'
        self.description = 'A squat, but aggresive alien'
        self.hp = 9
        self.hpMAX = 9
        self.armour = 4
        self.damage = 3


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

    elif enemy == 'BrainSucker':
        combat_enemy = BrainSucker()

    elif enemy == 'Cyberwolf':
        combat_enemy = Cyberwolf()

    elif enemy == 'ChainSawManiac':
        combat_enemy = ChainSawManiac()
    
    elif enemy == 'ExplodingMushroom':
        combat_enemy = ExplodingMushroom()

    elif enemy == 'Fishman':
        combat_enemy = Fishman()

    elif enemy == 'RoboMammoth':
        combat_enemy = RoboMammoth()

    elif enemy == 'CrazyRobotClown':
        combat_enemy = CrazyRobotClown()

    elif enemy == 'NervousChicken':
        combat_enemy = NervousChicken()

    elif enemy == 'KarateZombie':
        combat_enemy = KarateZombie()

    elif enemy == 'GiantKillerLeech':
        combat_enemy = GiantKillerLeech()

    elif enemy == 'BloodyXyloid':
        combat_enemy = BloodyXyloid()

    elif enemy == 'Gnash':
        combat_enemy = Gnash()

    print(f'There is a {combat_enemy.name} here!')
    print('What would you like to do?')
    while monster_defeated == False:
        combat_choice = input('Kill, Examine\n')
        if combat_choice.lower() == 'kill':
            print('You have killed the monster!')
            monster_defeated = True
        elif combat_choice.lower() == 'examine':
            print(combat_enemy.description)
