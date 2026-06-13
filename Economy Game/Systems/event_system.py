import Data.game_data as g, random

def generateRandomEvent(game_object : g.GameData) -> str:
    return random.choices(game_object.EVENTS, game_object.EVENT_WEIGHTS, k=1)[0]

def executeEvent(game_object : g.GameData, event : str) -> None:
    match event:
        case "Mine Collapse":
            province = random.choice(game_object.provinces)
            if province.getMines() > 0:
                province.updateMines(-1)
                print(f"Oh no! A mine has collapsed in {province.getName()}!")