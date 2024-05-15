import json
def create_rpg_race(id, list_race):
    dict_rpg_races = {
        id: list_race
    }
    with open("rpg_race.json", "a") as rpg_races:
        json.dump(dict_rpg_races, rpg_races, indent=4)