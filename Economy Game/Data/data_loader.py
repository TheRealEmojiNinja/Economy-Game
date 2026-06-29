'''
Preface: This file is used to load in data from .csv files to be used in game.

Author: TheEmojiNinja
'''

# Import required modules
import csv

# This method loads all province names from the province_names.csv file
def loadProvinceNames() -> list:
    province_names = []
    with open('Economy Game\Data\province_names.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            province_names.append(row["name"])
    return province_names

# This method loads all events and their weights from the events.csv file
def loadEventsAndWeights() -> tuple[list, list]:
    events, weights, effects = [], [], []
    with open('Economy Game\Data\events.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            events.append(row["name"])
            weights.append(int(row["weight"]))
    return (events, weights)

# This method loads all event descriptions from the event_descriptions.csv file
def loadEventDescriptions() -> dict[str, list]:
    event_descriptions = {}
    with open('Economy Game\Data\event_descriptions.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["event_type"] not in event_descriptions:
                event_descriptions[row["event_type"]] = []
                event_descriptions[row["event_type"]].append(row["description"])
            else:
                event_descriptions[row["event_type"]].append(row["description"])
    return event_descriptions