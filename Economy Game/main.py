'''
Preface: This file is the main game file, consisting of the main game loop. 

Author: TheEmojiNinja
'''

# Import required modules
import Systems.province_system as p,  Systems.resource_system as r, Systems.economy_system as e,  Systems.time_system as t, Data.game_data as g
import UI.main_menu as mm, UI.construction_menu as cm, UI.laws_menu as lm, UI.province_menu as pm
import time

# Key variables
running = True

game = g.GameData()

# Randomize game starting values
r.randomizeCoalQuantity(game)
r.randomizeStoneQuantity(game)
r.randomizeIronQuantity(game)
e.randomizeCurrencyAmount(game)

# Call the createProvinces method to generate unique provinces
p.createProvinces(game)

# Main game loop
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
                #lm.lawsAndManagementMenu(game)
                print("Sorry! This feature has not been implemented yet! ☹️")
            case '':
                t.updateDay(game)
            case _:
                print("That is not a valid input! ☹️")
                continue
        break



