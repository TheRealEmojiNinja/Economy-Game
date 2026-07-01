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

# Helper functions for the debt variable
def randomizeDebtAmount(game_object : g.GameData) -> None:
    game_object.debt = random.randint(100000, 200000)

def getDebtAmount(game_object : g.GameData) -> int:
    return game_object.debt

def addCurrencyToDebt(game_object : g.GameData, amount : int) -> None:
    game_object.debt += amount

def subtractCurrencyFromDebt(game_object : g.GameData, amount : int) -> None:
    game_object.debt -= amount

# Functions that randomize starting values for factories, mines and infrastructure level
def randomizeNumberOfFactories() -> int:
    # og 0,2
    return random.randrange(1, 2)

def randomizeNumberOfMines() -> int:
    return random.randrange(1, 3)

def randomizeInfrastructureLevel() -> int:
    # og 0,2
    return random.randrange(1, 2)

# Helper functions that return the cost and required resources for constructing factories, mines and infrastructure level
def getCostOfFactory() -> int:
    return 250

def getRequiredIronOfFactory() -> int:
    # og 500
    return 50

def getCostOfMine() -> int:
    return 300

def getRequiredStoneOfMine() -> int:
    # og 500
    return 50

def getCostOfInfrastructure() -> int:
    return 350

def getRequiredStoneOfInfrastructure() -> int:
    # og 300
    return 30

def payDebt(game_object : g.GameData) -> None:
    amount_to_be_paid = random.randint(250, 500)

    if getCurrencyAmount(game_object) >= amount_to_be_paid and getDebtAmount(game_object) > amount_to_be_paid:
        subtractCostFromCurrency(game_object, amount_to_be_paid)
        subtractCurrencyFromDebt(game_object, amount_to_be_paid)
        print(f"Debt for this month was successfully paid, totalling {amount_to_be_paid} currency!")
    elif getCurrencyAmount(game_object) >= amount_to_be_paid and getDebtAmount(game_object) <= amount_to_be_paid:
        amount_to_be_paid = getDebtAmount(game_object)
        subtractCostFromCurrency(amount_to_be_paid)
        subtractCurrencyFromDebt(amount_to_be_paid)
        print(f"Debt for this month was successfully paid, totalling {amount_to_be_paid} currency!")
    elif getCurrencyAmount(game_object) < amount_to_be_paid:
        print(f"Debt for this month was not paid! Our government failed to pay {amount_to_be_paid} currency.")
    
def getTotalFactories(game_object : g.GameData) -> int:
    total = 0
    for province in game_object.provinces:
        total += province.getFactories()
    return total

def getTotalMines(game_object : g.GameData) -> int:
    total = 0
    for province in game_object.provinces:
        total += province.getMines()
    return total
