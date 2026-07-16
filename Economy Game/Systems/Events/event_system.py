'''
Preface: This file contains important functions that handle randomly generated events that can affect the player/gameplay,
either positively or negatively.

Author: TheEmojiNinja
'''

# Import required modules
import Data.game_data as g, Models.province as p, random
import Systems.Events.disaster_events as d, Systems.Events.economy_events as e, Systems.Events.law_events as l, Systems.Events.politics_events as p, Systems.Events.resource_events as r

# Get a random event from the choices of events, also dependent upon their weights
def generateRandomEvent(game_object : g.GameData) -> str:
    province = random.choice(game_object.provinces)
    event = random.choices(game_object.EVENTS, game_object.EVENT_WEIGHTS, k=1)[0]
    return (event, province)

# Execute the effects of that event
def getEventMessageAndExecuteEvent(game_object : g.GameData, event : str, province : p.Province) -> str:
    match event:
        case "Mine Collapse":
            return d.doMineCollapseEvent(game_object, province)
        case "Emergency":
            return d.doEmergencyEvent(game_object, province)
        case "Extra Funds":
            return e.doExtraFundsEvent(game_object, province)
        case "Festival":
            return p.doFestivalEvent(game_object, province)
        case "Extra Ore Vein":
            return r.doExtraOreVeinEvent(game_object, province)
        case "Global Market Forum":
            return e.doGlobalMarketForumEvent(game_object)
        case "Heavy Storm":
            return d.doHeavyStormEvent(game_object, province)
        case "Smuggling Bust":
            return l.doSmugglingBustEvent(game_object, province)
        case "Corruption Bust":
            return l.doCorruptionBustEvent(game_object)
        case "Factory Maintenance":
            return e.doFactoryMaintenanceEvent(game_object, province)
        case "Infrastructure Repair":
            return e.doInfrastructureRepairEvent(game_object, province)
        case "Foreign Aid":
            return r.doForeignAidEvent(game_object)
        case "Electrical Outage":
            return d.doElectricalOutageEvent(game_object, province)
        case "Global Tension":
            return p.doGlobalTensionEvent(game_object)
        case "Nothing":
            return None

# Complete implementation of this method when working on version v.1.2.1
def generateRandomPopUp():
    pass

def getEventHistory(game_object : g.GameData):
    event_history = ''

    for event in game_object.event_history:
        event_history += event + '\n\n'
    
    return event_history

def addToEventHistory(game_object : g.GameData, event : str):

    if len(game_object.event_history) > 9:
        game_object.event_history.pop(0)
    if event != None:
        game_object.event_history.append(event)
