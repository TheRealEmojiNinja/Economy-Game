'''
Preface: This file contains important functions relating to some of the changeable variables outlined in key_variables.py.

Author: TheEmojiNinja
'''

# Required modules
import random, Data.game_data as g

# Helper functions for the currency variable
def randomizeCurrencyAmount(game_object : g.GameData) -> None:
    game_object.currency = random.randrange(500, 1500)

def getCurrencyAmount(game_object : g.GameData) -> int:
    return game_object.currency

def addProfitToCurrency(game_object : g.GameData, profit : int) -> None:
    game_object.currency += profit

def subtractCostFromCurrency(game_object : g.GameData, cost : int) -> None:
    game_object.currency -= cost

def randomizeNumberOfFactories() -> int:
    return random.randrange(0, 4)

def randomizeNumberOfMines() -> int:
    return random.randrange(2, 5)

def randomizeInfrastructureLevel() -> int:
    return random.randrange(0, 2)


    
