'''
Preface: This file contains important functions that handle randomly generated events that can affect the player/gameplay,
either positively or negatively.

Author: TheEmojiNinja
'''

# Import required modules
import Data.game_data as g, Systems.economy_system as e, Systems.resource_system as r, random

# Get a random event from the choices of events, also dependent upon their weights
def generateRandomEvent(game_object : g.GameData) -> str:
    return random.choices(game_object.EVENTS, game_object.EVENT_WEIGHTS, k=1)[0]

# Execute the effects of that event
def executeEvent(game_object : g.GameData, event : str) -> None:
    match event:
        case "Mine Collapse":
            province = random.choice(game_object.provinces)
            if province.getMines() > 0:
                province.updateMines(-1)
                print(f"Oh no! A mine has collapsed in {province.getName()}!")
        case "Emergency":
            emergency_cost = random.randint(100, 200)
            e.subtractCostFromCurrency(game_object, emergency_cost)
            print(f"The government was forced to use {emergency_cost} currency to deal with a small emergency.")
        case "Extra Funds":
            obtained_funds = random.randint(100, 300)
            e.addProfitToCurrency(game_object, obtained_funds)
            print(f"We have searched every coffer and managed to scrape together an extra {obtained_funds} currency!")
        case "Corruption Bust":
            lost_coal = random.randint(50, 100)
            obtained_funds = random.randint(200, 400)
            r.subtractFromCoalQuantity(game_object, lost_coal)
            print(f"A corrupt politician was caught smuggling {lost_coal} coal! They have been forced to pay compensations of {obtained_funds} currency!")
            print(f"")
        case "Nothing":
            pass

# Complete implementation of this method when working on version v.1.2.1
def generateRandomPopUp():
    pass