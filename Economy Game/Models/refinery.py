'''
Preface: The Refinery class is used to create a unique refinery.

Author: TheEmojiNinja
'''

# Refinery class declaration
class Refinery:

    def __init__(self, time : int, province_index : int, number : int) -> None:
        self.construction_time = time
        self.province_index = province_index
        self.number_of_refineries = number
    
    def getTime(self) -> int:
        return self.construction_time
    
    def getProvinceIndex(self) -> int:
        return self.province_index
    
    def getNumberOfRefineries(self) -> int:
        return self.number_of_refineries
    
    def addTime(self, time : int) -> int:
        self.construction_time += time
    
    def subtractTime(self, time : int) -> int:
        self.construction_time -= time