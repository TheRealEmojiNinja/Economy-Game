import Data.game_data as g, Models.factory as f, Models.mine as m, Systems.economy_system as e, Systems.province_system as p

def constructMenu(game_object : g.GameData):
    province_list = game_object.provinces
    constructing = True

    while constructing: 
        print("────────────────────────────────────────────────────────────────────────────────")
        print("\t\t\t\t———CONSTRUCTION———")
        print("\n\t\t-👉 (1)Build Factories-")
        print("\t\t-👉 (2)Build Mines-")
        print("\t\t-👉 (3)Build Infrastructure-")
        print("\n\t\t\t-Press Enter to Go Back-")
        print("────────────────────────────────────────────────────────────────────────────────")

        while True:
            user_response = input("(👆)> ")
            match (user_response):
                case '1':
                    factoriesMenu(game_object)
                case '2':
                    minesMenu(game_object)
                case '3':
                    print(3)
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

def factoriesMenu(game_object : g.GameData):
    province_list = game_object.provinces
    on_menu = True

    while on_menu: 
        province_names = p.getProvinceNames(game_object)
        print("────────────────────────────────────────────────────────────────────────────────")
        print("\t\t\t\t———FACTORIES———\n")
        print("Type the (case-insensitive) name of the specific province \nyou want to build factories in: ")
        print("\n\t\t\t-Press Enter to Go Back-")
        for province in province_list:
            print(province.getName(), end=' ')
        print("\n────────────────────────────────────────────────────────────────────────────────")

        while True:
            user_response = input("(👆)> ").title()
            if (user_response in province_names):
                province_index = province_names.index(user_response)
                buildFactories(game_object, province_index)
                break
            elif (user_response == ''):
                on_menu = False
                break
            else:
                print("That is not a valid input! ☹️")            

def buildFactories(game_object : g.GameData, index : int):
    print("────────────────────────────────────────────────────────────────────────────────")
    print("\t\t\t\t———FACTORIES———\n")
    print("Enter the number of factories you want to build: \n")
    print("\t\t\t-Press Enter to Go Back-")
    print("Currency: " + str(e.getCurrencyAmount(game_object)))
    print("────────────────────────────────────────────────────────────────────────────────")

    while True:
        user_response = input("(🔢)> ")
        if (user_response == ''):
            break
        try:
            user_response = int(user_response)
            cost = user_response*150
            if (cost <= e.getCurrencyAmount(game_object)):
                game_object.factories_being_constructed.append(f.Factory(5, index, user_response))
                e.subtractCostFromCurrency(game_object, cost)
                print("Purchase successful! " + str(user_response) + " factories are now currently being constructed for " + str(cost) + " currency! You now have " + str(e.getCurrencyAmount(game_object)) + " currency.")
            else:
                print("You unfortunately cannot afford " + str(user_response) + " factories for " + str(cost) + " currency!")
        except ValueError:
            print("That is not a valid input! ☹️")

def minesMenu(game_object : g.GameData):
    province_list = game_object.provinces
    on_menu = True

    while on_menu: 
        province_names = p.getProvinceNames(game_object)
        print("────────────────────────────────────────────────────────────────────────────────")
        print("\t\t\t\t———MINES———\n")
        print("Type the (case-insensitive) name of the specific province \nyou want to build factories in: ")
        print("\n\t\t\t-Press Enter to Go Back-")
        for province in province_list:
            print(province.getName(), end=' ')
        print("\n────────────────────────────────────────────────────────────────────────────────")

        while True:
            user_response = input("(👆)> ").title()
            if (user_response in province_names):
                province_index = province_names.index(user_response)
                buildMines(game_object, province_index)
                break
            elif (user_response == ''):
                on_menu = False
                break
            else:
                print("That is not a valid input! ☹️")          

def buildMines(game_object : g.GameData, index : int):
    print("────────────────────────────────────────────────────────────────────────────────")
    print("\t\t\t\t———MINES———\n")
    print("Enter the number of mines you want to build: \n")
    print("\t\t\t-Press Enter to Go Back-")
    print("Currency: " + str(e.getCurrencyAmount(game_object)))
    print("────────────────────────────────────────────────────────────────────────────────")

    while True:
        user_response = input("(🔢)> ")
        if (user_response == ''):
            break
        try:
            user_response = int(user_response)
            cost = user_response*150
            if (cost <= e.getCurrencyAmount(game_object)):
                game_object.mines_being_constructed.append(m.Mine(5, index, user_response))
                e.subtractCostFromCurrency(game_object, cost)
                print("Purchase successful! " + str(user_response) + " mines are now currently being constructed for " + str(cost) + " currency! You now have " + str(e.getCurrencyAmount(game_object)) + " currency.")
            else:
                print("You unfortunately cannot afford " + str(user_response) + " mines for " + str(cost) + " currency!")
        except ValueError:
            print("That is not a valid input! ☹️")  
