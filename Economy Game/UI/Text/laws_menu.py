'''
Preface: This file consists of the UI function for the laws and management menu, which is not yet implemented.

Author: TheEmojiNinja
'''

import Data.game_data as g, Systems.law_system as l, Systems.province_system as p
# The function that displays the laws and management menu, which is not yet implemented
def lawsAndManagementMenu(game_object : g.GameData):

    managing = True

    while managing:
        print("────────────────────────────────────────────────────────────────────────────────")
        print("\t\t\t\t———LAWS & MANAGEMENT———")
        print("\n\t\t-👉 (1)Manage Taxes-")
        print("\t\t-👉 (2)Manage Production-")
        print("\n\t\t\t-Press ENTER to Go Back-")
        print("────────────────────────────────────────────────────────────────────────────────")

        while True:
            user_response = input("(👆)> ")
            match (user_response):
                case '1':
                    taxesMenu(game_object)
                case '2':
                    productionMenu(game_object)
                case '':
                    managing = False
                    break
                case _:
                    print("That is not a valid input! ☹️")
                    continue
        
            break

def taxesMenu(game_object : g.GameData):

    managing = True

    while managing:
        print("────────────────────────────────────────────────────────────────────────────────")
        print("\t\t\t\t———TAXES———")
        print("\n\t\tSet a tax level:")
        print("\n\t\t-👉 (1)Very Low-")
        print("\t\t-👉 (2)Low-")
        print("\t\t-👉 (3)Average-")
        print("\t\t-👉 (4)High-")
        print("\t\t-👉 (5)Very High-")
        print(f"\n\t\tCurrent Tax Level: {l.getTaxLevel(game_object)}")
        print("\n\t\t\t-Press ENTER to Go Back-")
        print("────────────────────────────────────────────────────────────────────────────────")

        while True:
                user_response = input("(👆)> ")
                match (user_response):
                    case '1':
                        l.updateTaxLevel(game_object, 1)
                        print("Tax level is now very low!")
                    case '2':
                        l.updateTaxLevel(game_object, 2)
                        print("Tax level is now low!")
                    case '3':
                        l.updateTaxLevel(game_object, 3)
                        print("Tax level is now average!")
                    case '4':
                        l.updateTaxLevel(game_object, 4)
                        print("Tax level is now high!")
                    case '5':
                        l.updateTaxLevel(game_object, 5)   
                        print("Tax level is now very high!")
                    case '':
                        break
                    case _:
                        print("That is not a valid input! ☹️")
                        continue
            
                break
    
def productionMenu(game_object : g.GameData):

    managing = True

    province_list = game_object.provinces

    while managing:
        province_names = p.getProvinceNames(game_object)
        print("────────────────────────────────────────────────────────────────────────────────")
        print("\t\t\t\t———PRODUCTION———")
        print("\n\t\tList all the provinces (case-insensitive) you wish to change to or from maximum production (separated by space):")
        for province in province_list:
            print(province.getName(), end=' ')
        print("\n\t\t\t-Press ENTER to Go Back-")
        print("────────────────────────────────────────────────────────────────────────────────")

        while True:
            user_response = input("(👆)> ")
            if user_response == '':
                managing = False
                break
            elif user_response:
                provinces = user_response.split(' ')
                for province in provinces:
                    if province in province_names:
                        pass
            match (user_response):
                case '1':
                    taxesMenu(game_object)
                case '2':
                    productionMenu(game_object)
                case '':
                    managing = False
                    break
                case _:
                    print("That is not a valid input! ☹️")
                    continue
        
            break
