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
    return random.randrange(1, 2)

def randomizeNumberOfMines() -> int:
    return random.randrange(1, 3)

def randomizeNumberOfSawmills() -> int:
    return random.randrange(1, 3)

def randomizeInfrastructureLevel() -> int:
    return random.randrange(1, 2)

# Helper functions that return the cost and required resources for constructing factories, mines and infrastructure level
def getRequirementsOfFactoryConstruction() -> tuple[int]:
    cost_of_factory = 1000
    required_stone_for_factory = 600
    required_iron_for_factory = 350
    required_copper_for_factory = 200
    return (cost_of_factory, required_stone_for_factory, required_iron_for_factory, required_copper_for_factory)

def getRequirementsOfMineConstruction() -> tuple[int]:
    cost_of_mine = 600
    required_wood_for_mine = 450
    return (cost_of_mine, required_wood_for_mine)

def getRequirementsOfSawmillConstruction() -> tuple[int]:
    cost_of_sawmill = 450
    required_stone_for_sawmill = 300
    required_wood_for_sawmill = 100
    return (cost_of_sawmill, required_stone_for_sawmill, required_wood_for_sawmill)

def getRequirementsOfInfrastructureConstruction() -> tuple[int]:
    cost_of_infrastructure = 350
    required_stone_for_infrastructure = 300
    required_wood_for_infrastructure = 200
    return (cost_of_infrastructure, required_stone_for_infrastructure, required_wood_for_infrastructure)

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
