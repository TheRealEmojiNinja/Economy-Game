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
                 number_of_mines : int, province_resource_deposits : list, 
                 infrastructure_level : int, terrain_type : str, 
                 max_factories_possible : int, max_mines_possible : int, 
                 max_infrastructure_possible : int) -> None:
        self.province = {"Name":province_name, 
                         "Factories":number_of_factories, 
                         "Mines":number_of_mines, 
                         "Resource_Deposits":province_resource_deposits, 
                         "Infrastructure_Level":infrastructure_level, 
                         "Hidden_Resource_Deposits":["Coal", "Iron", "Stone"],
                         "Terrain":terrain_type,
                         "Max_Factories":max_factories_possible,
                         "Max_Mines":max_mines_possible,
                         "Max_Infrastructure_Level":max_infrastructure_possible}

    # Helper methods that get different values for certain province components 
    def getName(self) -> str:
        return self.province["Name"]
    
    def getFactories(self) -> int:
        return self.province["Factories"]
    
    def getMines(self) -> int:
        return self.province["Mines"]
    
    def getTerrainType(self) -> str:
        return self.province["Terrain"]
    
    def getMaxFactories(self) -> int:
        return self.province["Max_Factories"]
    
    def getMaxMines(self) -> int:
        return self.province["Max_Mines"]
    
    def getMaxInfrastructureLevel(self) -> int:
        return self.province["Max_Infrastructure_Level"]
    
    # Helper methods to update the values for certain province components 
    def setName(self, name : str) -> None:
        self.province["Name"] = name

    def addFactories(self, newFactories : int) -> None:
        self.province["Factories"] += newFactories

    def addMines(self, newMines : int) -> None:
        self.province["Mines"] += newMines

    # Helper method to return the province's available resources currently
    def getAvailableResources(self) -> list:
        return self.province["Resource_Deposits"]

    # The printStats method prints out all the unique attributes of a province in a formatted manner
    def printStats(self) -> str:
        deposits = ''
        for resource in self.province["Resource_Deposits"]:
            deposits += resource + " "

        stats = f'''{self.province["Name"].upper()}: 
        Factories: {self.province["Factories"]}
        Mines: {self.province["Mines"]}
        Infrastructure Level: {self.province["Infrastructure_Level"]}
        Terrain Type: {self.province["Terrain"]}
        Known Resources: {deposits}
        Max Factories Possible: {self.province["Max_Factories"]}
        Max Mines Possible: {self.province["Max_Mines"]}
        Max Infrastructure Level Possible: {self.province["Max_Infrastructure_Level"]}'''

        return stats