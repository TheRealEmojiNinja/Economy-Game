'''
Preface: This file contains important functions relating to the management of the overall economy and the economic costs
of constructing buildings. 

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

# Functions that randomize starting values for factories, mines and infrastructure level
def randomizeNumberOfFactories() -> int:
    return random.randrange(0, 2)

def randomizeNumberOfMines() -> int:
    return random.randrange(1, 3)

def randomizeInfrastructureLevel() -> int:
    return random.randrange(0, 2)

# Helper functions that return the cost and required resources for constructing factories and mines
def getCostOfFactory() -> int:
    return 250

def getRequiredIronOfFactory() -> int:
    return 500

def getCostOfMine() -> int:
    return 300

def getRequiredStoneOfFactory() -> int:
    return 500
