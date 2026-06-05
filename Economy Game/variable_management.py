'''
Preface: This file contains important functions relating to some of the changeable variables outlined in key_variables.py.

Author: TheEmojiNinja
'''

# Required modules
import random
from key_variables import currency, resources, coal, iron, stone, day

# Helper functions for the currency variable
def randomizeCurrencyAmount() -> None:
    global currency
    currency = random.randrange(500, 1500)

def getCurrencyAmount() -> int:
    global currency
    return currency

def addProfitToCurrency(profit : int) -> None:
    global currency
    currency += profit

def subtractCostFromCurrency(cost : int) -> None:
    global currency
    currency -= cost

# Helper functions for the coal variable
def randomizeCoalQuantity() -> None:
    global coal
    coal = random.randrange(1000, 2000)

def getCoalQuantity() -> int:
    global coal
    return coal

def addToCoalQuantity(added_coal : int) -> None:
    global coal
    coal += added_coal

def subtractFromCoalQuantity(subtracted_coal : int) -> None:
    global coal
    coal -= subtracted_coal

# Helper functions for the iron variable
def randomizeIronQuantity() -> None:
    global iron
    iron = random.randrange(10, 30)

def getIronQuantity() -> int:
    global iron
    return iron

def addToIronQuantity(added_iron : int) -> None:
    global iron
    iron += added_iron

def subtractFromIronQuantity(subtracted_iron : int) -> None:
    global iron
    iron -= subtracted_iron

# Helper functions for the stone variable
def randomizeStoneQuantity() -> None:
    global stone
    stone = random.randrange(25, 55)

def getStoneQuantity() -> int:
    global stone
    return stone

def addToStoneQuantity(added_stone : int) -> None:
    global stone
    stone += added_stone

def subtractFromStoneQuantity(subtracted_stone : int) -> None:
    global stone
    stone -= subtracted_stone


def randomizeNumberOfFactories() -> int:
    return random.randrange(0, 4)

def randomizeNumberOfMines() -> int:
    return random.randrange(2, 5)

def randomizeInfrastructureLevel() -> int:
    return random.randrange(0, 2)

def randomizeResourceDeposits() -> list:
    global resources
    deposits = []
    num_deposits = random.randrange(1, 3)
    j = 0
    while (j < num_deposits):
        deposits.append(random.choice(resources))
        j += 1
    return deposits
    
