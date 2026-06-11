# Economy Game consists of two major goals:
#       1) Improve the economy
#       2) Maintain said economy

# You will have a certain number of provinces, each with their own:
#       - Generated amount of factories
#       - Unique resource deposits
#       - Level of infrastructure
#       - Generated amount of mines

# Factories will earn money daily, improving the overall economic power
# Mines will mine resources everyday depending on the province's deposits
# Resources and money can be used to construct more factories/mines/infrastructure
# They can also be used in special investment projects
# Infrastructure speeds up construction time
# There will be special events that may impact you in a good or bad way

# The game will have a leader satisfaction rating, that determine how much the people like you
# This rating will be affected by player decisions

# There will be certain laws you can pass, that can effect things such as the rating and daily output (in the form of buffs)

# Coal will be used to power factories
# Iron will be used to construct more factories
# Stone will be used to construct more mines/infrastructure

# If you do not have a certain resource, you will have to import it until you have enough money to invest into excavation projects to find that resource

# The overarching goal is to get your country out of its misery and into economic utopia (a certain amount of money in x amount of time not decided yet)

'''
Preface:

Author: TheEmojiNinja
'''

# Potentially required modules
import Systems.province_system as p,  Systems.resource_system as r, Systems.economy_system as e,  Systems.time_system as t, Data.game_data as g
import UI.main_menu as mm, UI.construction_menu as cm, UI.laws_menu as lm, UI.province_menu as pm
#from key_variables import currency

# Key variables
running = True

game = g.GameData()

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
                pm.provincesMenu(game) # Pass in game object
            case '2':
                cm.constructMenu(game)
            case '3':
                lm.lawsAndManagementMenu(game)
            case '4':
                t.updateDay(game)
            case _:
                print("That is not a valid input! ☹️")
                continue
        break



