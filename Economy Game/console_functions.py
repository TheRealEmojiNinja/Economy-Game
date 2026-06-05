'''
Preface: This file contains the bulk of all the code that makes the Economy Game prgram run. Due to the nature of this file and the 
rather long, complicated sections of code, further docstrings will be used to differentiate and organize the code.

Author: TheEmojiNinja
'''

import province as p, major_functions as f, variable_management as vm
from key_variables import coal, iron, stone, day
from factory import Factory
from mine import Mine
from typing import List

factories_being_constructed: List[Factory] = []
mines_being_constructed: List[Mine] = []


'''
The 
'''

# The function that displays the main game console
def mainGameScreen():
    global coal, iron, stone, day
    print("────────────────────────────────────────────────────────────────────────────────")
    print("\t\t\t\t———Day " + str(day) + "———\n")
    print("\t\t\t  ———Total Resources———")
    print("\t🪨  (Coal): " + str(vm.getCoalQuantity()) + " \t🪨  (Iron): " + str(vm.getIronQuantity()) + " \t🪨  (Stone): " + str(vm.getStoneQuantity()))
    print("\t\t\t💰 (Economic Budget): " + str(vm.getCurrencyAmount()))
    print("\n\t\t-👉 (1)View Provinces-")
    print("\t\t-👉 (2)Construct-")
    print("\t\t-👉 (3)Laws/Management-")
    print("\t\t-👉 (4)Continue to Next Day-")
    print("────────────────────────────────────────────────────────────────────────────────")

# The function that displays the list of provinces and their attributes
def provincesMenu(province_list : list[p.Province]):
    print("────────────────────────────────────────────────────────────────────────────────")
    print("\t\t\t\t———PROVINCES———\n")
    for province in province_list:
        print(province.printStats() + "\n")
    print("\t\t\t-Press Enter to Go Back-")
    print("────────────────────────────────────────────────────────────────────────────────")

    while True:
        user_response = input("(🫲 )> ")
        if (user_response == ''):
            break
        else:
            print("Press \"Enter\" to exit! 😊")


def constructMenu(province_list : list[p.Province]):
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
                    factoriesMenu(province_list)
                case '2':
                    minesMenu(province_list)
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

def factoriesMenu(province_list : list[p.Province]):
    on_menu = True

    while on_menu: 
        province_names = f.getProvinceNames(province_list)
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
                buildFactories(province_index)
                break
            elif (user_response == ''):
                on_menu = False
                break
            else:
                print("That is not a valid input! ☹️")            

def buildFactories(index):
    print("────────────────────────────────────────────────────────────────────────────────")
    print("\t\t\t\t———FACTORIES———\n")
    print("Enter the number of factories you want to build: \n")
    print("\t\t\t-Press Enter to Go Back-")
    print("Currency: " + str(vm.getCurrencyAmount()))
    print("────────────────────────────────────────────────────────────────────────────────")

    while True:
        user_response = input("(🔢)> ")
        if (user_response == ''):
            break
        try:
            user_response = int(user_response)
            cost = user_response*150
            if (cost <= vm.getCurrencyAmount()):
                factories_being_constructed.append(Factory(5, index, user_response))
                vm.subtractCostFromCurrency(cost)
                print("Purchase successful! " + str(user_response) + " factories are now currently being constructed for " + str(cost) + " currency! You now have " + str(vm.getCurrencyAmount()) + " currency.")
            else:
                print("You unfortunately cannot afford " + str(user_response) + " factories for " + str(cost) + " currency!")
        except ValueError:
            print("That is not a valid input! ☹️")

def minesMenu(province_list : list[p.Province]):
    on_menu = True

    while on_menu: 
        province_names = f.getProvinceNames(province_list)
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
                buildFactories(province_index)
                break
            elif (user_response == ''):
                on_menu = False
                break
            else:
                print("That is not a valid input! ☹️")          

def buildMines(index):
    print("────────────────────────────────────────────────────────────────────────────────")
    print("\t\t\t\t———MINES———\n")
    print("Enter the number of mines you want to build: \n")
    print("\t\t\t-Press Enter to Go Back-")
    print("Currency: " + str(vm.getCurrencyAmount()))
    print("────────────────────────────────────────────────────────────────────────────────")

    while True:
        user_response = input("(🔢)> ")
        if (user_response == ''):
            break
        try:
            user_response = int(user_response)
            cost = user_response*150
            if (cost <= vm.getCurrencyAmount()):
                mines_being_constructed.append(Mine(5, index, user_response))
                vm.subtractCostFromCurrency(cost)
                print("Purchase successful! " + str(user_response) + " mines are now currently being constructed for " + str(cost) + " currency! You now have " + str(vm.getCurrencyAmount()) + " currency.")
            else:
                print("You unfortunately cannot afford " + str(user_response) + " mines for " + str(cost) + " currency!")
        except ValueError:
            print("That is not a valid input! ☹️")  

def updateFactoriesInConstruction(province_list : list[p.Province]):
    for factory_instance in factories_being_constructed:
        if factory_instance.getTime() < 1:
            province = province_list[factory_instance.getIndex()]
            province.addFactories(factory_instance.getNumberOfFactories())
            factories_being_constructed.remove(factory_instance)
        elif factory_instance.getTime() > 0:
            factory_instance.subtractTime(1)

def getTotalFactoryOutput(province_list):
    total = 0
    province_list : list[p.Province] = province_list    
    for province in province_list:
        total += province.getFactories()
    return 

def updateMinesInConstruction(province_list : list[p.Province]):
    for mine_instance in mines_being_constructed:
        if mine_instance.getTime() < 1:
            province = province_list[mine_instance.getIndex()]
            province.addMines(mine_instance.getNumberOfMines())
            mines_being_constructed.remove(mine_instance)
        elif mine_instance.getTime() > 0:
            mine_instance.subtractTime(1)

def getTotalMiningOutput(province_list):
    total = 0
    province_list : list[p.Province] = province_list    
    for province in province_list:
        total += province.getMines()
    return total

def updateDay(province_list):
    global day
    updateFactoriesInConstruction(province_list)
    vm.addProfitToCurrency(getTotalFactoryOutput(province_list)*10)
    updateMinesInConstruction(province_list)
    
    day += 1
    
def lawsAndManagementMenu(province_list):

    managing = True

    while managing:
        print("────────────────────────────────────────────────────────────────────────────────")
        print("\t\t\t\t———LAWS & MANAGEMENT———")
        print("\n\t\t-👉 (1)Rename Province-")
        print("\t\t-👉 (2)Manage Work Week-")
        print("\n\t\t\t-Press Enter to Go Back-")
        print("────────────────────────────────────────────────────────────────────────────────")
