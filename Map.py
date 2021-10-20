# Course: CS 30
# Period: 3
# Date created: 20/9/2021
# Date last modified: 10/20/2021
# Name: Ben Oblinski
# Description: map system for the game menu
from numpy import*

descriptions = {"Tumbleweed":
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
    """ This function prints out the map of
    areas the player can go.
    Prints out the above map and the dictionary
    of disriptions of the places
    This function can be called by typing 'inv'
    """
    # if the player wants to see the map...
    print("\n☠-----☠-----MAP-----☠-----☠")
    print(location)
    for places in descriptions:
        print(places)
        for abouts in descriptions[places]:
            print(descriptions[places][abouts])
        print(" ")
    print("☠-----☠-----☠-----☠-----☠\n")
