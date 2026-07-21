'''
Preface: This file consists of very important functions that manage key operations relating to mines. 

Author: TheEmojiNinja
'''

# Import required modules
import Data.game_data as g, Models.province as p, Models.mine as m, Systems.economy_system as economy, Systems.Resource.refined_resource_system as refined_resource

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

    COST_OF_MINE, REQUIRED_WOOD_FOR_MINE = economy.getRequirementsOfMineConstruction()

    cost_requirements_met = number_of_mines_to_be_bought*COST_OF_MINE < economy.getCurrencyAmount(game_object)
    wood_requirements_met = number_of_mines_to_be_bought*REQUIRED_WOOD_FOR_MINE < refined_resource.getWoodQuantity(game_object)

    return cost_requirements_met and wood_requirements_met

# This method will add mines into current production.
def addMinesToQueue(game_object : g.GameData, number_of_mines : int, province_index : int):
    COST_OF_MINE, REQUIRED_WOOD_FOR_MINE = economy.getRequirementsOfMineConstruction()

    cost = number_of_mines*COST_OF_MINE
    required_wood = number_of_mines*REQUIRED_WOOD_FOR_MINE

    province_list = game_object.provinces
    time = province_list[province_index].getConstructionSpeed()

    if not overMaxMineLimit(game_object, province_index, number_of_mines) and minesCanBeBought(game_object, number_of_mines):
        game_object.mines_being_constructed.append(m.Mine(time, province_index, number_of_mines))
        economy.subtractCostFromCurrency(game_object, cost)
        refined_resource.subtractFromWoodQuantity(game_object, required_wood)

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

def getTotalMiningOutputForCopper(game_object : g.GameData):
    province_list : list[p.Province] = game_object.provinces
    total = 0
    for province in province_list:
        if "Copper" in province.getAvailableResources():
            total += province.getMines()
    return total