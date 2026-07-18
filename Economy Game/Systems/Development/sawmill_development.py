'''
Preface: This file consists of very important functions that manage key operations relating to sawmills.

Author: TheEmojiNinja
'''

# Import required modules
import Data.game_data as g, Models.province as p, Models.factory as f, Models.mine as m, Models.infrastructure as i, Systems.economy_system as economy, Systems.raw_resource_system as raw_resource, Systems.refined_resource_system as refined_resource

# This method returns a boolean result which explains whether the user is building over the max sawmill limit.
def overMaxSawmillLimit(game_object : g.GameData, province_index : int, number_of_sawmills_to_be_bought : int) -> bool:
    province_list = game_object.provinces
    province = province_list[province_index]
    in_construction = []
    for sawmill in game_object.sawmills_being_constructed:
        if sawmill.getProvinceIndex() == province_index:
            in_construction.append(sawmill)
    return province.getSawmills() + len(in_construction) + number_of_sawmills_to_be_bought > province.getMaxSawmills()

# This method returns a boolean result that is determined by whether the player has enough resources 
# to purchase the selected number of sawmills.
def sawmillsCanBeBought(game_object : g.GameData, number_of_sawmills_to_be_bought : int, province : p.Province):

    COST_OF_SAWMILL, REQUIRED_STONE_FOR_SAWMILL, REQUIRED_WOOD_FOR_SAWMILL = economy.getRequirementsOfSawmillConstruction()

    cost_requirements_met = number_of_sawmills_to_be_bought*COST_OF_SAWMILL < economy.getCurrencyAmount(game_object)
    stone_requirements_met = number_of_sawmills_to_be_bought*REQUIRED_STONE_FOR_SAWMILL < raw_resource.getStoneQuantity(game_object)
    wood_requirements_met = number_of_sawmills_to_be_bought*REQUIRED_WOOD_FOR_SAWMILL < refined_resource.getWoodQuantity(game_object)
    terrain_type_valid = True if province.getTerrainType() in ['Mountainous', 'Forested'] else False

    return cost_requirements_met and stone_requirements_met and wood_requirements_met and terrain_type_valid

# This method will add factories into current production.
def addFactoriesToQueue(game_object : g.GameData, number_of_factories : int, province_index : int):
    COST_OF_FACTORY = e.getCostOfFactory()
    IRON_NEEDED = e.getRequiredIronOfFactory()

    cost = number_of_factories*COST_OF_FACTORY
    required_iron = number_of_factories*IRON_NEEDED

    province_list = game_object.provinces
    time = province_list[province_index].getConstructionSpeed()

    if not overMaxFactoryLimit(game_object, province_index, number_of_factories) and factoriesCanBeBought(game_object, number_of_factories):
        game_object.factories_being_constructed.append(f.Factory(time, province_index, number_of_factories))
        e.subtractCostFromCurrency(game_object, cost)
        r.subtractFromIronQuantity(game_object, required_iron)

# This method updates current sawmills in production by subtracting a day from the
# remaining number of days before it is finished constructing.
def updateSawmillsInConstruction(game_object : g.GameData):
    province_list = game_object.provinces
    for sawmill_instance in game_object.sawmills_being_constructed:
        if sawmill_instance.getTime() == 1:
            province = province_list[sawmill_instance.getProvinceIndex()]
            province.updateSawmills(sawmill_instance.getNumberOfSawmills())
            game_object.sawmills_being_constructed.remove(sawmill_instance)
        elif sawmill_instance.getTime() > 0:
            sawmill_instance.subtractTime(1)

# This method essentially returns the total number of sawmills across all provinces.
def getTotalLumberOutputForTimber(game_object : g.GameData):
    province_list : list[p.Province] = game_object.provinces
    total = 0
    for province in province_list:
        if "Timber" in province.getAvailableResources():
            total += province.getSawmills()
    return total