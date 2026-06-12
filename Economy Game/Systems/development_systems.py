'''
Preface: This file consists of very important functions that manage key operations relating to factories and mines. These
include adding factories/mines to production lasting a certain amount of time, updating them with every passing day until 
they complete production, and returning their total output.

Author: TheEmojiNinja
'''

# Import required modules
import Data.game_data as g, Models.province as p, Models.factory as f, Models.mine as m, Systems.economy_system as e, Systems.resource_system as r

# The isFactorySlotsMaxed method returns a boolean value that checks if a province's factory slots have been maxed out.
# before choosing the number of factories to buy
def isFactorySlotsMaxed(game_object : g.GameData, province_index : int) -> bool:
    province_list = game_object.provinces
    province = province_list[province_index]
    return province.getFactories() + len(game_object.factories_being_constructed) == province.getMaxFactories()

# The overMaxFactoryLimit method is similar to the isFactorySlotsMaxed method, but this one checks if the factories the 
# user is attempting to buy exceeds the limit based on available factories and factories currently in construction
def overMaxFactoryLimit(game_object : g.GameData, province_index : int, number_of_factories_to_be_bought : int) -> bool:
    province_list = game_object.provinces
    province = province_list[province_index]
    return province.getFactories() + len(game_object.factories_being_constructed) + number_of_factories_to_be_bought > province.getMaxFactories()

# 5 available, 4 in construction, buy 2 more

# The addFactoriesToQueue method will add factories into current production if the player has enough resources to buy 
# them. If they do not have enough resources, it will not add any factories.
def addFactoriesToQueue(game_object : g.GameData, number_of_factories : int, province_index : int):
    COST_OF_FACTORY = e.getCostOfFactory()
    IRON_NEEDED = e.getRequiredIronOfFactory()
    cost = number_of_factories*COST_OF_FACTORY
    required_iron = number_of_factories*IRON_NEEDED
    time = 20
    if (cost <= e.getCurrencyAmount(game_object) and required_iron <= r.getIronQuantity(game_object) and not overMaxFactoryLimit(game_object, province_index, number_of_factories)):
        game_object.factories_being_constructed.append(f.Factory(time, province_index, number_of_factories))
        e.subtractCostFromCurrency(game_object, cost)
        r.subtractFromIronQuantity(game_object, required_iron)
        return (True, cost, required_iron)
    else:
        return (False, cost, required_iron)

# The updateFactoriesInConstruction method updates current factories in production by subtracting a day from the
# remaining number of days before it is finished constructing.
def updateFactoriesInConstruction(game_object : g.GameData):
    province_list = game_object.provinces
    for factory_instance in game_object.factories_being_constructed:
        if factory_instance.getTime() < 1:
            province = province_list[factory_instance.getProvinceIndex()]
            province.addFactories(factory_instance.getNumberOfFactories())
            game_object.factories_being_constructed.remove(factory_instance)
        elif factory_instance.getTime() > 0:
            factory_instance.subtractTime(1)

# The getTotalFactoryOutput method essentially returns the total number of factories across all provinces.
def getTotalFactoryOutput(game_object : g.GameData):
    province_list : list[p.Province] = game_object.provinces
    total = 0   
    for province in province_list:
        total += province.getFactories()
    return total

# The isMineSlotsMaxed method returns a boolean value that checks if a province's mine slots have been maxed out
# before choosing the number of mines to buy
def isMineSlotsMaxed(game_object : g.GameData, province_index : int) -> bool:
    province_list = game_object.provinces
    province = province_list[province_index]
    return province.getMines() + len(game_object.mines_being_constructed) == province.getMaxMines()

# The overMaxMineLimit method is similar to the isMineSlotsMaxed method, but this one checks if the mines the 
# user is attempting to buy exceeds the limit based on available mines and mines currently in construction
def overMaxMineLimit(game_object : g.GameData, province_index : int, number_of_mines_to_be_bought : int) -> bool:
    province_list = game_object.provinces
    province = province_list[province_index]
    return province.getMines() + len(game_object.mines_being_constructed) + number_of_mines_to_be_bought > province.getMaxMines()

# The addMinesToQueue method will add mines into current production if the player has enough resources to buy 
# them. If they do not have enough resources, it will not add any mines.
def addMinesToQueue(game_object : g.GameData, number_of_mines : int, province_index : int):
    COST_OF_MINE = e.getCostOfMine()
    STONE_NEEDED = e.getRequiredStoneOfMine()
    cost = number_of_mines*COST_OF_MINE
    required_stone = number_of_mines*STONE_NEEDED
    time = 20
    if (cost <= e.getCurrencyAmount(game_object) and required_stone <= r.getStoneQuantity(game_object) and not overMaxMineLimit(game_object, province_index, number_of_mines)):
        game_object.mines_being_constructed.append(m.Mine(time, province_index, number_of_mines))
        e.subtractCostFromCurrency(game_object, cost)
        r.subtractFromStoneQuantity(game_object, required_stone)
        return (True, cost, required_stone)
    else:
        return (False, cost, required_stone)

# The updateMinesInConstruction method updates current mines in production by subtracting a day from the
# remaining number of days before it is finished constructing.
def updateMinesInConstruction(game_object : g.GameData):
    province_list = game_object.provinces
    for mine_instance in game_object.mines_being_constructed:
        if mine_instance.getTime() < 1:
            province = province_list[mine_instance.getProvinceIndex()]
            province.addMines(mine_instance.getNumberOfMines())
            game_object.mines_being_constructed.remove(mine_instance)
        elif mine_instance.getTime() > 0:
            mine_instance.subtractTime(1)

# The getTotalMiningOutputForCoal method returns the total number of mines across all provinces, provided that 
# province has coal deposits.
def getTotalMiningOutputForCoal(game_object : g.GameData):
    province_list : list[p.Province] = game_object.provinces
    total = 0
    for province in province_list:
        if "Coal" in province.getAvailableResources():
            total += province.getMines()
    return total

# The getTotalMiningOutputForIron method returns the total number of mines across all provinces, provided that 
# province has iron deposits.
def getTotalMiningOutputForIron(game_object : g.GameData):
    province_list : list[p.Province] = game_object.provinces
    total = 0
    for province in province_list:
        if "Iron" in province.getAvailableResources():
            total += province.getMines()
    return total

# The getTotalMiningOutputForStone method returns the total number of mines across all provinces, provided that 
# province has stone deposits.
def getTotalMiningOutputForStone(game_object : g.GameData):
    province_list : list[p.Province] = game_object.provinces
    total = 0
    for province in province_list:
        if "Stone" in province.getAvailableResources():
            total += province.getMines()
    return total