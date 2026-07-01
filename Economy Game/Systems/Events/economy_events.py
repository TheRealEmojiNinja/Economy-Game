'''
Preface: This file contains all events that correlate to the economy.

Author: TheEmojiNinja
'''

# Import required modules
import random, Data.game_data as g, Models.province as p, Systems.economy_system as e

def doInfrastructureRepairEvent(game_object : g.GameData, province : p.Province) -> None:
    if province.getInfrastructureLevel() < 1:
        return None
    repair_cost = random.randint(50, 150)
    if repair_cost < e.getCurrencyAmount(game_object):
        e.subtractCostFromCurrency(game_object, repair_cost)
        return random.choice(game_object.EVENT_DESCRIPTIONS["Infrastructure_Repair_Success"]).format(cost=repair_cost, province=province.getName())
    else:
        province.updateInfrastructureLevel(-1)
        return random.choice(game_object.EVENT_DESCRIPTIONS["Infrastructure_Repair_Failure"]).format(cost=repair_cost, province=province.getName())

def doFactoryMaintenanceEvent(game_object : g.GameData, province : p.Province) -> None:
    if province.getFactories() < 1:
        return None
    repair_cost = random.randint(50, 150)
    if repair_cost < e.getCurrencyAmount(game_object):
        e.subtractCostFromCurrency(game_object, repair_cost)
        return random.choice(game_object.EVENT_DESCRIPTIONS["Factory_Maintenance_Success"]).format(cost=repair_cost, province=province.getName())
    else:
        province.updateFactories(-1)
        return random.choice(game_object.EVENT_DESCRIPTIONS["Factory_Maintenance_Failure"]).format(cost=repair_cost, province=province.getName())

def doGlobalMarketForumEvent(game_object : g.GameData) -> None:
    return random.choice(game_object.EVENT_DESCRIPTIONS["Global_Market_Forum"])

def doExtraFundsEvent(game_object : g.GameData, province : p.Province) -> None:
    obtained_funds = random.randint(100, 300)
    e.addProfitToCurrency(game_object, obtained_funds)
    return random.choice(game_object.EVENT_DESCRIPTIONS["Extra_Funds"]).format(profit=obtained_funds, province=province.getName())