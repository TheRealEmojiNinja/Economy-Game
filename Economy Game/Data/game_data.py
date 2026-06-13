'''
Preface: The GameData class is used to create an object containing all key game variables for easy management throughout
gameplay.

Author: TheEmojiNinja
'''

# Required modules
import Models.factory as f, Models.mine as m, Models.province as p, Models.infrastructure as i, Data.data_loader as d
from typing import List

# GameData class declaration
class GameData:
    def __init__(self):
        
        self.currency = 0
        self.coal, self.iron, self.stone = 0, 0, 0

        self.factories_being_constructed: List[f.Factory] = []
        self.mines_being_constructed: List[m.Mine] = []
        self.infrastructure_being_constructed: List[i.Infrastructure]= []

        self.resource_deposits = []

        self.day = 1

        self.satisfaction = 50
        self.satisfaction_multiplier = 0

        self.PROVINCE_NAMES = d.loadProvinceNames()

        self.provinces : List[p.Province] = []