'''
Preface: This file contains all events that correlate to law enforcement.

Author: TheEmojiNinja
'''

# Import required modules
import random, Data.game_data as g, Models.province as p, Systems.economy_system as e, Systems.resource_system as r

def doSmugglingBustEvent(game_object : g.GameData, province : p.Province) -> None:
    confiscated_assets = random.randint(300, 600)
    e.addProfitToCurrency(game_object, confiscated_assets)
    print(random.choice(game_object.EVENT_DESCRIPTIONS["Smuggling_Bust"]).format(profit=confiscated_assets, province=province.getName()))

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
    print(random.choice(game_object.EVENT_DESCRIPTIONS["Corruption_Bust"]).format(amount=lost_resource, resource=resource_type.lower(), profit=obtained_funds))