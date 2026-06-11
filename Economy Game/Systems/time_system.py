import Systems.economy_system as e, Systems.development_systems as d, Data.game_data as g

def updateDay(game_object : g.GameData):
    d.updateFactoriesInConstruction(game_object)
    profit = d.getTotalFactoryOutput(game_object)*10
    e.addProfitToCurrency(game_object, profit)
    d.updateMinesInConstruction(game_object)
    
    game_object.day += 1