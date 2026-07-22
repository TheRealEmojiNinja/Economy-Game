import Data.game_data as g, Systems.economy_system as economy, Systems.Resource.raw_resource_system as raw_resource, Systems.Resource.refined_resource_system as refined_resource, Models.research as research
import Research.research_requirements as research_requirements

RESEARCH = {'Basic Tools I':research.Research('Basic Tools I', 'BASICTOOLSI', 30, 
                {'Cost':400, 'Stone':200, 'Iron':0, 'Coal':0, 'Timber':0, 'Copper':0, 'Steel':0, 'Fuel':0, 'Wood':100}, 
                {'Construction_Boost':3}),
            'Basic Tools II':research.Research('Basic Tools I', 'BASICTOOLSI', 30, 
                {'Cost':600, 'Stone':300, 'Iron':50, 'Coal':0, 'Timber':0, 'Copper':0, 'Steel':0, 'Fuel':0, 'Wood':200}, 
                {'Construction_Boost':3}),
            'Basic Tools III':research.Research('Basic Tools I', 'BASICTOOLSI', 30, 
                {'Cost':1000, 'Stone':600, 'Iron':150, 'Coal':0, 'Timber':0, 'Copper':0, 'Steel':0, 'Fuel':0, 'Wood':300}, 
                {'Construction_Boost':3}),
            'Basic Tools IV':research.Research('Basic Tools I', 'BASICTOOLSI', 30, 
                {'Cost':2000, 'Stone':1200, 'Iron':400, 'Coal':0, 'Timber':0, 'Copper':0, 'Steel':0, 'Fuel':0, 'Wood':500}, 
                {'Construction_Boost':3})
                }

def canAffordToResearch(game_object : g.GameData, research_object : research.Research):
    research_requirements = research_object.getResearchRequirements()
    cost_requirements_met = research_requirements['Cost'] <= economy.getCurrencyAmount(game_object)
    stone_requirements_met = research_requirements['Stone'] <= raw_resource.getStoneQuantity(game_object)
    iron_requirements_met = research_requirements['Iron'] <= raw_resource.getIronQuantity(game_object)
    coal_requirements_met = research_requirements['Coal'] <= raw_resource.getCoalQuantity(game_object)
    timber_requirements_met = research_requirements['Timber'] <= raw_resource.getTimberQuantity(game_object)
    copper_requirements_met = research_requirements['Copper'] <= raw_resource.getCopperQuantity(game_object)
    steel_requirements_met = research_requirements['Steel'] <= refined_resource.getSteelQuantity(game_object)
    fuel_requirements_met = research_requirements['Fuel'] <= refined_resource.getFuelQuantity(game_object)
    wood_requirements_met = research_requirements['Wood'] <= refined_resource.getWoodQuantity(game_object)
    
    return cost_requirements_met and stone_requirements_met and iron_requirements_met and coal_requirements_met and timber_requirements_met and copper_requirements_met and steel_requirements_met and fuel_requirements_met and wood_requirements_met

def addToResearch(game_object : g.GameData, research_object : research.Research):

    if canAffordToResearch(game_object, research_object):
        game_object.research_in_progress.append(research_object)

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
    RESEARCH = {'BASICTOOLSI':research.Research('Basic Tools I', 'BASICTOOLSI', 30, {'Cost':0, 'Stone':0, 'Iron':0}, {'Construction_Boost':3}),}

    match research_type:
        case "BASICTOOLSI":
            research_and_effects['BASICTOOLSI'](game_object)
        case "BASICTOOLSII":
            research_and_effects['BASICTOOLSII'](game_object)

def updateResearchRequirements()

