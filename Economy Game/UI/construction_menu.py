'''
Preface: This file consists of UI functions for the construction menu.

Author: TheEmojiNinja
'''

# Import required modules
import Data.game_data as g, Models.factory as f, Models.mine as m, Systems.economy_system as e, Systems.province_system as p, Systems.resource_system as r, Systems.development_systems as d

# The function that lists the construction menu
def constructMenu(game_object : g.GameData):
    province_list = game_object.provinces
    constructing = True

    while constructing: 
        print("────────────────────────────────────────────────────────────────────────────────")
        print("\t\t\t\t———CONSTRUCTION———")
        print("\n\t\t-👉 (1)Build Factories-")
        print("\t\t-👉 (2)Build Mines-")
        print("\t\t-👉 (3)Build Infrastructure-")
        print("\n\t\t\t-Press ENTER to Go Back-")
        print("────────────────────────────────────────────────────────────────────────────────")

        while True:
            user_response = input("(👆)> ")
            match (user_response):
                case '1':
                    factoriesMenu(game_object)
                case '2':
                    minesMenu(game_object)
                case '3':
                    print("Sorry! This feature has not been implemented yet! ☹️")
                case '':
                    constructing = False
                    break
                case _:
                    print("That is not a valid input! ☹️")
                    continue
        
            break

'''
The code contained under this docstring manages everything related to the development of factories.
'''

# The function that lists the factories menu and asks the user to choose what province to add factories to
def factoriesMenu(game_object : g.GameData):
    province_list = game_object.provinces
    on_menu = True

    while on_menu: 
        province_names = p.getProvinceNames(game_object)
        print("────────────────────────────────────────────────────────────────────────────────")
        print("\t\t\t\t———FACTORIES———\n")
        print("Type the (case-insensitive) name of the specific province \nyou want to build factories in: ")
        for province in province_list:
            print(province.getName(), end=' ')
        print("\n\n\t\t\t-Press ENTER to Go Back-")
        print("────────────────────────────────────────────────────────────────────────────────")

        while True:
            user_response = input("(👆)> ").title().strip()
            if (user_response in province_names):
                province_index = province_names.index(user_response)
                buildFactories(game_object, province_index)
                break
            elif (user_response == ''):
                on_menu = False
                break
            else:
                print("That is not a valid input! ☹️")            

# A continuation of the factories menu that allows the player to buy a number of factories
def buildFactories(game_object : g.GameData, index : int):
    print("────────────────────────────────────────────────────────────────────────────────")
    print("\t\t\t\t———FACTORIES———\n")
    print("Enter the number of factories you want to build (costs x currency and y iron): \n")
    print("Currency: " + str(e.getCurrencyAmount(game_object)) + " Iron: " + str(r.getIronQuantity(game_object)))
    print("\n\t\t\t-Press ENTER to Go Back-")
    print("────────────────────────────────────────────────────────────────────────────────")

    while True:
        user_response = input("(🔢)> ")
        if (user_response == ''):
            break
        try:
            user_response = int(user_response)
            result, total_cost, total_iron = d.addFactoriesToQueue(game_object, user_response, index)
            if result:
                print("Purchase successful! " + str(user_response) + " factories are now currently being constructed for " + str(total_cost) + " currency and " + str(total_iron) + " iron! You now have " + str(e.getCurrencyAmount(game_object)) + " currency and " + str(r.getIronQuantity(game_object)) + " iron.")
            else:
                print("You unfortunately cannot afford " + str(user_response) + " factories for " + str(total_cost) + " currency and " + str(total_iron) + " iron.")
        except ValueError:
            print("That is not a valid input! ☹️")

'''
The code contained under this docstring manages everything related to the development of mines.
'''

# The function that lists the mines menu and asks the user to choose what province to add mines to
def minesMenu(game_object : g.GameData):
    province_list = game_object.provinces
    on_menu = True

    while on_menu: 
        province_names = p.getProvinceNames(game_object)
        print("────────────────────────────────────────────────────────────────────────────────")
        print("\t\t\t\t———MINES———\n")
        print("Type the (case-insensitive) name of the specific province \nyou want to build mines in: ")
        for province in province_list:
            print(province.getName(), end=' ')
        print("\n\n\t\t\t-Press ENTER to Go Back-")
        print("────────────────────────────────────────────────────────────────────────────────")

        while True:
            user_response = input("(👆)> ").title().strip()
            if (user_response in province_names):
                province_index = province_names.index(user_response)
                buildMines(game_object, province_index)
                break
            elif (user_response == ''):
                on_menu = False
                break
            else:
                print("That is not a valid input! ☹️")          

# A continuation of the mines menu that allows the player to buy a number of mines
def buildMines(game_object : g.GameData, index : int):
    print("────────────────────────────────────────────────────────────────────────────────")
    print("\t\t\t\t———MINES———\n")
    print("Enter the number of mines you want to build (costs x currency and y stone): \n")
    print("Currency: " + str(e.getCurrencyAmount(game_object)) + " Stone: " + str(r.getStoneQuantity(game_object)))
    print("\n\t\t\t-Press ENTER to Go Back-")
    print("────────────────────────────────────────────────────────────────────────────────")

    while True:
        user_response = input("(🔢)> ")
        if (user_response == ''):
            break
        try:
            user_response = int(user_response)
            result, total_cost, total_stone = d.addMinesToQueue(game_object, user_response, index)
            if result:
                print("Purchase successful! " + str(user_response) + " mines are now currently being constructed for " + str(total_cost) + " currency and " + str(total_stone) + " stone! You now have " + str(e.getCurrencyAmount(game_object)) + " currency and " + str(r.getStoneQuantity(game_object)) + " stone.")
            else:
                print("You unfortunately cannot afford " + str(user_response) + " mines for " + str(total_cost) + " currency and " + str(total_stone) + " stone!")
        except ValueError:
            print("That is not a valid input! ☹️")  
