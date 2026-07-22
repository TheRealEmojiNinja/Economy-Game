'''
Preface: The Research class is used to create a unique research object that keeps track of things being researched..

Author: TheEmojiNinja
'''

# Research class declaration
class Research:

    def __init__(self, time : int, research_type : str) -> None:
        self.research_time = time
        self.research_type = research_type
    
    def getTime(self) -> int:
        return self.research_time
    
    def getResearchType(self) -> int:
        return self.research_type
    
    def addTime(self, time : int) -> int:
        self.research_time += time
    
    def subtractTime(self, time : int) -> int:
        self.research_time -= time