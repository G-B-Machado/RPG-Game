import json
from rpg_class import create_rpg_class#, search_rpg_class
from rpg_race import create_rpg_race

def create_character(name, rpg_class, rpg_race):
    #print(search_rpg_class(rpg_class))
    disc_character = {
        0: [name, rpg_class, rpg_race]}

    with open("rpg_character.json", "a") as rpg_characters:
        json.dump(disc_character, rpg_characters, indent=4)
        #print(f'{disc_character}', file=rpg_characters)

    return disc_character