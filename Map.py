# Course: CS 30
# Period: 3
# Date created: 20/9/2021
# Date last modified: 10/20/2021
# Name: Ben Oblinski
# Description: Menu system for a text-based RPG game
from numpy import*

decriptions = {"Tumbleweed":
               {"Description": "A dry, dying town \
in the middle of the desert"},
               "Rattlesnake farm":
               {"Desription": "An old cattle farm \
turned into a gang hideout by Jake \"The Snake\""},
               "Claymore": {"Desription": "A small, mostly abandoned settlment \
with houses made of clay"},
               "New Highlands":
                           {"Descrpition": "A new, classy town"},
               "Great Bear Falls":
                           {"Descrpition": "An enormous water fall\
that leads into the White water river"}}
# list of loactions around the world
# list can be accsessed by typing 'map'
# subdivisions of the map dictonary: location/places/about

location = array("""
+-----------+-----------+-----------+-----------+-----------+-----------+
|           |           |           |Great Bear |           |           |
|           |           |           |Falls      |           |           |
+-----------+-----------+-----------+-----------+-----------+-----------+
|           |Rattlesnake|           |           |           |New        |
|           |Farm       |           |           |           |Highlands  |
+-----------+-----------+-----------+-----------+-----------+-----------+
|           |           |           |           |           |           |
|           |           |           |           |           |           |
+-----------+-----------+-----------+-----------+-----------+-----------+
|           |           |Claymore   |           |           |           |
|           |           |           |           |           |           |
+-----------+-----------+-----------+-----------+-----------+-----------+
|Tumbleweed |           |           |           |           |           |
|           |           |           |           |           |           |
+-----------+-----------+-----------+-----------+-----------+-----------+
""")


def playerMap():
    # if the player wants to see the map...
    print("")
    print("☠-----☠-----MAP-----☠-----☠")
    print(location)
    for places in decriptions:
        print(places)
        for abouts in decriptions[places]:
            print(decriptions[places][abouts])
            print(" ")
    print("☠-----☠-----☠-----☠-----☠")
print("")
