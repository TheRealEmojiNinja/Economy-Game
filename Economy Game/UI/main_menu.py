import Data.game_data as g, Systems.resource_system as r, Systems.economy_system as e

# The function that displays the main game console
def mainGameScreen(game_object : g.GameData):
    print("────────────────────────────────────────────────────────────────────────────────")
    print("\t\t\t\t———Day " + str(game_object.day) + "———\n")
    print("\t\t\t  ———Total Resources———")
    print("\t🪨  (Coal): " + str(r.getCoalQuantity(game_object)) + " \t🪨  (Iron): " + str(r.getIronQuantity(game_object)) + " \t🪨  (Stone): " + str(r.getStoneQuantity(game_object)))
    print("\t\t\t💰 (Economic Budget): " + str(e.getCurrencyAmount(game_object)))
    print("\n\t\t-👉 (1)View Provinces-")
    print("\t\t-👉 (2)Construct-")
    print("\t\t-👉 (3)Laws/Management-")
    print("\t\t-👉 (4)Continue to Next Day-")
    print("────────────────────────────────────────────────────────────────────────────────")
