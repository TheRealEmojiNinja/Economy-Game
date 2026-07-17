'''
Preface: This file contains all events that correlate to disasters.

Author: TheEmojiNinja
'''

# Import required modules
import random, Data.game_data as g, Models.province as p, Systems.economy_system as e

def doElectricalOutageEvent(game_object : g.GameData, province : p.Province) -> None:
    if province.getFactories() < 1 or province.getOutageStatus() == True:
        return None
    days = random.randint(2, 7)
    province.updateOutageStatus(True)
    province.updateOutageTime(days+1)
    return random.choice(game_object.EVENT_DESCRIPTIONS["Electrical_Outage"]).format(province=province.getName(), days=days)

def doMineCollapseEvent(game_object : g.GameData, province : p.Province) -> None:
    if province.getMines() < 1:
        return None
    
    prob = 0.0

    match province.getInfrastructureLevel():
        case 0:
            prob = 1.0
        case 1:
            prob = 0.75
        case 2:
            prob = 0.5
        case 3:
            prob = 0.3
        case 4:
            prob = 0.15
        case 5:
            prob = 0.05
        case _:
            prob = 0
        
    if random.random() < prob:
        province.updateMines(-1)
        return random.choice(game_object.EVENT_DESCRIPTIONS["Mine_Collapse"]).format(province=province.getName(), deaths=random.randint(5, 65))

def doHeavyStormEvent(game_object : g.GameData, province : p.Province) -> None:
    storm_cost = random.randint(250, 500)
    if storm_cost < e.getCurrencyAmount(game_object):
        e.subtractCostFromCurrency(game_object, storm_cost)
        return random.choice(game_object.EVENT_DESCRIPTIONS["Heavy_Storm_Success"]).format(cost=storm_cost, province=province.getName())
    else:
        return random.choice(game_object.EVENT_DESCRIPTIONS["Heavy_Storm_Failure"]).format(cost=storm_cost, province=province.getName())

def doEmergencyEvent(game_object : g.GameData, province : p.Province) -> None:
    emergency_cost = random.randint(100, 350)
    if emergency_cost < e.getCurrencyAmount(game_object):
        e.subtractCostFromCurrency(game_object, emergency_cost)
        return random.choice(game_object.EVENT_DESCRIPTIONS["Emergency_Success"]).format(cost=emergency_cost, province=province.getName())
    else:
        return random.choice(game_object.EVENT_DESCRIPTIONS["Emergency_Failure"]).format(cost=emergency_cost, province=province.getName())
        # In the future when the satisfaction system is implemented, this block will also lower the satisfaction by a certain amount
        # for failing to deal with the emergency