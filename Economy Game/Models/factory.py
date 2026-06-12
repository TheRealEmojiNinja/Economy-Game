'''
Preface: The Factory class is used to create a unique factory.

Author: TheEmojiNinja
'''

# Factory class declaration
class Factory:
    construction_time = 0
    province_index = 0
    number_of_factories = 0

    def __init__(self, time : int, province_index : int, number : int) -> None:
        self.construction_time = time
        self.province_index = province_index
        self.number_of_factories = number
    
    def getTime(self) -> int:
        return self.construction_time
    
    def getProvinceIndex(self) -> int:
        return self.province_index
    
    def getNumberOfFactories(self) -> int:
        return self.number_of_factories
    
    def addTime(self, time : int) -> int:
        self.construction_time += time
    
    def subtractTime(self, time : int) -> int:
        self.construction_time -= time