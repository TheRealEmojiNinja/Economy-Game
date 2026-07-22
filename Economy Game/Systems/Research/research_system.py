import Data.game_data as g, Systems.economy_system as economy, Systems.Resource.raw_resource_system as raw_resource, Models.research as research
import Research.research_requirements as research_requirements

def canAffordToResearchBasicToolsI(game_object : g.GameData) -> bool:
    COST_OF_BASIC_TOOLS_I, REQUIRED_IRON_FOR_BASIC_TOOLS_I, REQUIRED_STONE_FOR_BASIC_TOOLS_I = research_requirements.getRequirementsOfBasicToolsI()

    cost_requirements_met = COST_OF_BASIC_TOOLS_I < economy.getCurrencyAmount(game_object)
    iron_requirements_met = REQUIRED_IRON_FOR_BASIC_TOOLS_I < raw_resource.getIronQuantity(game_object)
    stone_requirements_met = REQUIRED_STONE_FOR_BASIC_TOOLS_I < raw_resource.getStoneQuantity(game_object)

    return cost_requirements_met and iron_requirements_met and stone_requirements_met

def addBasicToolsIToResearch(game_object : g.GameData):

    if canAffordToResearchBasicToolsI(game_object):
        game_object.research_in_progress.append(research.Research(game_object.base_research_time, 'BASICTOOLSI'))

def updateAllResearchInQueue(game_object : g.GameData):
    for research_instance in game_object.research_in_progress:
        if research_instance.getTime() < 1:
            executeResearchEffect(research_instance.getResearchType())
            game_object.research_in_progress.remove(research_instance)
        elif research_instance.getTime() > 0:
            research_instance.subtractTime(1)

def completeBasicToolsI(game_object : g.GameData):
    for province in game_object.provinces:
        province.updateConstructionBoost(3)

def completeBasicToolsII(game_object : g.GameData):
    for province in game_object.provinces:
        province.updateConstructionBoost(5)

def executeResearchEffect(game_object : g.GameData, research_type : str) -> None:
    research_and_effects = {'BASICTOOLSI':completeBasicToolsI, 'BASICTOOLSII':completeBasicToolsII}

    match research_type:
        case "BASICTOOLSI":
            research_and_effects['BASICTOOLSI'](game_object)
        case "BASICTOOLSII":
            research_and_effects['BASICTOOLSII'](game_object)

