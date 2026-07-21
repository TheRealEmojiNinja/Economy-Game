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

# Functions that randomize starting values for factories, mines, sawmills, refineries and infrastructure level
def randomizeNumberOfFactories() -> int:
    return random.randrange(0, 2)

def randomizeNumberOfMines() -> int:
    return random.randrange(1, 3)

def randomizeNumberOfSawmills() -> int:
    return random.randrange(1, 3)

def randomizeNumberOfRefineries() -> int:
    return random.randrange(0, 2)

def randomizeNumberOfCementPlants() -> int:
    return random.randrange(1, 2)

def randomizeInfrastructureLevel() -> int:
    return random.randrange(0, 2)

# Helper functions that return the cost and required resources for constructing factories, mines and infrastructure level
def getRequirementsOfFactoryConstruction() -> tuple[int, int, int, int]:
    COST_OF_FACTORY = 1000
    REQUIRED_CEMENT_FOR_FACTORY = 600
    REQUIRED_IRON_FOR_FACTORY = 350
    REQUIRED_COPPER_FOR_FACTORY = 200
    return (COST_OF_FACTORY, REQUIRED_CEMENT_FOR_FACTORY, REQUIRED_IRON_FOR_FACTORY, REQUIRED_COPPER_FOR_FACTORY)

def getRequirementsOfMineConstruction() -> tuple[int, int]:
    COST_OF_MINE = 600
    REQUIRED_WOOD_FOR_MINE = 450
    return (COST_OF_MINE, REQUIRED_WOOD_FOR_MINE)

def getRequirementsOfSawmillConstruction() -> tuple[int, int, int]:
    COST_OF_SAWMILL = 450
    REQUIRED_CEMENT_FOR_SAWMILL = 300
    REQUIRED_WOOD_FOR_SAWMILL = 100
    return (COST_OF_SAWMILL, REQUIRED_CEMENT_FOR_SAWMILL, REQUIRED_WOOD_FOR_SAWMILL)

def getRequirementsOfRefineryConstruction() -> tuple[int, int, int]:
    COST_OF_REFINERY = 750
    REQUIRED_IRON_FOR_REFINERY = 250
    REQUIRED_COPPER_FOR_REFINERY = 100
    return (COST_OF_REFINERY, REQUIRED_IRON_FOR_REFINERY, REQUIRED_COPPER_FOR_REFINERY)

def getRequirementsOfCementPlantConstruction() -> tuple[int, int, int]:
    COST_OF_CEMENT_PLANT = 600
    REQUIRED_CEMENT_FOR_CEMENT_PLANT = 200
    REQUIRED_WOOD_FOR_CEMENT_PLANT = 200
    return (COST_OF_CEMENT_PLANT, REQUIRED_CEMENT_FOR_CEMENT_PLANT, REQUIRED_WOOD_FOR_CEMENT_PLANT)

def getRequirementsOfInfrastructureConstruction() -> tuple[int, int, int]:
    COST_OF_INFRASTRUCTURE = 350
    REQUIRED_CEMENT_FOR_INFRASTRUCTURE = 300
    REQUIRED_WOOD_FOR_INFRASTRUCTURE = 200
    return (COST_OF_INFRASTRUCTURE, REQUIRED_CEMENT_FOR_INFRASTRUCTURE, REQUIRED_WOOD_FOR_INFRASTRUCTURE)

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