import random

def randomizeTerrainType() -> str:
    terrain_types = ["Urban", "Mountainous", "Forested", "Plains"]
    return random.choice(terrain_types)

def maxFactoryCount(terrain_type : str) -> int:
    match terrain_type:
        case "Urban":
            return 20
        case "Mountainous":
            return 5
        case "Forested":
            return 10
        case "Plains":
            return 15
        
def maxMineCount(terrain_type : str) -> int:
    match terrain_type:
        case "Urban":
            return 5
        case "Mountainous":
            return 20
        case "Forested":
            return 10
        case "Plains":
            return 15
        
def maxInfrastructureCount(terrain_type : str) -> int:
    match terrain_type:
        case "Urban":
            return 5
        case "Mountainous":
            return 5
        case "Forested":
            return 10
        case "Plains":
            return 5