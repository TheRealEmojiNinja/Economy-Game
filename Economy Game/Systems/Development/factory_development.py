'''
Preface: This file consists of very important functions that manage key operations relating to factories. 

Author: TheEmojiNinja
'''

# Import required modules
import Data.game_data as g, Models.province as p, Models.factory as f, Systems.economy_system as economy, Systems.raw_resource_system as raw_resource, Systems.refined_resource_system as refined_resource

# This method returns a boolean result which explains whether the user is building over the max factory limit.
def overMaxFactoryLimit(game_object : g.GameData, province_index : int, number_of_factories_to_be_bought : int) -> bool:
    province_list = game_object.provinces
    province = province_list[province_index]
    in_construction = []
    for factory in game_object.factories_being_constructed:
        if factory.getProvinceIndex() == province_index:
            in_construction.append(factory)
    return province.getFactories() + len(in_construction) + number_of_factories_to_be_bought > province.getMaxFactories()

# This method returns a boolean result that is determined by whether the player has enough resources 
# to purchase the selected number of factories.
def factoriesCanBeBought(game_object : g.GameData, number_of_factories_to_be_bought : int):

    COST_OF_FACTORY, REQUIRED_STONE_FOR_FACTORY, REQUIRED_IRON_FOR_FACTORY, REQUIRED_COPPER_FOR_FACTORY = economy.getRequirementsOfFactoryConstruction()

    cost_requirements_met = number_of_factories_to_be_bought*COST_OF_FACTORY < economy.getCurrencyAmount(game_object)
    stone_requirements_met = number_of_factories_to_be_bought*REQUIRED_STONE_FOR_FACTORY < raw_resource.getStoneQuantity(game_object)
    iron_requirements_met = number_of_factories_to_be_bought*REQUIRED_IRON_FOR_FACTORY < raw_resource.getIronQuantity(game_object)
    copper_requirements_met = number_of_factories_to_be_bought*REQUIRED_COPPER_FOR_FACTORY < raw_resource.getCopperQuantity(game_object)

    return cost_requirements_met and stone_requirements_met and iron_requirements_met and copper_requirements_met

# This method will add factories into current production.
def addFactoriesToQueue(game_object : g.GameData, number_of_factories : int, province_index : int):
    COST_OF_FACTORY, REQUIRED_STONE_FOR_FACTORY, REQUIRED_IRON_FOR_FACTORY, REQUIRED_COPPER_FOR_FACTORY = economy.getRequirementsOfFactoryConstruction()

    cost = number_of_factories*COST_OF_FACTORY
    required_stone = number_of_factories*REQUIRED_STONE_FOR_FACTORY
    required_iron = number_of_factories*REQUIRED_IRON_FOR_FACTORY
    required_copper = number_of_factories*REQUIRED_COPPER_FOR_FACTORY

    province_list = game_object.provinces
    time = province_list[province_index].getConstructionSpeed()

    if not overMaxFactoryLimit(game_object, province_index, number_of_factories) and factoriesCanBeBought(game_object, number_of_factories):
        game_object.factories_being_constructed.append(f.Factory(time, province_index, number_of_factories))
        economy.subtractCostFromCurrency(game_object, cost)
        raw_resource.subtractFromStoneQuantity(game_object, required_stone)
        raw_resource.subtractFromIronQuantity(game_object, required_iron)
        raw_resource.subtractFromCopperQuantity(game_object, required_copper)

# This method updates current factories in production by subtracting a day from the
# remaining number of days before it is finished constructing.
def updateFactoriesInConstruction(game_object : g.GameData):
    province_list = game_object.provinces
    for factory_instance in game_object.factories_being_constructed:
        if factory_instance.getTime() < 1:
            province = province_list[factory_instance.getProvinceIndex()]
            province.updateFactories(factory_instance.getNumberOfFactories())
            game_object.factories_being_constructed.remove(factory_instance)
        elif factory_instance.getTime() > 0:
            factory_instance.subtractTime(1)

# This method essentially returns the total number of factories across all provinces.
def getTotalFactoryOutput(game_object : g.GameData):
    province_list : list[p.Province] = game_object.provinces
    total = 0   
    for province in province_list:
        if province.getOutageStatus() == True:
            if province.getOutageTime() < 1:
                province.updateOutageStatus(False)
                province.updateOutageTime(-1)
            else:
                province.updateOutageTime(-1)
        else:
            total += province.getFactories()*2 if province.getMaximumProductionStatus() else province.getFactories()
    return total