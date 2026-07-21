'''
Preface: This file is the main game file, consisting of the main game loop. 

Author: TheEmojiNinja
'''

# Import required modules
import Systems.province_system as p,  Systems.Resource.raw_resource_system as raw_resource, Systems.Resource.refined_resource_system as refined_resource, Systems.economy_system as economy,  Systems.time_system as time, Data.game_data as g
import UI.GUI.game_gui_interface as gui

# Key variables
running = True

game = g.GameData()

# Randomize game starting values
raw_resource.randomizeCoalQuantity(game)
raw_resource.randomizeStoneQuantity(game)
raw_resource.randomizeIronQuantity(game)
raw_resource.randomizeTimberQuantity(game)
raw_resource.randomizeCopperQuantity(game)
refined_resource.randomizeSteelQuantity(game)
refined_resource.randomizeFuelQuantity(game)
refined_resource.randomizeWoodQuantity(game)
economy.randomizeCurrencyAmount(game)
economy.randomizeDebtAmount(game)

# Call the createProvinces method to generate unique provinces
p.createProvinces(game)

# Main game loop
gui.mainGameLoop(game)




