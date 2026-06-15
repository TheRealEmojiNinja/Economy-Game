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

def loadEventsAndWeights() -> tuple[list, list]:
    events, weights, effects = [], [], []
    with open('Economy Game\Data\events.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            events.append(row["name"])
            weights.append(int(row["weight"]))
    return (events, weights)