'''
Preface: The Mine class is used to create a unique mine.

Author: TheEmojiNinja
'''

# Mine class declaration
class Mine:
    construction_time = 0
    province_index = 0
    number_of_mines = 0

    def __init__(self, time : int, province_index : int, number : int) -> None:
        self.construction_time = time
        self.province_index = province_index
        self.number_of_mines = number
    
    def getTime(self) -> int:
        return self.construction_time
    
    def getProvinceIndex(self) -> int:
        return self.province_index
    
    def getNumberOfMines(self) -> int:
        return self.number_of_mines
    
    def addTime(self, time : int) -> int:
        self.construction_time += time
    
    def subtractTime(self, time : int) -> int:
        self.construction_time -= time