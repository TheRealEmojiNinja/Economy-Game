'''
Preface: The Infrastructure class is used to create infrastructure.

Author: TheEmojiNinja
'''

# Infrastructure class declaration
class Infrastructure:

    def __init__(self, time : int, province_index : int, number : int) -> None:
        self.construction_time = time
        self.province_index = province_index
        self.updated_infrastructure_level = number
    
    def getTime(self) -> int:
        return self.construction_time
    
    def getProvinceIndex(self) -> int:
        return self.province_index
    
    def getInfrastructureLevel(self) -> int:
        return self.updated_infrastructure_level
    
    def addTime(self, time : int) -> int:
        self.construction_time += time
    
    def subtractTime(self, time : int) -> int:
        self.construction_time -= time