'''
Preface: This file includes key functions regarding the creation of unique provinces.

Author: TheEmojiNinja
'''

# Required modules and components
import random, Data.game_data as g, Systems.resource_system as r, Systems.economy_system as e, Systems.terrain_system as t, Models.province as p, csv

# This method returns a random province name
def getRandomProvinceName(game_object : g.GameData) -> str:
    return game_object.PROVINCE_NAMES.pop(random.randint(0, len(game_object.PROVINCE_NAMES)-1))

# The createProvinces method takes an empty province list and populates it with randomly generated provinces.
def createProvinces(game_object : g.GameData):
    name, factories, mines, infrastructure, deposits, terrain, max_factories, max_mines = None, None, None, None, None, None, None, None
    num_provinces = random.randrange(4, 8)
    i = 0

    province_list = game_object.provinces

    while (i < num_provinces):

        name = getRandomProvinceName(game_object)
        factories = e.randomizeNumberOfFactories()
        mines = e.randomizeNumberOfMines()
        infrastructure = e.randomizeInfrastructureLevel()
        deposits = r.randomizeResourceDeposits()
        terrain = t.randomizeTerrainType()
        max_factories = t.maxFactoryCount(terrain)
        max_mines = t.maxMineCount(terrain)
        max_infrastructure = t.maxInfrastructureCount(terrain)

        province = p.Province(name, factories, mines, deposits, infrastructure, terrain, max_factories, max_mines, max_infrastructure)
        province_list.append(province)

        i += 1

# The getProvinceNames method returns a list with all the province names.
def getProvinceNames(game_object : g.GameData) -> list[p.Province]:
    list = []
    province_list = game_object.provinces
    for province in province_list:
        list.append(province.getName())
    return list



        





