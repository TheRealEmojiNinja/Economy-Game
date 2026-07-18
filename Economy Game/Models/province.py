'''
Preface: The Province class represents a unique province with its own variations of different components. It is comprised
of a province name, the number of factories and mines, the infrastructure level, the unique resource deposits it contains,
and a hidden resource deposit that contains all resources to excavate in the future. The hidden resource deposit is not dependent 
upon any argument or parameter and is automatically defined with each Province instantiation.

Author: TheEmojiNinja
'''

# Class declaration for a Province
class Province:
    
    resources = ["Coal", "Iron", "Stone"]
    
    # Constructor with specific parameters to take in arguments that is then applied to the different components of the province
    def __init__(self, province_name : str, number_of_factories : int, 
                 number_of_mines : int, number_of_sawmills : int,
                 province_resource_deposits : list, 
                 infrastructure_level : int, terrain_type : str, 
                 max_factories_possible : int, max_mines_possible : int, 
                 max_sawmills_possible : int, max_infrastructure_possible : int) -> None:
        
        self.province_name = province_name
        self.factories = number_of_factories
        self.mines = number_of_mines
        self.sawmills = number_of_sawmills
        self.infrastructure_level = infrastructure_level
        self.resource_deposits = province_resource_deposits
        self.province_terrain = terrain_type
        self.max_factory_limit = max_factories_possible
        self.max_mine_limit = max_mines_possible
        self.max_sawmill_limit = max_sawmills_possible
        self.max_infrastructure_limit = max_infrastructure_possible
        self.hidden_resource_deposits = Province.resources
        self.electrical_outage_status = False
        self.electrical_outage_time = -1
        self.maximum_production_status = False


    # Helper methods that get different values for certain province components 
    def getName(self) -> str:
        return self.province_name
    
    def getFactories(self) -> int:
        return self.factories

    def getMines(self) -> int:
        return self.mines
    
    def getSawmills(self) -> int:
        return self.sawmills
    
    def getInfrastructureLevel(self) -> int:
        return self.infrastructure_level
    
    def getTerrainType(self) -> str:
        return self.province_terrain
    
    def getMaxFactories(self) -> int:
        return self.max_factory_limit
    
    def getMaxMines(self) -> int:
        return self.max_mine_limit
    
    def getMaxSawmills(self) -> int:
        return self.max_sawmill_limit
    
    def getMaxInfrastructureLevel(self) -> int:
        return self.max_infrastructure_limit

    def getAvailableResources(self) -> list:
        deposits = ''
        for deposit in self.resource_deposits:
            deposits += deposit
            if self.resource_deposits.index(deposit) != len(self.resource_deposits)-1:
                deposits += ', '
        return deposits
    
    def getConstructionSpeed(self) -> int:
        infrastructure_level = self.infrastructure_level
        match infrastructure_level:
            case 0:
                return 30
            case 1:
                return 28
            case 2:
                return 25
            case 3:
                return 22
            case 4:
                return 19
            case 5:
                return 17
            case 6:
                return 15
            case 7:
                return 14
            case 8:
                return 13
            case 9:
                return 11
            case 10:
                return 10
    
    def getOutageStatus(self) -> bool:
        return self.electrical_outage_status
    
    def getOutageTime(self) -> int:
        return self.electrical_outage_time
    
    def getMaximumProductionStatus(self) -> bool:
        return self.maximum_production_status
    
    # Helper methods to update the values for certain province components 
    def setName(self, name : str) -> None:
        self.province_name = name

    def updateFactories(self, new_factories : int) -> None:
        self.factories += new_factories

    def updateMines(self, new_mines : int) -> None:
        self.mines += new_mines
    
    def updateSawmills(self, new_sawmills : int) -> None:
        self.sawmills += new_sawmills

    def updateInfrastructureLevel(self, new_infrastructure_level : int):
        self.infrastructure_level += new_infrastructure_level
    
    def updateOutageStatus(self, status : bool) -> None:
        self.electrical_outage_status = status
    
    def updateOutageTime(self, days : int) -> None:
        self.electrical_outage_time += days

    def updateMaximumProductionStatus(self, new_max_production_status : bool) -> None:
        self.maximum_production_status = new_max_production_status