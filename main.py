from rpg_character import create_character
from rpg_class import create_rpg_class
from rpg_race import create_rpg_race

rpg_character_condition = 0
rpg_settings_condition = 0

def increase_id(id):
    id +=1
    return id

def main():

    print("For this programa, you input 1 for yes and 2 for no")

    rpg_settings_condition = input("Do you want change de settings? ")

    if rpg_settings_condition == "1":
        
        rpg_class_condition = input("Do you want create a new class1? ")
        if rpg_class_condition == "1":
            rpg_class_key = input("Name of your class: ")
            create_rpg_class(rpg_class_key, ["skills", "abilities"])

        rpg_race_condition = input("Do you want create a new race? ")
        if rpg_race_condition == "1":
            rpg_race_key = input("Name of your race: ")
            create_rpg_race(rpg_race_key, ["skills", "abilities"])

    rpg_character_condition = input("Do you want create a character? ")
    if rpg_character_condition == "1":
        name = input("Type your character name: ")
        rpg_class = input("Type your class name: ")
        rpg_race = input("Type your race name: ")

        print(create_character(name, rpg_class, rpg_race))

main()
