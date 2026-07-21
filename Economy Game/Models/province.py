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
                 number_of_refineries : int, number_of_cement_plants : int,
                 infrastructure_level : int, 
                 terrain_type : str, province_resource_deposits : list, 
                 max_factories_possible : int, max_mines_possible : int, 
                 max_sawmills_possible : int, max_refineries_possible : int,
                 max_cement_plants_possible : int, max_infrastructure_possible : int) -> None:
        
        self.province_name = province_name
        self.factories = number_of_factories
        self.mines = number_of_mines
        self.sawmills = number_of_sawmills
        self.refineries = number_of_refineries
        self.cement_plants = number_of_cement_plants
        self.infrastructure_level = infrastructure_level
        self.resource_deposits = province_resource_deposits
        self.province_terrain = terrain_type
        self.max_factory_limit = max_factories_possible
        self.max_mine_limit = max_mines_possible
        self.max_sawmill_limit = max_sawmills_possible
        self.max_refinery_limit = max_refineries_possible
        self.max_cement_plant_limit = max_cement_plants_possible
        self.max_infrastructure_limit = max_infrastructure_possible
        self.steel_production = False
        self.fuel_production = False
        self.wood_production = False
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
    
    def getRefineries(self) -> int:
        return self.refineries
    
    def getCementPlants(self) -> int:
        return self.cement_plants
    
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

    def getMaxRefineries(self) -> int:
        return self.max_refinery_limit
    
    def getMaxCementPlants(self) -> int:
        return self.max_cement_plant_limit
    
    def getMaxInfrastructureLevel(self) -> int:
        return self.max_infrastructure_limit
    
    def getSteelProductionStatus(self) -> bool:
        return self.steel_production
    
    def getFuelProductionStatus(self) -> bool:
        return self.fuel_production
    
    def getWoodProductionStatus(self) -> bool:
        return self.wood_production

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

    def updateRefineries(self, new_refineries : int) -> None:
        self.refineries += new_refineries

    def updateCementPlants(self, new_cement_plants : int) -> None:
        self.cement_plants += new_cement_plants

    def updateInfrastructureLevel(self, new_infrastructure_level : int) -> None:
        self.infrastructure_level += new_infrastructure_level

    def updateSteelProductionStatus(self, new_status : bool) -> None:
        self.steel_production = new_status

    def updateFuelProductionStatus(self, new_status : bool) -> None:
        self.fuel_production = new_status
    
    def updateWoodProductionStatus(self, new_status : bool) -> None:
        self.wood_production = new_status
    
    def updateOutageStatus(self, status : bool) -> None:
        self.electrical_outage_status = status
    
    def updateOutageTime(self, days : int) -> None:
        self.electrical_outage_time += days

    def updateMaximumProductionStatus(self, new_max_production_status : bool) -> None:
        self.maximum_production_status = new_max_production_status