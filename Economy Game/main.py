'''
Preface: This file is the main game file, consisting of the main game loop. 

Author: TheEmojiNinja
'''

# Import required modules
import Systems.province_system as p,  Systems.resource_system as r, Systems.economy_system as e,  Systems.time_system as t, Data.game_data as g
import UI.GUI.game_gui_interface as gui

# Key variables
running = True

game = g.GameData()

# Randomize game starting values
r.randomizeCoalQuantity(game)
r.randomizeStoneQuantity(game)
r.randomizeIronQuantity(game)
e.randomizeCurrencyAmount(game)
e.randomizeDebtAmount(game)

# Call the createProvinces method to generate unique provinces
p.createProvinces(game)

# Main game loop
gui.mainGameLoop(game)




