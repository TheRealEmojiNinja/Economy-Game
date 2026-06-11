'''
Preface: This file consists of the UI function for the provinces screen.

Author: TheEmojiNinja
'''
# Import required modules
import Data.game_data as g

# The function that displays the list of provinces and their attributes
def provincesMenu(game_object : g.GameData):
    province_list = game_object.provinces
    print("────────────────────────────────────────────────────────────────────────────────")
    print("\t\t\t\t———PROVINCES———\n")
    for province in province_list:
        print(province.printStats() + "\n")
    print("\t\t\t-Press ENTER to Go Back-")
    print("────────────────────────────────────────────────────────────────────────────────")

    while True:
        user_response = input("(🫲 )> ")
        if (user_response == ''):
            break
        else:
            print("Press \"Enter\" to exit! 😊")