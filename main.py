from rpg_character import create_character
from rpg_class import create_rpg_class
from rpg_race import create_rpg_race

def increase_id(id):
    id +=1
    return id

def main():

    print("For this programa, you input 1 for yes and 2 for no")

    rpg_class_condition = input("Do you want create a new class or use an existing? ")
    if rpg_class_condition == "1":
        create_rpg_class(input("Name of your class: "), ["skills", "abilities"])
    else:
        rpg_class = input("Input the name of your class: ")

    rpg_race_condition = input("Do you want create a new race or use an existing? ")
    if rpg_race_condition == "1":
        create_rpg_race(input("Name of your race: "), ["skills", "abilities"])
    else:
        rpg_race = input("Input the name of your race: ")

    name = input("What is your character name? ")
2
create_character(name, rpg_class, rpg_race)

main()
