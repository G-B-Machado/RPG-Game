import json

def create_rpg_class(id, list_class):
    dict_rpg_classes = {
        id: list_class
    }
    with open("rpg_class.json", "a") as rpg_classes:
        json.dump(dict_rpg_classes, rpg_classes, indent=4)