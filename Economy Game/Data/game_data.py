'''
Preface: The GameData class is used to create an object containing all key game variables for easy management throughout
gameplay.

Author: TheEmojiNinja
'''

# Required modules
import Models.factory as f, Models.mine as m, Models.province as p, Models.infrastructure as i, Models.sawmill as s, Data.data_loader as d
from typing import List

# GameData class declaration
class GameData:
    def __init__(self):
        
        self.currency = 0
        self.debt = 0

        self.coal = 0
        self.iron = 0
        self.stone = 0
        self.timber = 0
        self.copper = 0
        
        self.steel = 0
        self.fuel = 0
        self.wood = 0

        self.steel_production = False
        self.fuel_production = False
        self.wood_production = False

        self.tax_level = 0

        self.factories_being_constructed: List[f.Factory] = []
        self.mines_being_constructed: List[m.Mine] = []
        self.infrastructure_being_constructed: List[i.Infrastructure]= []
        self.sawmills_being_constructed: List[s.Sawmill] = []

        self.resource_deposits = []

        self.day = 1

        self.satisfaction = 50
        self.satisfaction_multiplier = 0

        self.PROVINCE_NAMES = d.loadProvinceNames()
        self.EVENTS, self.EVENT_WEIGHTS = d.loadEventsAndWeights()

        self.EVENT_DESCRIPTIONS = d.loadEventDescriptions()

        self.provinces : List[p.Province] = []

        self.event_history = []