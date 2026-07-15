'''
Preface: This file consists of very important functions that manage key operations relating to factories and mines. These
include adding factories/mines to production lasting a certain amount of time, updating them with every passing day until 
they complete production, and returning their total output.

Author: TheEmojiNinja
'''

# Import required modules
import Data.game_data as g, Models.province as p, Models.factory as f, Models.mine as m, Models.infrastructure as i, Systems.economy_system as e, Systems.resource_system as r

# This method returns a string returning any buildings in construction
def returnBuildingsInConstruction(game_object : g.GameData):
    buildings_in_construction = ''
    province_list = game_object.provinces

    for province in province_list:
        buildings_in_construction += f"{province.getName()}:\n"
        for factory in game_object.factories_being_constructed:
            factory_index = factory.getProvinceIndex()
            if factory_index == province_list.index(province):
                #print("first: ", factory_index, " second: ", province_list.index(province))
                buildings_in_construction += f"{factory.getNumberOfFactories()} factories will\nfinish construction\nin {factory.getTime()} days\n"
        for mine in game_object.mines_being_constructed:
            mine_index = mine.getProvinceIndex()
            if mine_index == province_list.index(province):
                buildings_in_construction += f"{mine.getNumberOfMines()} mines will\nfinish construction\nin {mine.getTime()} days\n"
        for infrastructure in game_object.infrastructure_being_constructed:
            infrastructure_index = infrastructure.getProvinceIndex()
            if infrastructure_index == province_list.index(province):
                buildings_in_construction += f"{infrastructure.getInfrastructureLevel()} infrastructure levels will\nfinish construction\nin {infrastructure.getTime()} days\n"
        buildings_in_construction += "\n"
    
    return buildings_in_construction

'''
The code contained under this docstring manages everything related to the development of factories.
'''

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
    result = number_of_factories_to_be_bought*e.getCostOfFactory() < e.getCurrencyAmount(game_object) and number_of_factories_to_be_bought*e.getRequiredIronOfFactory() < r.getIronQuantity(game_object)
    return result

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

'''
The code contained under this docstring manages everything related to the development of mines.
'''

# This method returns a boolean result which explains whether the user is building over the max mine limit.
def overMaxMineLimit(game_object : g.GameData, province_index : int, number_of_mines_to_be_bought : int) -> bool:
    province_list = game_object.provinces
    province = province_list[province_index]
    in_construction = []
    for mine in game_object.mines_being_constructed:
        if mine.getProvinceIndex() == province_index:
            in_construction.append(mine)
    return province.getMines() + len(in_construction) + number_of_mines_to_be_bought > province.getMaxMines()

# This method returns a boolean result that is determined by whether the player has enough resources 
# to purchase the selected number of mines.
def minesCanBeBought(game_object : g.GameData, number_of_mines_to_be_bought : int):
    result = number_of_mines_to_be_bought*e.getCostOfMine() < e.getCurrencyAmount(game_object) and number_of_mines_to_be_bought*e.getRequiredStoneOfMine() < r.getStoneQuantity(game_object)
    return result

# This method will add mines into current production.
def addMinesToQueue(game_object : g.GameData, number_of_mines : int, province_index : int):
    COST_OF_MINE = e.getCostOfMine()
    STONE_NEEDED = e.getRequiredStoneOfMine()

    cost = number_of_mines*COST_OF_MINE
    required_stone = number_of_mines*STONE_NEEDED

    province_list = game_object.provinces
    time = province_list[province_index].getConstructionSpeed()

    if not overMaxMineLimit(game_object, province_index, number_of_mines) and minesCanBeBought(game_object, number_of_mines):
        game_object.mines_being_constructed.append(m.Mine(time, province_index, number_of_mines))
        e.subtractCostFromCurrency(game_object, cost)
        r.subtractFromStoneQuantity(game_object, required_stone)

# This method updates current mines in production by subtracting a day from the
# remaining number of days before it is finished constructing.
def updateMinesInConstruction(game_object : g.GameData):
    province_list = game_object.provinces
    for mine_instance in game_object.mines_being_constructed:
        if mine_instance.getTime() < 1:
            province = province_list[mine_instance.getProvinceIndex()]
            province.updateMines(mine_instance.getNumberOfMines())
            game_object.mines_being_constructed.remove(mine_instance)
        elif mine_instance.getTime() > 0:
            mine_instance.subtractTime(1)

# This method returns the total number of mines across all provinces, provided that 
# province has coal deposits.
def getTotalMiningOutputForCoal(game_object : g.GameData):
    province_list : list[p.Province] = game_object.provinces
    total = 0
    for province in province_list:
        if "Coal" in province.getAvailableResources():
            total += province.getMines()
    return total

# This method returns the total number of mines across all provinces, provided that 
# province has iron deposits.
def getTotalMiningOutputForIron(game_object : g.GameData):
    province_list : list[p.Province] = game_object.provinces
    total = 0
    for province in province_list:
        if "Iron" in province.getAvailableResources():
            total += province.getMines()
    return total

# This method returns the total number of mines across all provinces, provided that 
# province has stone deposits.
def getTotalMiningOutputForStone(game_object : g.GameData):
    province_list : list[p.Province] = game_object.provinces
    total = 0
    for province in province_list:
        if "Stone" in province.getAvailableResources():
            total += province.getMines()
    return total

'''
The code contained under this docstring manages everything related to the development of infrastructure.
'''

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
    result = number_of_infrastructure_levels_to_be_bought*e.getCostOfInfrastructure() < e.getCurrencyAmount(game_object) and number_of_infrastructure_levels_to_be_bought*e.getRequiredStoneOfInfrastructure() < r.getStoneQuantity(game_object)
    return result

# This method will add infrastructure into current production.
def addInfrastructureToQueue(game_object : g.GameData, number_of_infrastructure : int, province_index : int):
    COST_OF_INFRASTRUCTURE = e.getCostOfInfrastructure()
    STONE_NEEDED = e.getRequiredStoneOfInfrastructure()
    TIME_FOR_INFRASTRUCTURE_UPGRADE = 30

    cost = number_of_infrastructure*COST_OF_INFRASTRUCTURE
    required_stone = number_of_infrastructure*STONE_NEEDED

    if not overMaxInfrastructureLimit(game_object, province_index, number_of_infrastructure) and infrastructureCanBeBought(game_object, number_of_infrastructure):
        game_object.infrastructure_being_constructed.append(i.Infrastructure(TIME_FOR_INFRASTRUCTURE_UPGRADE, province_index, number_of_infrastructure))
        e.subtractCostFromCurrency(game_object, cost)
        r.subtractFromStoneQuantity(game_object, required_stone)

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
