'''
Preface: This file includes the UI function for the main game screen.

Author: TheEmojiNinja
'''

# Import required modules
import Data.game_data as g, Systems.resource_system as r, Systems.economy_system as e

# The function that displays the main game console
def mainGameScreen(game_object : g.GameData):
    print("────────────────────────────────────────────────────────────────────────────────")
    print(f"\t\t\t\t———Day {game_object.day} (v.1.0.2)———\n")
    print("\t\t\t  ———Total Resources———")
    print(f"\t🪨  (Coal): {r.getCoalQuantity(game_object)} \t🪨  (Iron): {r.getIronQuantity(game_object)} \t🪨  (Stone): {r.getStoneQuantity(game_object)}")
    print(f"\t\t\t💰 (Economic Budget): {e.getCurrencyAmount(game_object)}")
    print("\n\t\t-👉 (1)View Provinces-")
    print("\t\t-👉 (2)Construct-")
    print("\t\t-👉 (3)Laws/Management-")
    print("\t\t-👉 (ENTER)Continue to Next Day-")
    print("────────────────────────────────────────────────────────────────────────────────")
