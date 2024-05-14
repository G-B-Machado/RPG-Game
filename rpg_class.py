from random import Random, randrange

def create_rpg_class(id, list_class):
    dict_rpg_classes = {
        id: list_class
    }
    with open("rpg_class.txt", "at") as rpg_classes:
        print(f'{dict_rpg_classes}', file=rpg_classes)
"""
def search_rpg_class(id):
    with open("rpg_class.txt", "r") as rpg_classes:
        dict_rpg_classes = {}
        rpg_class = ''
        for line in rpg_classes:
            (key, val) = line.translate({ord('{'): None}).translate({ord('""'): None}).translate({ord('}'): None}).split(":")
            dict_rpg_classes[key] = val
        print(dict_rpg_classes)
        rpg_classes = rpg_classes.read()
        if id in rpg_classes:
           print('teste')
           rpg_class = rpg_classes[id]
    return rpg_class
"""