'''
Preface: The Sawmill class is used to create a unique sawmill.

Author: TheEmojiNinja
'''

# Sawmill class declaration
class Sawmill:

    def __init__(self, time : int, province_index : int, number : int) -> None:
        self.construction_time = time
        self.province_index = province_index
        self.number_of_sawmills = number
    
    def getTime(self) -> int:
        return self.construction_time
    
    def getProvinceIndex(self) -> int:
        return self.province_index
    
    def getNumberOfSawmills(self) -> int:
        return self.number_of_sawmills
    
    def addTime(self, time : int) -> int:
        self.construction_time += time
    
    def subtractTime(self, time : int) -> int:
        self.construction_time -= time