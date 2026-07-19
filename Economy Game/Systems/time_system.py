'''
Preface: This file includes an important function that manages different elements of the game as time progresses.

Author: TheEmojiNinja
'''

# Import required modules
import Systems.economy_system as e, Systems.Development.factory_development as factory_development, Systems.Development.mine_development as mine_development, Systems.Development.sawmill_development as sawmill_development, Systems.Development.refinery_development as refinery_development, Systems.Development.infrastructure_development as infrastructure_development
import Systems.raw_resource_system as raw_resource, Systems.refined_resource_system as refined_resource, Systems.Events.event_system as ev, Data.game_data as g, random, time

# The updateDay method simply computes the day's resource outputs and consumption before progressing to another day.
def updateDay(game_object : g.GameData):

    # Subtract coal deposits dependent on number of factories to simulate coal consumption
    total_factories = d.getTotalFactoryOutput(game_object)
    used_coal = total_factories*random.randint(10, 25)

    # Add the day's worth of economic output to total currency if there is sufficient coal
    if r.getCoalQuantity(game_object) > used_coal:
        profit = total_factories*random.randint(10, 20)
        e.addProfitToCurrency(game_object, profit)
        r.subtractFromCoalQuantity(game_object, used_coal)
    else:
        print("Cannot continue factory production due to shortage of coal!")    

    if game_object.day % 30 == 0 and game_object.day != 0:
        e.payDebt(game_object)
    
    # Generate a random event and execute it
    event, province = ev.generateRandomEvent(game_object)
    #time.sleep(0.2)
    event = ev.getEventMessageAndExecuteEvent(game_object, event, province)

    ev.addToEventHistory(game_object, event)

    #time.sleep(0.2)
    
    # Progress the day
    game_object.day += 1

# Progress the construction of factories, mines, sawmills and infrastructure
def updateBuildingsInConstruction(game_object : g.GameData) -> None:
    factory_development.updateFactoriesInConstruction(game_object)
    mine_development.updateMinesInConstruction(game_object)
    sawmill_development.updateSawmillsInConstruction(game_object)
    refinery_development.updateRefineriesInConstruction(game_object)
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
    
    for province in province_list:
        if province.getSteelProductionStatus():
            obtained_steel += refined_resource.calculateSteelOutput(game_object)*factory_development.getTotalFactoryOutput(game_object)
        if province.getFuelProductionStatus():
            obtained_fuel += refined_resource.calculateFuelOutput(game_object)
        if province.getWoodProductionStatus():
            obtained_wood += refined_resource.calculateWoodOutput()*sawmill_development.getTotalLumberOutputForTimber(game_object)

    refined_resource.addToSteelQuantity(game_object, obtained_steel)
    refined_resource.addToFuelQuantity(game_object, obtained_fuel)
    refined_resource.addToWoodQuantity(game_object, obtained_wood)