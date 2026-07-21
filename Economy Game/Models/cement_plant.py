'''
Preface: The CementPlant class is used to create a unique cement plant.

Author: TheEmojiNinja
'''

# CementPlant class declaration
class CementPlant:

    def __init__(self, time : int, province_index : int, number : int) -> None:
        self.construction_time = time
        self.province_index = province_index
        self.number_of_cement_plants = number
    
    def getTime(self) -> int:
        return self.construction_time
    
    def getProvinceIndex(self) -> int:
        return self.province_index
    
    def getNumberOfCementPlants(self) -> int:
        return self.number_of_cement_plants
    
    def addTime(self, time : int) -> int:
        self.construction_time += time
    
    def subtractTime(self, time : int) -> int:
        self.construction_time -= time