'''
Preface: This file includes an important function that manages different elements of the game as time progresses.

Author: TheEmojiNinja
'''

# Import required modules
import Systems.economy_system as e, Systems.development_systems as d, Systems.resource_system as r, Systems.Events.event_system as ev, Data.game_data as g, random, time

# The updateDay method simply computes the day's resource outputs and consumption before progressing to another day.
def updateDay(game_object : g.GameData):

    # Progress the construction of factories, mines and infrastructure
    d.updateFactoriesInConstruction(game_object)
    d.updateMinesInConstruction(game_object)
    d.updateInfrastructureInConstruction(game_object)

    # Add the day's worth of coal to total stocks
    obtained_coal = d.getTotalMiningOutputForCoal(game_object)*r.randomCoalOutput()
    r.addToCoalQuantity(game_object, obtained_coal)

    # Add the day's worth of iron to total stocks
    obtained_iron = d.getTotalMiningOutputForIron(game_object)*r.randomIronOutput()
    r.addToIronQuantity(game_object, obtained_iron)

    # Add the day's worth of stone to total stocks
    obtained_stone = d.getTotalMiningOutputForStone(game_object)*r.randomStoneOutput()
    r.addToStoneQuantity(game_object, obtained_stone)

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
    ev.executeEvent(game_object, event, province)

    #time.sleep(0.2)
    
    # Progress the day
    game_object.day += 1