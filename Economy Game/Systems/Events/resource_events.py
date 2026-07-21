'''
Preface: This file contains all events that correlate to resources.

Author: TheEmojiNinja
'''

# Import required modules
import random, Data.game_data as g, Models.province as p, Systems.Resource.raw_resource_system as raw_resource

def doExtraOreVeinEvent(game_object : g.GameData, province : p.Province) -> None:
    resources = ["Coal", "Iron", "Stone"]
    resource_type = random.choice(resources)
    obtained_resource = random.randint(20, 120)

    if resource_type == 'Coal':
        raw_resource.addToCoalQuantity(game_object, obtained_resource)
    elif resource_type == 'Iron':
        raw_resource.addToIronQuantity(game_object, obtained_resource)
    elif resource_type == 'Stone':
        raw_resource.addToStoneQuantity(game_object, obtained_resource)

    return random.choice(game_object.EVENT_DESCRIPTIONS["Extra_Ore_Vein"]).format(resource=resource_type.lower(), amount=obtained_resource, province=province.getName())

def doForeignAidEvent(game_object : g.GameData) -> None:
    resources = ["Coal", "Iron", "Stone"]
    resource_type = random.choice(resources)
    aid = random.randint(100, 400)

    if resource_type == 'Coal':
        raw_resource.addToCoalQuantity(game_object, aid)
    elif resource_type == 'Iron':
        raw_resource.addToIronQuantity(game_object, aid)
    elif resource_type == 'Stone':
        raw_resource.addToStoneQuantity(game_object, aid)

    return random.choice(game_object.EVENT_DESCRIPTIONS["Foreign_Aid"]).format(amount=aid, resource=resource_type.lower())