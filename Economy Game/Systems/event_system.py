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
            if province.getMines() > 0:
                province.updateMines(-1)
                print(random.choice(ed.EVENT_DESCRIPTION["Mine_Collapse"]).format(province=province.getName(), deaths=random.randint(5, 65)))
        case "Emergency":
            emergency_cost = random.randint(100, 350)
            if emergency_cost < game_object.currency:
                e.subtractCostFromCurrency(game_object, emergency_cost)
                print(random.choice(ed.EVENT_DESCRIPTION["Emergency_Success"]).format(cost=emergency_cost, province=province.getName()))
            else:
                print(random.choice(ed.EVENT_DESCRIPTION["Emergency_Failure"]).format(cost=emergency_cost, province=province.getName()))
                # In the future when the satisfaction system is implemented, this block will also lower the satisfaction by a certain amount
                # for failing to deal with the emergency
        case "Extra Funds":
            obtained_funds = random.randint(100, 300)
            e.addProfitToCurrency(game_object, obtained_funds)
            print(random.choice(ed.EVENT_DESCRIPTION["Extra_Funds"]).format(profit=obtained_funds, province=province.getName()))
        case "Festival":
            print(random.choice(ed.EVENT_DESCRIPTION["Festival"]).format(province=province.getName()))
            # In the future this will boost satisfaction
        case "Extra_Ore_Vein":
            resources = ["Coal", "Iron", "Stone"]
            resource_type = random.choice(resources)
            obtained_resource = random.randint(20, 120)

            if resource_type == 'Coal':
                r.addToCoalQuantity(obtained_resource)
            elif resource_type == 'Iron':
                r.addToIronQuantity(obtained_resource)
            elif resource_type == 'Stone':
                r.addToStoneQuantity(obtained_resource)

            print(random.choice(ed.EVENT_DESCRIPTION["Extra_Ore_Vein"]).format(resource=resource_type, amount=obtained_resource, province=province.getName()))
        case "Global_Market_Forum":
            print(random.choice(ed.EVENT_DESCRIPTION["Global_Market_Forum"]))
        case "Heavy_Storm":
            storm_cost = random.randint(250, 500)
            if storm_cost < game_object.currency:
                e.subtractCostFromCurrency(game_object, storm_cost)
                print(random.choice(ed.EVENT_DESCRIPTION["Heavy_Storm_Success"]).format(cost=storm_cost, province=province.getName()))
            else:
                print(random.choice(ed.EVENT_DESCRIPTION["Heavy_Storm_Failure"]).format(cost=storm_cost, province=province.getName()))
        case "Smuggling_Bust":
            confiscated_assets = random.randint(300, 600)
            game_object.currency += confiscated_assets
            print(random.choice(ed.EVENT_DESCRIPTION["Smuggling_Bust"]).format(profit=confiscated_assets, province=province.getName()))
        case "Corruption Bust":
            lost_coal = random.randint(50, 100)
            obtained_funds = random.randint(200, 400)
            r.subtractFromCoalQuantity(game_object, lost_coal)
            e.addProfitToCurrency(game_object, obtained_funds)
            print(f"A corrupt politician was caught smuggling {lost_coal} coal! They have been forced to pay compensations of {obtained_funds} currency!")
        case "Nothing":
            pass

# Complete implementation of this method when working on version v.1.2.1
def generateRandomPopUp():
    pass