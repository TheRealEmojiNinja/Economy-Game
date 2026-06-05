'''
Preface: The Province class represents a unique province with its own variations of different components. It is comprised
of a province name, the number of factories and mines, the infrastructure level, the unique resource deposits it contains,
and a hidden resource deposit that contains all resources to excavate in the future. The hidden resource deposit is not dependent 
upon any argument or parameter and is automatically defined with each Province instantiation.

Author: TheEmojiNinja
'''

# Class declaration for a Province
class Province:
    province = {"Name":None, "Factories":None, "Mines":None, "Resource_Deposits":[], "Infrastructure_Level":None, "Hidden_Resource_Deposits":[]}
    
    # Constructor with specific parameters to take in arguments that is then applied to the different components of the province
    def __init__(self, province_name : str, number_of_factories : int, number_of_mines : int, province_resource_deposits : list, infrastructure_level : int) -> None:
        self.province = {"Name":province_name, 
                         "Factories":number_of_factories, 
                         "Mines":number_of_mines, 
                         "Resource_Deposits":province_resource_deposits, 
                         "Infrastructure_Level":infrastructure_level, 
                         "Hidden_Resource_Deposits":["Coal", "Iron", "Stone"]}

    # Helper methods that get different values for certain province components (name, factories, mines)
    def getName(self):
        return self.province["Name"]
    
    def getFactories(self):
        return self.province["Factories"]
    
    def getMines(self):
        return self.province["Mines"]
    
    # Helper methods to update the values for certain province components (name, factories, mines)
    def setName(self, name):
        self.province["Name"] = name

    def addFactories(self, newFactories):
        self.province["Factories"] += newFactories

    def addMines(self, newMines):
        self.province["Mines"] += newMines

    # The printStats method prints out all the unique attributes of a province in a formatted manner.
    def printStats(self):
        stats = self.province["Name"] + " consists of " + str(self.province["Factories"]) + " factories, " + str(self.province["Mines"]) + " mines, \nan infrastructure level of " + str(self.province["Infrastructure_Level"]) + " and the following resources: "

        for resource in self.province["Resource_Deposits"]:
            stats += resource + " "
        return stats