'''
Preface: This file includes an important function that manages different elements of the game as time progresses.

Author: TheEmojiNinja
'''

# Import required modules
import Systems.economy_system as economy, Systems.Development.factory_development as factory_development, Systems.Development.mine_development as mine_development, Systems.Development.sawmill_development as sawmill_development, Systems.Development.refinery_development as refinery_development, Systems.Development.cement_plant_development as cement_plant_development, Systems.Development.infrastructure_development as infrastructure_development
import Systems.Resource.raw_resource_system as raw_resource, Systems.Resource.refined_resource_system as refined_resource, Systems.Events.event_system as ev, Data.game_data as g, random, time

# The updateDay method simply computes the day's resource outputs and consumption before progressing to another day.
def updateProgression(game_object : g.GameData) -> None:
    progressDate(game_object)
    updateBuildingsInConstruction(game_object)
    updateRawResourceGains(game_object)
    updateRefinedResourceGains(game_object)
    throwRandomEvent(game_object)

def progressDate(game_object : g.GameData) -> None:
    
    month = game_object.date[0]
    day = game_object.date[1]
    year = game_object.date[2]

    match month:
        case 1:
            if day != 31:
                day += 1
            else:
                day = 1
                month += 1
        case 2:
            if day != 28:
                day += 1
            else:
                day = 1
                month += 1
        case 3:
            if day != 31:
                day += 1
            else:
                day = 1
                month += 1
        case 4:
            if day != 30:
                day += 1
            else:
                day = 1
                month += 1
        case 5:
            if day != 31:
                day += 1
            else:
                day = 1
                month += 1
        case 6:
            if day != 30:
                day += 1
            else:
                day = 1
                month += 1
        case 7:
            if day != 31:
                day += 1
            else:
                day = 1
                month += 1
        case 8:
            if day != 31:
                day += 1
            else:
                day = 1
                month += 1
        case 9:
            if day != 30:
                day += 1
            else:
                day = 1
                month += 1
        case 10:
            if day != 31:
                day += 1
            else:
                day = 1
                month += 1
        case 11:
            if day != 30:
                day += 1
            else:
                day = 1
                month += 1
        case 12:
            if day != 31:
                day += 1
            else:
                day = 1
                month = 1
                year += 1

    game_object.date[0] = month
    game_object.date[1] = day
    game_object.date[2] = year

# Progress the construction of factories, mines, sawmills and infrastructure
def updateBuildingsInConstruction(game_object : g.GameData) -> None:
    factory_development.updateFactoriesInConstruction(game_object)
    mine_development.updateMinesInConstruction(game_object)
    sawmill_development.updateSawmillsInConstruction(game_object)
    refinery_development.updateRefineriesInConstruction(game_object)
    cement_plant_development.updateCementPlantsInConstruction(game_object)
    infrastructure_development.updateInfrastructureInConstruction(game_object)

def updateRawResourceGains(game_object : g.GameData) -> None:
    obtained_coal = mine_development.getTotalMiningOutputForCoal(game_object)*raw_resource.randomCoalOutput()
    raw_resource.addToCoalQuantity(game_object, obtained_coal)

    obtained_iron = mine_development.getTotalMiningOutputForIron(game_object)*raw_resource.randomIronOutput()
    raw_resource.addToIronQuantity(game_object, obtained_iron)
    
    obtained_stone = mine_development.getTotalMiningOutputForStone(game_object)*raw_resource.randomStoneOutput()
    raw_resource.addToStoneQuantity(game_object, obtained_stone)

    obtained_copper = mine_development.getTotalMiningOutputForCopper(game_object)*raw_resource.randomCopperOutput()
    raw_resource.addToCopperQuantity(game_object, obtained_copper)

    obtained_timber = sawmill_development.getTotalLumberOutputForTimber(game_object)*raw_resource.randomTimberOutput()
    raw_resource.addToTimberQuantity(game_object, obtained_timber)

def updateRefinedResourceGains(game_object : g.GameData) -> None:
    province_list = game_object.provinces
    obtained_steel = 0
    obtained_fuel = 0
    obtained_wood = 0
    obtained_cement = 0
    
    for province in province_list:
        if province.getSteelProductionStatus():
            obtained_steel += refined_resource.calculateSteelOutput(game_object)*factory_development.getTotalFactoryOutput(game_object)
        if province.getFuelProductionStatus():
            obtained_fuel += refined_resource.calculateFuelOutput(game_object)
        if province.getWoodProductionStatus():
            obtained_wood += refined_resource.calculateWoodOutput(game_object)*sawmill_development.getTotalLumberOutputForTimber(game_object)

    obtained_cement += refined_resource.calculateCementOutput(game_object)*cement_plant_development.getTotalCementPlantOutput(game_object)

    refined_resource.addToSteelQuantity(game_object, obtained_steel)
    refined_resource.addToFuelQuantity(game_object, obtained_fuel)
    refined_resource.addToWoodQuantity(game_object, obtained_wood) 
    refined_resource.addToCementQuantity(game_object, obtained_cement)

def throwRandomEvent(game_object : g.GameData):
    event, province = ev.generateRandomEvent(game_object)
    executed_event = ev.getEventMessageAndExecuteEvent(game_object, event, province)
    ev.addToEventHistory(game_object, executed_event)

def updateDebt(game_object : g.GameData) -> None:
    if game_object.day % 30 == 0 and game_object.day != 0:
        economy.payDebt(game_object)