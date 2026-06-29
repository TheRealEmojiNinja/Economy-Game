'''
Preface: This file contains all events that correlate to politcs, domestic and international.

Author: TheEmojiNinja
'''

# Import required modules
import random, Data.game_data as g, Models.province as p

def doGlobalTensionEvent(game_object : g.GameData) -> None:
    print(random.choice(game_object.EVENT_DESCRIPTIONS["Global_Tension"]))

def doFestivalEvent(game_object : g.GameData, province : p.Province) -> None:
    print(random.choice(game_object.EVENT_DESCRIPTIONS["Festival"]).format(province=province.getName()))
    # In the future this will boost satisfaction