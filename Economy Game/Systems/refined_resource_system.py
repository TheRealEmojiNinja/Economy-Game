'''
Preface: This file includes important functions regarding the resources used in the game: Coal, Iron and Stone.

Author: TheEmojiNinja
'''

# Import required modules
import random, Data.game_data as g, Systems.raw_resource_system as raw_resource, Systems.economy_system as economy, Systems.refined_resource_system as refined_resource

# Helper functions for the steel variable
def randomizeSteelQuantity(game_object : g.GameData) -> None:
    game_object.steel = random.randrange(45, 95)

def getSteelQuantity(game_object : g.GameData) -> int:
    return game_object.steel

def addToSteelQuantity(game_object : g.GameData, added_steel : int) -> None:
    game_object.steel += added_steel

def subtractFromSteelQuantity(game_object : g.GameData, subtracted_steel : int) -> None:
    game_object.steel -= subtracted_steel

def calculateSteelOutput(game_object : g.GameData) -> int:
    IRON_REQUIREMENTS = 10
    FUEL_REQUIREMENTS = 1
    PRODUCED_STEEL = 2

    if raw_resource.getIronQuantity(game_object) > IRON_REQUIREMENTS and refined_resource.getFuelQuantity(game_object) > FUEL_REQUIREMENTS:
        raw_resource.subtractFromIronQuantity(game_object, IRON_REQUIREMENTS)
        refined_resource.subtractFromFuelQuantity(game_object, FUEL_REQUIREMENTS)
        return PRODUCED_STEEL
    else:
        return 0

# Helper functions for the fuel variable
def randomizeFuelQuantity(game_object : g.GameData) -> None:
    game_object.fuel = random.randrange(10, 30)

def getFuelQuantity(game_object : g.GameData) -> int:
    return game_object.fuel

def addToFuelQuantity(game_object : g.GameData, added_fuel : int) -> None:
    game_object.fuel += added_fuel

def subtractFromFuelQuantity(game_object : g.GameData, subtracted_fuel : int) -> None:
    game_object.fuel -= subtracted_fuel

def calculateFuelOutput(game_object : g.GameData) -> int:
    COAL_REQUIREMENTS = 20
    PRODUCED_FUEL = 5

    if raw_resource.getCoalQuantity(game_object) > COAL_REQUIREMENTS:
        raw_resource.subtractFromCoalQuantity(COAL_REQUIREMENTS)
        return PRODUCED_FUEL
    else:
        return 0

# Helper functions for the wood variable
def randomizeWoodQuantity(game_object : g.GameData) -> None:
    game_object.wood = random.randrange(25, 55)

def getWoodQuantity(game_object : g.GameData) -> int:
    return game_object.wood

def addToWoodQuantity(game_object : g.GameData, added_wood : int) -> None:
    game_object.wood += added_wood

def subtractFromWoodQuantity(game_object : g.GameData, subtracted_wood : int) -> None:
    game_object.wood -= subtracted_wood

def calculateWoodOutput(game_object : g.GameData) -> int:
    TIMBER_REQUIREMENTS = 10
    PRODUCED_WOOD = 5

    if raw_resource.getTimberQuantity(game_object) > TIMBER_REQUIREMENTS:
        raw_resource.subtractFromTimberQuantity(TIMBER_REQUIREMENTS)
        return PRODUCED_WOOD
    else:
        return 0