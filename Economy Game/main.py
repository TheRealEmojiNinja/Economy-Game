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
import random, math, time, province as p, major_functions as f, console_functions as c, variable_management as vm
#from key_variables import currency

# Key variables
running = True

provinces = []

vm.randomizeCoalQuantity()
vm.randomizeStoneQuantity()
vm.randomizeIronQuantity()
vm.randomizeCurrencyAmount()

# Call the createProvinces method to generate unique provinces
f.createProvinces(provinces)

# Main game loop
while running:
    c.mainGameScreen()
    while True:
        response = input("(👆)> ")
        match response:
            case '1':
                c.provincesMenu(provinces)
            case '2':
                c.constructMenu(provinces)
            case '3':
                c.lawsAndManagementMenu(provinces)
            case '4':
                c.updateDay(provinces)
            case _:
                print("That is not a valid input! ☹️")
                continue
        break



