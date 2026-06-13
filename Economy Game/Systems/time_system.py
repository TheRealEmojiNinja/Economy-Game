'''
Preface: This file includes an important function that manages different elements of the game as time progresses.

Author: TheEmojiNinja
'''

# Import required modules
import Systems.economy_system as e, Systems.development_systems as d, Systems.resource_system as r, Systems.event_system as ev, Data.game_data as g, random

# The updateDay method simply computes the day's resource outputs and consumption before progressing to another day.
def updateDay(game_object : g.GameData):

    # Progress the construction of factories, mines and infrastructure
    d.updateFactoriesInConstruction(game_object)
    d.updateMinesInConstruction(game_object)
    d.updateInfrastructureInConstruction(game_object)

    # Add the day's worth of coal to total stocks
    obtained_coal = d.getTotalMiningOutputForCoal(game_object)*random.randint(10, 20)
    r.addToCoalQuantity(game_object, obtained_coal)

    # Add the day's worth of iron to total stocks
    obtained_iron = d.getTotalMiningOutputForIron(game_object)*random.randint(5, 10)
    r.addToIronQuantity(game_object, obtained_iron)

    # Add the day's worth of stone to total stocks
    obtained_stone = d.getTotalMiningOutputForStone(game_object)*random.randint(5, 10)
    r.addToStoneQuantity(game_object, obtained_stone)

    # Subtract coal deposits dependent on number of factories to simulate coal consumption
    total_factories = 0
    for province in game_object.provinces:
        total_factories += province.getFactories()
    used_coal = total_factories*random.randint(50, 101)

    # Add the day's worth of economic output to total currency if there is sufficient coal
    if game_object.coal > used_coal:
        profit = d.getTotalFactoryOutput(game_object)*10
        e.addProfitToCurrency(game_object, profit)
        r.subtractFromCoalQuantity(game_object, used_coal)
    else:
        print("Cannot continue factory production due to shortage of coal!")    
    
    ev.executeEvent(game_object, ev.generateRandomEvent(game_object))
    
    # Progress the day
    game_object.day += 1