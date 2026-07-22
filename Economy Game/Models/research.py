'''
Preface: The Research class is used to create a unique research object that keeps track of things being researched..

Author: TheEmojiNinja
'''

# Research class declaration
class Research:

    def __init__(self, research_name : str, research_type : str, research_time : int, research_requirements : dict, research_effects : dict) -> None:
        self.name = research_name
        self.type = research_type
        self.time = research_time
        self.requirements = research_requirements
        self.effects = research_effects

    def getResearchName(self) -> str:
        return self.name
    
    def getResearchType(self) -> str:
        return self.type
    
    def getTime(self) -> int:
        return self.time
    
    def getResearchRequirements(self) -> dict:
        return self.requirements
    
    def getResearchEffects(self) -> dict:
        return self.effects
    
    def subtractTime(self, time : int) -> None:
        self.time -= time