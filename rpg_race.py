def create_rpg_race(id, list_race):
    dict_rpg_races = {
        id: list_race
    }
    with open("rpg_race.txt", "at") as rpg_races:
        print(f'{dict_rpg_races}', file=rpg_races)