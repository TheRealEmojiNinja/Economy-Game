'''
Preface: This file consists of very important functions that manage key operations relating to factories and mines. These
include adding factories/mines to production lasting a certain amount of time, updating them with every passing day until 
they complete production, and returning their total output.

Author: TheEmojiNinja
'''

# Import required modules
import Data.game_data as g, Models.province as p, Models.factory as f, Models.mine as m, Models.infrastructure as i, Systems.economy_system as economy, Systems.raw_resource_system as raw_resource, Systems.refined_resource_system as refined_resource

# This method returns a string returning any buildings in construction
def returnBuildingsInConstruction(game_object : g.GameData):
    buildings_in_construction = ''
    province_list = game_object.provinces

    for province in province_list:
        buildings_in_construction += f"{province.getName()}:\n"
        for factory in game_object.factories_being_constructed:
            factory_index = factory.getProvinceIndex()
            if factory_index == province_list.index(province):
                buildings_in_construction += f"{factory.getNumberOfFactories()} factories will\nfinish construction\nin {factory.getTime()} days\n"
        for mine in game_object.mines_being_constructed:
            mine_index = mine.getProvinceIndex()
            if mine_index == province_list.index(province):
                buildings_in_construction += f"{mine.getNumberOfMines()} mines will\nfinish construction\nin {mine.getTime()} days\n"
        for sawmill in game_object.sawmills_being_constructed:
            sawmill_index = sawmill.getProvinceIndex()
            if sawmill_index == province_list.index(province):
                buildings_in_construction += f"{sawmill.getNumberOfSawmills()} sawmills will\nfinish construction\nin {sawmill.getTime()} days\n"
        for infrastructure in game_object.infrastructure_being_constructed:
            infrastructure_index = infrastructure.getProvinceIndex()
            if infrastructure_index == province_list.index(province):
                buildings_in_construction += f"{infrastructure.getInfrastructureLevel()} infrastructure levels will\nfinish construction\nin {infrastructure.getTime()} days\n"
        buildings_in_construction += "\n"
    
    return buildings_in_construction