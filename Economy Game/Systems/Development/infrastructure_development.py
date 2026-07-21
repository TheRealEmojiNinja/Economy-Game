'''
Preface: This file consists of very important functions that manage key operations relating to infrastructure development. 

Author: TheEmojiNinja
'''

# Import required modules
import Data.game_data as g, Models.infrastructure as i, Systems.economy_system as economy, Systems.Resource.refined_resource_system as refined_resource

# This method returns a boolean result which explains whether the user is building over the max mine limit.
def overMaxInfrastructureLimit(game_object : g.GameData, province_index : int, infrastructure_level_to_be_upgraded_to : int) -> bool:
    province_list = game_object.provinces
    province = province_list[province_index]
    in_construction = []
    for infrastructure in game_object.infrastructure_being_constructed:
        if infrastructure.getProvinceIndex() == province_index:
            in_construction.append(infrastructure)
    return province.getInfrastructureLevel() + len(in_construction) + infrastructure_level_to_be_upgraded_to > province.getMaxInfrastructureLevel()

# This method returns a boolean result that is determined by whether the player has enough resources 
# to purchase the selected number of infrastructure levels.
def infrastructureCanBeBought(game_object : g.GameData, number_of_infrastructure_levels_to_be_bought : int):

    COST_OF_INFRASTRUCTURE, REQUIRED_CEMENT_FOR_INFRASTRUCTURE, REQUIRED_WOOD_FOR_INFRASTRUCTURE = economy.getRequirementsOfInfrastructureConstruction()

    cost_requirements_met = number_of_infrastructure_levels_to_be_bought*COST_OF_INFRASTRUCTURE < economy.getCurrencyAmount(game_object)
    cement_requirements_met = number_of_infrastructure_levels_to_be_bought*REQUIRED_CEMENT_FOR_INFRASTRUCTURE < refined_resource.getCementQuantity(game_object)
    wood_requirements_met = number_of_infrastructure_levels_to_be_bought*REQUIRED_WOOD_FOR_INFRASTRUCTURE < refined_resource.getWoodQuantity(game_object)

    return cost_requirements_met and cement_requirements_met and wood_requirements_met

# This method will add infrastructure into current production.
def addInfrastructureToQueue(game_object : g.GameData, number_of_infrastructure_levels : int, province_index : int):
    COST_OF_INFRASTRUCTURE, REQUIRED_CEMENT_FOR_INFRASTRUCTURE, REQUIRED_WOOD_FOR_INFRASTRUCTURE = economy.getRequirementsOfInfrastructureConstruction()
    TIME_FOR_INFRASTRUCTURE_UPGRADE = 30

    cost = number_of_infrastructure_levels*COST_OF_INFRASTRUCTURE
    required_cement = number_of_infrastructure_levels*REQUIRED_CEMENT_FOR_INFRASTRUCTURE
    required_wood = number_of_infrastructure_levels*REQUIRED_WOOD_FOR_INFRASTRUCTURE

    if not overMaxInfrastructureLimit(game_object, province_index, number_of_infrastructure_levels) and infrastructureCanBeBought(game_object, number_of_infrastructure_levels):
        game_object.infrastructure_being_constructed.append(i.Infrastructure(TIME_FOR_INFRASTRUCTURE_UPGRADE, province_index, number_of_infrastructure_levels))
        economy.subtractCostFromCurrency(game_object, cost)
        refined_resource.subtractFromCementQuantity(game_object, required_cement)
        refined_resource.subtractFromWoodQuantity(game_object, required_wood)

# This method updates current infrastructure in production by subtracting a day from the
# remaining number of days before it is finished constructing.
def updateInfrastructureInConstruction(game_object : g.GameData):
    province_list = game_object.provinces
    for infrastructure_instance in game_object.infrastructure_being_constructed:
        if infrastructure_instance.getTime() < 1:
            province = province_list[infrastructure_instance.getProvinceIndex()]
            province.updateInfrastructureLevel(infrastructure_instance.getInfrastructureLevel())
            game_object.infrastructure_being_constructed.remove(infrastructure_instance)
        elif infrastructure_instance.getTime() > 0:
            infrastructure_instance.subtractTime(1)
