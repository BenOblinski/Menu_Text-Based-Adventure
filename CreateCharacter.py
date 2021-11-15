# Course: CS 30
# Period: 3
# Date created: 20/9/2021
# Date last modified: 11/14/2021
# Name: Ben Oblinski
# Description: Character creation system for a text-based RPG game

# Dictonary that holds all of the classes a play can play as and their stats
Description = "Description"
classes = {"heavy": {Description: "A slow, but tough fighter",
                     "Health": 160,
                     "Attack": 35,
                     "Defense": 25},
           "footsoldier":
                    {Description: "A quick and agile, but \
weak, gunfighter",
                     "Health": 100,
                     "Attack": 30,
                     "Defense": 20},
           "sniper":
                    {Description: "Heavy attack, but weak and slow",
                     "Health": 110,
                     "Attack": 45,
                     "Defense": 35},
           "marine":
                    {Description: "A well rounded class with no \
specific advatages or disadvantages",
                     "Health": 115,
                     "Attack": 30,
                     "Defense": 30}}


# Player character class
class character:
    def __init__(self, health, attack, defense):
        self.health = health
        self.attack = attack
        self.defense = defense

character1 = character
character1.health = 0
character1.attack = 0
character1.defense = 0


# Prints a preview about each of the classes
def ClassMenuDemo():
    for people in classes:
        print(f"{people} - {classes[people][Description]}")


# Menu allows players to choose a name and class
def CharacterCreationMenu():
    a = 1
    filename1 = 'CharacterName.txt'
    nameChoice = input("name your character\n")
    with open(filename1, 'w') as NameFile:
        NameFile.write(nameChoice)
        print("\nname confirmed")
        print("please choose a class")

    # This block shows the player the classes they can play as
    ClassMenuDemo()

    # Allows the player to choose a class to play as
    while a == 1:
        filename2 = 'CharacterClass.txt'
        x = str(input("\nChoose a Class\n"))
        classChoice = x.lower()
        if classChoice == 'heavy':
            a = 2
        elif classChoice == 'footsoldier':
            a = 2
        elif classChoice == 'marine':
            a = 2
        elif classChoice == 'sniper':
            a = 2
        else:
            print("typo, please type again")
    with open(filename2, 'w') as ClassFile:
            ClassFile.write(classChoice)
    print("class confirmed\n")

    # This block lets the player review their selections
    print("your character")
    name = open('CharacterName.txt', 'r')
    nameText = name.read()
    name.close()
    print(f"Name: {nameText}")
    printChosenClass()
    print('\n')


# Creates a character with the qualities specified by the player
def printChosenClass():
    x = open('CharacterClass.txt', 'r')
    classChoice = str(x.read())
    x.close()
    character1 = character
    character1.health = classes[classChoice]["Health"]
    character1.attack = classes[classChoice]["Attack"]
    character1.defense = classes[classChoice]["Defense"]
    character1.location = 'a1'
    print(f"Class: {classChoice}")
    print(f"Health: {character1.health}")
    print(f"Attack: {character1.attack}")
    print(f"Defense: {character1.defense}")
    print("☠-----☠-----☠-----☠-----☠-----☠")
