'''
Preface: This file consists of very important functions that manage key operations relating to refineries.

Author: TheEmojiNinja
'''

# Import required modules
import Data.game_data as g, Models.province as p, Models.refinery as refinery, Systems.economy_system as economy, Systems.raw_resource_system as raw_resource, Systems.refined_resource_system as refined_resource

# This method returns a boolean result which explains whether the user is building over the max sawmill limit.
def overMaxRefineryLimit(game_object : g.GameData, province_index : int, number_of_refineries_to_be_bought : int) -> bool:
    province_list = game_object.provinces
    province = province_list[province_index]
    in_construction = []
    for refinery in game_object.refineries_being_constructed:
        if refinery.getProvinceIndex() == province_index:
            in_construction.append(refinery)
    return province.getRefineries() + len(in_construction) + number_of_refineries_to_be_bought > province.getMaxRefineries()

# This method returns a boolean result that is determined by whether the player has enough resources 
# to purchase the selected number of refineries.
def refineriesCanBeBought(game_object : g.GameData, number_of_refineries_to_be_bought : int):

    COST_OF_REFINERY, REQUIRED_IRON_FOR_REFINERY, REQUIRED_COPPER_FOR_REFINERY = economy.getRequirementsOfRefineryConstruction()

    cost_requirements_met = number_of_refineries_to_be_bought*COST_OF_REFINERY < economy.getCurrencyAmount(game_object)
    iron_requirements_met = number_of_refineries_to_be_bought*REQUIRED_IRON_FOR_REFINERY < raw_resource.getIronQuantity(game_object)
    copper_requirements_met = number_of_refineries_to_be_bought*REQUIRED_COPPER_FOR_REFINERY < raw_resource.getCopperQuantity(game_object)

    return cost_requirements_met and iron_requirements_met and copper_requirements_met

# This method will add refineries into current production.
def addRefineriesToQueue(game_object : g.GameData, number_of_refineries : int, province_index : int):
    COST_OF_REFINERY, REQUIRED_IRON_FOR_REFINERY, REQUIRED_COPPER_FOR_REFINERY = economy.getRequirementsOfRefineryConstruction()

    cost = number_of_refineries*COST_OF_REFINERY
    required_iron = number_of_refineries*REQUIRED_IRON_FOR_REFINERY
    required_copper = number_of_refineries*REQUIRED_COPPER_FOR_REFINERY

    province_list = game_object.provinces
    time = province_list[province_index].getConstructionSpeed()

    if not overMaxRefineryLimit(game_object, province_index, number_of_refineries) and refineriesCanBeBought(game_object, number_of_refineries):
        game_object.refineries_being_constructed.append(refinery.Refinery(time, province_index, number_of_refineries))
        economy.subtractCostFromCurrency(game_object, cost)
        raw_resource.subtractFromIronQuantity(game_object, required_iron)
        raw_resource.subtractFromCopperQuantity(game_object, required_copper)

# This method updates current refineries in production by subtracting a day from the
# remaining number of days before it is finished constructing.
def updateRefineriesInConstruction(game_object : g.GameData):
    province_list = game_object.provinces
    for refinery_instance in game_object.refineries_being_constructed:
        if refinery_instance.getTime() == 1:
            province = province_list[refinery_instance.getProvinceIndex()]
            province.updateRefineries(refinery_instance.getNumberOfRefineries())
            game_object.refineries_being_constructed.remove(refinery_instance)
        elif refinery_instance.getTime() > 0:
            refinery_instance.subtractTime(1)

# This method essentially returns the total number of refineries across all provinces.
def getTotalRefineryOutput(game_object : g.GameData):
    province_list : list[p.Province] = game_object.provinces
    total = 0
    for province in province_list:
        total += province.getRefineries()
    return total