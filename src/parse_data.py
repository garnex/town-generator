import json
import random

data_dir = "../data"
town_data = {}


json_files = {
    "culture": "town_culture.json",
    "defenses": "town_defenses.json",
    "districts": "town_districts.json",
    "exports": "town_exports.json",
    "geography": "town_geography.json",
    "government": "town_government.json",
    "historical": "town_historical.json",
    "landmarks": "town_landmarks.json",
    "law": "town_law_enforcement.json",
    "powerplayers": "town_powerplayers.json",
    "threats": "town_threats.json",
}

def read_town_data():
    for key, json_file in json_files.items():
        data = json.load(open(f"{data_dir}/{json_file}"))
        town_data[key] = data

def select_random_value(section):
    if section not in ["powerplayers", "exports"]:
        data = town_data[section]
        key = random.choice(list(data.keys()))
        value = random.choice(data[key])
        return value
    elif section == "powerplayers":
        data = town_data[section]
        key = random.choice(list(data.keys()))
        value_dict = random.choice(data[key])
        value = f"{value_dict['title']}\nmotivation: {value_dict['motivation']}\nagenda: {value_dict['agenda']}"
        return value
    else: # exports
        pass


def main():
    read_town_data()
    # Display in a semi-grouped order
    for section in ["geography", "culture", "exports", "government", "law", "defenses", "districts", "landmarks", "historical", "powerplayers", "threats"]:
         value = select_random_value(section)
         print(f"{section.capitalize()}: {value}\n")
         #print(f"{value}\n")
main()