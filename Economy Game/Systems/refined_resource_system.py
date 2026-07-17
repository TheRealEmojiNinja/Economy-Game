'''
Preface: This file includes important functions regarding the resources used in the game: Coal, Iron and Stone.

Author: TheEmojiNinja
'''

# Import required modules
import random, Data.game_data as g

# Helper functions for the steel variable
def randomizeSteelQuantity(game_object : g.GameData) -> None:
    game_object.steel = random.randrange(45, 95)

def getSteelQuantity(game_object : g.GameData) -> int:
    return game_object.steel

def addToCoalQuantity(game_object : g.GameData, added_coal : int) -> None:
    game_object.coal += added_coal

def subtractFromCoalQuantity(game_object : g.GameData, subtracted_coal : int) -> None:
    game_object.coal -= subtracted_coal

def randomCoalOutput() -> int:
    return random.randint(10, 20)

# Helper functions for the iron variable
def randomizeIronQuantity(game_object : g.GameData) -> None:
    game_object.iron = random.randrange(10, 30)

def getIronQuantity(game_object : g.GameData) -> int:
    return game_object.iron

def addToIronQuantity(game_object : g.GameData, added_iron : int) -> None:
    game_object.iron += added_iron

def subtractFromIronQuantity(game_object : g.GameData, subtracted_iron : int) -> None:
    game_object.iron -= subtracted_iron

def randomIronOutput() -> int:
    return random.randint(5, 10)

# Helper functions for the stone variable
def randomizeStoneQuantity(game_object : g.GameData) -> None:
    game_object.stone = random.randrange(25, 55)

def getStoneQuantity(game_object : g.GameData) -> int:
    return game_object.stone

def addToStoneQuantity(game_object : g.GameData, added_stone : int) -> None:
    game_object.stone += added_stone

def subtractFromStoneQuantity(game_object : g.GameData, subtracted_stone : int) -> None:
    game_object.stone -= subtracted_stone

# Helper functions for the timber variable
def randomizeTimberQuantity(game_object : g.GameData) -> None:
    game_object.timber = random.randrange(50, 105)

def getTimberQuantity(game_object : g.GameData) -> int:
    return game_object.timber

def addToTimberQuantity(game_object : g.GameData, added_timber : int) -> None:
    game_object.timber += added_timber

def subtractFromTimberQuantity(game_object : g.GameData, subtracted_timber : int) -> None:
    game_object.timber -= subtracted_timber

# Helper functions for the copper variable
def randomizeCopperQuantity(game_object : g.GameData) -> None:
    game_object.copper = random.randrange(5, 25)

def getCopperQuantity(game_object : g.GameData) -> int:
    return game_object.copper

def addToCopperQuantity(game_object : g.GameData, added_copper : int) -> None:
    game_object.copper += added_copper

def subtractFromCopperQuantity(game_object : g.GameData, subtracted_copper : int) -> None:
    game_object.copper -= subtracted_copper

# Helper functions for the copper variable
def randomizeCopperQuantity(game_object : g.GameData) -> None:
    game_object.copper = random.randrange(5, 25)

def getCopperQuantity(game_object : g.GameData) -> int:
    return game_object.copper

def addToCopperQuantity(game_object : g.GameData, added_copper : int) -> None:
    game_object.copper += added_copper

def subtractFromCopperQuantity(game_object : g.GameData, subtracted_copper : int) -> None:
    game_object.copper -= subtracted_copper

def randomStoneOutput() -> int:
    return random.randint(5, 10)

# Function that randomizes the resource deposits
def randomizeResourceDeposits() -> list:
    resources = ['Iron', 'Coal', 'Stone']
    deposits = []
    num_deposits = random.randrange(1, 3)
    j = 0
    while (j < num_deposits):
        chosen_resource = random.choice(resources)
        resources.remove(chosen_resource)
        deposits.append(chosen_resource)
        j += 1
    return deposits