'''
Preface: This file contains important functions that handle randomly generated events that can affect the player/gameplay,
either positively or negatively.

Author: TheEmojiNinja
'''

# Import required modules
import Data.game_data as g, Models.province as p, random
import Events.disaster_events as d, Events.economy_events as e, Events.law_events as l, Events.politics_events as p, Events.resource_events as r

# Get a random event from the choices of events, also dependent upon their weights
def generateRandomEvent(game_object : g.GameData) -> str:
    province = random.choice(game_object.provinces)
    event = random.choices(game_object.EVENTS, game_object.EVENT_WEIGHTS, k=1)[0]
    return (event, province)

# Execute the effects of that event
def executeEvent(game_object : g.GameData, event : str, province : p.Province) -> None:
    match event:
        case "Mine Collapse":
            d.doMineCollapseEvent(game_object, province)
        case "Emergency":
            d.doEmergencyEvent(game_object, province)
        case "Extra Funds":
           e.doExtraFundsEvent(game_object, province)
        case "Festival":
            p.doFestivalEvent(game_object, province)
        case "Extra Ore Vein":
            r.doExtraOreVeinEvent(game_object, province)
        case "Global Market Forum":
            e.doGlobalMarketForumEvent(game_object)
        case "Heavy Storm":
            d.doHeavyStormEvent(game_object, province)
        case "Smuggling Bust":
            l.doSmugglingBustEvent(game_object, province)
        case "Corruption Bust":
            l.doCorruptionBustEvent(game_object)
        case "Factory Maintenance":
            e.doFactoryMaintenanceEvent(game_object, province)
        case "Infrastructure Repair":
            e.doInfrastructureRepairEvent(game_object, province)
        case "Foreign Aid":
            r.doForeignAidEvent(game_object)
        case "Electrical Outage":
            d.doElectricalOutageEvent(game_object, province)
        case "Global Tension":
            p.doGlobalTensionEvent()
        case "Nothing":
            pass

# Complete implementation of this method when working on version v.1.2.1
def generateRandomPopUp():
    pass