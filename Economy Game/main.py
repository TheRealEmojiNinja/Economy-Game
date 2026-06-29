'''
Preface: This file is the main game file, consisting of the main game loop. 

Author: TheEmojiNinja
'''

# Import required modules
import Systems.province_system as p,  Systems.resource_system as r, Systems.economy_system as e,  Systems.time_system as t, Data.game_data as g
import UI.Text.main_menu as mm, UI.Text.construction_menu as cm, UI.Text.laws_menu as lm, UI.Text.province_menu as pm
import time
import UI.GUI.test as test

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

testingGUI = True

# Main game loop
if not testingGUI:
    while running:
        mm.mainGameScreen(game)
        while True:
            response = input("(👆)> ")
            match response:
                case '1':
                    pm.provincesMenu(game)
                case '2':
                    cm.constructMenu(game)
                case '3':
                    lm.lawsAndManagementMenu(game)
                case '':
                    t.updateDay(game)
                case _:
                    print("That is not a valid input! ☹️")
                    continue
            break
else:
    test.mainGameLoop(game)




