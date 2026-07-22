'''
Preface: The GameData class is used to create an object containing all key game variables for easy management throughout
gameplay.

Author: TheEmojiNinja
'''

# Required modules
import Models.factory as factory, Models.mine as mine, Models.province as p, Models.infrastructure as infrastructure
import Models.sawmill as sawmill, Models.refinery as refinery, Models.cement_plant as cement_plant, Models.research as research
import Data.data_loader as d
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
        self.cement = 0

        self.tax_level = 0

        self.base_research_time = 45

        self.factories_being_constructed: List[factory.Factory] = []
        self.mines_being_constructed: List[mine.Mine] = []
        self.sawmills_being_constructed: List[sawmill.Sawmill] = []
        self.refineries_being_constructed: List[refinery.Refinery] = []
        self.cement_plants_being_constructed : List[cement_plant.CementPlant] = []
        self.infrastructure_being_constructed: List[infrastructure.Infrastructure]= []
        
        self.research_in_progress: List[research.Research] = []

        self.resource_deposits = []

        self.day = 1
        self.date = [1, 1, 2000]

        self.satisfaction = 50
        self.satisfaction_multiplier = 0

        self.PROVINCE_NAMES = d.loadProvinceNames()
        self.EVENTS, self.EVENT_WEIGHTS = d.loadEventsAndWeights()

        self.EVENT_DESCRIPTIONS = d.loadEventDescriptions()

        self.provinces : List[p.Province] = []

        self.event_history = []