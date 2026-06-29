import Data.game_data as g, Models.province as p


# Very Low -> 1, Low -> 2, Average -> 3, High -> 4, Very High -> 5
def setBaseTaxLevel(game_object : g.GameData) -> None:
    game_object.tax_level = 3

def updateTaxLevel(game_object : g.GameData, new_tax_level : int) -> None:
    if new_tax_level in [1, 2, 3, 4, 5]:
        game_object.tax_level = new_tax_level
    else:
        return None
    
def getTaxLevel(game_object : g.GameData) -> str:
    match game_object.tax_level:
        case 1:
            return "Very Low"
        case 2:
            return "Low"
        case 3:
            return "Average"
        case 4:
            return "High"
        case 5:
            return "Very High"

def updateMaximumProductionStatus(province : p.Province, new_status : bool) -> None:
    if new_status != province.getMaximumProductionStatus():
        province.updateMaximumProductionStatus(new_status)
    else:
        return None
