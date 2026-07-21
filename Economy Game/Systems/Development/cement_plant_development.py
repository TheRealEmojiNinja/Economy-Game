'''
Preface: This file consists of very important functions that manage key operations relating to cement plants. 

Author: TheEmojiNinja
'''

# Import required modules
import Data.game_data as g, Models.cement_plant as cement_plant, Systems.economy_system as economy, Systems.Resource.refined_resource_system as refined_resource, Models.province as p

# This method returns a boolean result which explains whether the user is building over the max cement plant limit.
def overMaxCementPlantLimit(game_object : g.GameData, province_index : int, number_of_cement_plants_to_be_bought : int) -> bool:
    province_list = game_object.provinces
    province = province_list[province_index]
    in_construction = []
    for cement_plant in game_object.cement_plants_being_constructed:
        if cement_plant.getProvinceIndex() == province_index:
            in_construction.append(cement_plant)
    return province.getCementPlants() + len(in_construction) + number_of_cement_plants_to_be_bought > province.getMaxCementPlants()

# This method returns a boolean result that is determined by whether the player has enough resources 
# to purchase the selected number of cement plants.
def cementPlantsCanBeBought(game_object : g.GameData, number_of_cement_plants_to_be_bought : int):

    COST_OF_CEMENT_PLANT, REQUIRED_CEMENT_FOR_CEMENT_PLANT, REQUIRED_WOOD_FOR_CEMENT_PLANT = economy.getRequirementsOfCementPlantConstruction()

    cost_requirements_met = number_of_cement_plants_to_be_bought*COST_OF_CEMENT_PLANT < economy.getCurrencyAmount(game_object)
    cement_requirements_met = number_of_cement_plants_to_be_bought*REQUIRED_CEMENT_FOR_CEMENT_PLANT < refined_resource.getCementQuantity(game_object)
    wood_requirements_met = number_of_cement_plants_to_be_bought*REQUIRED_WOOD_FOR_CEMENT_PLANT < refined_resource.getWoodQuantity(game_object)

    return cost_requirements_met and cement_requirements_met and wood_requirements_met

# This method will add cement plants into current production.
def addCementPlantsToQueue(game_object : g.GameData, number_of_cement_plants_to_be_bought : int, province_index : int):
    COST_OF_CEMENT_PLANT, REQUIRED_CEMENT_FOR_CEMENT_PLANT, REQUIRED_WOOD_FOR_CEMENT_PLANT = economy.getRequirementsOfCementPlantConstruction()

    cost = number_of_cement_plants_to_be_bought*COST_OF_CEMENT_PLANT
    required_cement = number_of_cement_plants_to_be_bought*REQUIRED_CEMENT_FOR_CEMENT_PLANT
    required_wood = number_of_cement_plants_to_be_bought*REQUIRED_WOOD_FOR_CEMENT_PLANT

    province_list = game_object.provinces
    time = province_list[province_index].getConstructionSpeed()

    if not overMaxCementPlantLimit(game_object, province_index, number_of_cement_plants_to_be_bought) and cementPlantsCanBeBought(game_object, number_of_cement_plants_to_be_bought):
        game_object.cement_plants_being_constructed.append(cement_plant.CementPlant(time, province_index, number_of_cement_plants_to_be_bought))
        economy.subtractCostFromCurrency(game_object, cost)
        refined_resource.subtractFromCementQuantity(game_object, required_cement)
        refined_resource.subtractFromWoodQuantity(game_object, required_wood)

# This method updates current cement plants in production by subtracting a day from the
# remaining number of days before it is finished constructing.
def updateCementPlantsInConstruction(game_object : g.GameData):
    province_list = game_object.provinces
    for cement_plant_instance in game_object.cement_plants_being_constructed:
        if cement_plant_instance.getTime() < 1:
            province = province_list[cement_plant_instance.getProvinceIndex()]
            province.updateCementPlants(cement_plant_instance.getNumberOfCementPlants())
            game_object.cement_plants_being_constructed.remove(cement_plant_instance)
        elif cement_plant_instance.getTime() > 0:
            cement_plant_instance.subtractTime(1)

# This method essentially returns the total number of cement plants across all provinces.
def getTotalCementPlantOutput(game_object : g.GameData):
    province_list : list[p.Province] = game_object.provinces
    total = 0   
    for province in province_list:
        total += province.getSawmills()
    return total