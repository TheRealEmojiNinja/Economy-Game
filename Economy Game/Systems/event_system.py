'''
Preface: This file contains important functions that handle randomly generated events that can affect the player/gameplay,
either positively or negatively.

Author: TheEmojiNinja
'''

# Import required modules
import Data.game_data as g, Data.event_description as ed, Systems.economy_system as e, Systems.resource_system as r, Models.province as p, random

# Get a random event from the choices of events, also dependent upon their weights
def generateRandomEvent(game_object : g.GameData) -> str:
    province = random.choice(game_object.provinces)
    event = random.choices(game_object.EVENTS, game_object.EVENT_WEIGHTS, k=1)[0]
    return (event, province)

# Execute the effects of that event
def executeEvent(game_object : g.GameData, event : str, province : p.Province) -> None:
    match event:
        case "Mine Collapse":
            doMineCollapseEvent(province)
        case "Emergency":
            doEmergencyEvent(game_object, province)
        case "Extra Funds":
           doExtraFundsEvent(game_object, province)
        case "Festival":
            doFestivalEvent(game_object, province)
        case "Extra Ore Vein":
            doExtraOreVeinEvent(game_object, province)
        case "Global Market Forum":
            doGlobalMarketForumEvent()
        case "Heavy Storm":
            doHeavyStormEvent(game_object, province)
        case "Smuggling Bust":
            doSmugglingBustEvent(game_object, province)
        case "Corruption Bust":
            doCorruptionBustEvent(game_object)
        case "Factory Maintenance":
            doFactoryMaintenanceEvent(game_object, province)
        case "Infrastructure Repair":
            doInfrastructureRepairEvent(game_object, province)
        case "Foreign Aid":
            doForeignAidEvent(game_object)
        case "Electrical Outage":
            doElectricalOutageEvent(province)
        case "Global Tension":
            doGlobalTensionEvent()
        case "Nothing":
            pass

def doGlobalTensionEvent() -> None:
    print(random.choice(ed.EVENT_DESCRIPTION["Global_Tension"]))

def doElectricalOutageEvent(province : p.Province) -> None:
    if province.getFactories() < 1 or province.getOutageStatus() == True:
        return None
    days = random.randint(2, 7)
    province.updateOutageStatus(True)
    province.updateOutageTime(days+1)
    print(random.choice(ed.EVENT_DESCRIPTION["Electrical_Outage"]).format(province=province.getName(), days=days))
    

def doForeignAidEvent(game_object : g.GameData) -> None:
    resources = ["Coal", "Iron", "Stone"]
    resource_type = random.choice(resources)
    aid = random.randint(100, 400)

    if resource_type == 'Coal':
        r.addToCoalQuantity(game_object, aid)
    elif resource_type == 'Iron':
        r.addToIronQuantity(game_object, aid)
    elif resource_type == 'Stone':
        r.addToStoneQuantity(game_object, aid)

    print(random.choice(ed.EVENT_DESCRIPTION["Foreign_Aid"]).format(amount=aid, resource=resource_type.lower()))

def doInfrastructureRepairEvent(game_object : g.GameData, province : p.Province) -> None:
    if province.getInfrastructureLevel() < 1:
        return None
    repair_cost = random.randint(50, 150)
    if repair_cost < e.getCurrencyAmount(game_object):
        e.subtractCostFromCurrency(game_object, repair_cost)
        print(random.choice(ed.EVENT_DESCRIPTION["Infrastructure_Repair_Success"]).format(cost=repair_cost, province=province.getName()))
    else:
        province.updateInfrastructureLevel(-1)
        print(random.choice(ed.EVENT_DESCRIPTION["Infrastructure_Repair_Failure"]).format(cost=repair_cost, province=province.getName()))

def doFactoryMaintenanceEvent(game_object : g.GameData, province : p.Province) -> None:
    if province.getFactories() < 1:
        return None
    repair_cost = random.randint(50, 150)
    if repair_cost < e.getCurrencyAmount(game_object):
        e.subtractCostFromCurrency(game_object, repair_cost)
        print(random.choice(ed.EVENT_DESCRIPTION["Factory_Maintenance_Success"]).format(cost=repair_cost, province=province.getName()))
    else:
        province.updateFactories(-1)
        print(random.choice(ed.EVENT_DESCRIPTION["Factory_Maintenance_Failure"]).format(cost=repair_cost, province=province.getName()))

def doMineCollapseEvent(province : p.Province) -> None:
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
        print(random.choice(ed.EVENT_DESCRIPTION["Mine_Collapse"]).format(province=province.getName(), deaths=random.randint(5, 65)))

def doEmergencyEvent(game_object : g.GameData, province : p.Province) -> None:
    emergency_cost = random.randint(100, 350)
    if emergency_cost < e.getCurrencyAmount(game_object):
        e.subtractCostFromCurrency(game_object, emergency_cost)
        print(random.choice(ed.EVENT_DESCRIPTION["Emergency_Success"]).format(cost=emergency_cost, province=province.getName()))
    else:
        print(random.choice(ed.EVENT_DESCRIPTION["Emergency_Failure"]).format(cost=emergency_cost, province=province.getName()))
        # In the future when the satisfaction system is implemented, this block will also lower the satisfaction by a certain amount
        # for failing to deal with the emergency

def doExtraFundsEvent(game_object : g.GameData, province : p.Province) -> None:
    obtained_funds = random.randint(100, 300)
    e.addProfitToCurrency(game_object, obtained_funds)
    print(random.choice(ed.EVENT_DESCRIPTION["Extra_Funds"]).format(profit=obtained_funds, province=province.getName()))

def doFestivalEvent(game_object : g.GameData, province : p.Province) -> None:
    print(random.choice(ed.EVENT_DESCRIPTION["Festival"]).format(province=province.getName()))
    # In the future this will boost satisfaction

def doExtraOreVeinEvent(game_object : g.GameData, province : p.Province) -> None:
    resources = ["Coal", "Iron", "Stone"]
    resource_type = random.choice(resources)
    obtained_resource = random.randint(20, 120)

    if resource_type == 'Coal':
        r.addToCoalQuantity(game_object, obtained_resource)
    elif resource_type == 'Iron':
        r.addToIronQuantity(game_object, obtained_resource)
    elif resource_type == 'Stone':
        r.addToStoneQuantity(game_object, obtained_resource)

    print(random.choice(ed.EVENT_DESCRIPTION["Extra_Ore_Vein"]).format(resource=resource_type.lower(), amount=obtained_resource, province=province.getName()))

def doSmugglingBustEvent(game_object : g.GameData, province : p.Province) -> None:
    confiscated_assets = random.randint(300, 600)
    e.addProfitToCurrency(game_object, confiscated_assets)
    print(random.choice(ed.EVENT_DESCRIPTION["Smuggling_Bust"]).format(profit=confiscated_assets, province=province.getName()))

def doGlobalMarketForumEvent() -> None:
    print(random.choice(ed.EVENT_DESCRIPTION["Global_Market_Forum"]))

def doHeavyStormEvent(game_object : g.GameData, province : p.Province) -> None:
    storm_cost = random.randint(250, 500)
    if storm_cost < e.getCurrencyAmount(game_object):
        e.subtractCostFromCurrency(game_object, storm_cost)
        print(random.choice(ed.EVENT_DESCRIPTION["Heavy_Storm_Success"]).format(cost=storm_cost, province=province.getName()))
    else:
        print(random.choice(ed.EVENT_DESCRIPTION["Heavy_Storm_Failure"]).format(cost=storm_cost, province=province.getName()))

def doCorruptionBustEvent(game_object : g.GameData) -> None:
    resources = ["Coal", "Iron", "Stone"]
    resource_type = random.choice(resources)
    lost_resource = random.randint(50, 100)

    resource_amount = 0
    if resource_type == 'Coal':
        resource_amount = r.getCoalQuantity(game_object)
    elif resource_type == 'Iron':
        resource_amount = r.getIronQuantity(game_object)
    elif resource_type == 'Stone':
        resource_amount = r.getStoneQuantity(game_object)

    if lost_resource > resource_amount:
        return None
    else:
        if resource_type == 'Coal':
            r.subtractFromCoalQuantity(game_object, lost_resource)
        elif resource_type == 'Iron':
            r.subtractFromIronQuantity(game_object, lost_resource)
        elif resource_type == 'Stone':
            r.subtractFromStoneQuantity(game_object, lost_resource)
    
    obtained_funds = random.randint(200, 400)
    e.addProfitToCurrency(game_object, obtained_funds)
    print(random.choice(ed.EVENT_DESCRIPTION["Corruption_Bust"]).format(amount=lost_resource, resource=resource_type.lower(), profit=obtained_funds))

# Complete implementation of this method when working on version v.1.2.1
def generateRandomPopUp():
    pass