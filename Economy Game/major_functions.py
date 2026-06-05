'''
Preface:

Author: TheEmojiNinja
'''

# Required modules and components
import random, province as p, variable_management as vm

# The createProvinces method takes an empty province list and populates it with randomly generated provinces.
def createProvinces(province_list : list):
    name, factories, mines, infrastructure, deposits = None, None, None, None, None
    num_provinces = random.randrange(4, 8)
    i = 0

    while (i < num_provinces):

        name = "Province " + str(i+1)
        factories = vm.randomizeNumberOfFactories()
        mines = vm.randomizeNumberOfMines()
        infrastructure = vm.randomizeInfrastructureLevel()
        deposits = vm.randomizeResourceDeposits()

        province = p.Province(name, factories, mines, deposits, infrastructure)
        province_list.append(province)

        i += 1

def getProvinceNames(province_list : list[p.Province]) -> list[p.Province]:
    list = []
    for province in province_list:
        list.append(province.getName())
    return list






        





