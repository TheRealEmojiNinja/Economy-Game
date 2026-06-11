'''
Preface:

Author: TheEmojiNinja
'''

# Required modules and components
import random, Data.game_data as g, Systems.resource_system as r, Systems.economy_system as e, Models.province as p

# The createProvinces method takes an empty province list and populates it with randomly generated provinces.
def createProvinces(game_object : g.GameData):
    name, factories, mines, infrastructure, deposits = None, None, None, None, None
    num_provinces = random.randrange(4, 8)
    i = 0

    province_list = game_object.provinces

    while (i < num_provinces):

        name = "Province " + str(i+1)
        factories = e.randomizeNumberOfFactories()
        mines = e.randomizeNumberOfMines()
        infrastructure = e.randomizeInfrastructureLevel()
        deposits = r.randomizeResourceDeposits()

        province = p.Province(name, factories, mines, deposits, infrastructure)
        province_list.append(province)

        i += 1

def getProvinceNames(game_object : g.GameData) -> list[p.Province]:
    list = []
    province_list = game_object.provinces
    for province in province_list:
        list.append(province.getName())
    return list






        





