'''
Preface: This file includes important functions regarding the resources used in the game: Coal, Iron and Stone.

Author: TheEmojiNinja
'''

# Import required modules
import random, Data.game_data as g

# Helper functions for the coal variable
def randomizeCoalQuantity(game_object : g.GameData) -> None:
    game_object.coal = random.randrange(1000, 2000)

def getCoalQuantity(game_object : g.GameData) -> int:
    return game_object.coal

def addToCoalQuantity(game_object : g.GameData, added_coal : int) -> None:
    game_object.coal += added_coal

def subtractFromCoalQuantity(game_object : g.GameData, subtracted_coal : int) -> None:
    game_object.coal -= subtracted_coal

# Helper functions for the iron variable
def randomizeIronQuantity(game_object : g.GameData) -> None:
    game_object.iron = random.randrange(10, 30)

def getIronQuantity(game_object : g.GameData) -> int:
    return game_object.iron

def addToIronQuantity(game_object : g.GameData, added_iron : int) -> None:
    game_object.iron += added_iron

def subtractFromIronQuantity(game_object : g.GameData, subtracted_iron : int) -> None:
    game_object.iron -= subtracted_iron

# Helper functions for the stone variable
def randomizeStoneQuantity(game_object : g.GameData) -> None:
    game_object.stone = random.randrange(25, 55)

def getStoneQuantity(game_object : g.GameData) -> int:
    return game_object.stone

def addToStoneQuantity(game_object : g.GameData, added_stone : int) -> None:
    game_object.stone += added_stone

def subtractFromStoneQuantity(game_object : g.GameData, subtracted_stone : int) -> None:
    game_object.stone -= subtracted_stone

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