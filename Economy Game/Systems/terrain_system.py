'''
Preface: This file includes functions that relate to terrain generation which affect the max amounts of certain buildings.

Author: TheEmojiNinja
'''

# Import required modules
import random

# This method returns a random terrain type
def randomizeTerrainType() -> str:
    terrain_types = ["Urban", "Mountainous", "Forested", "Plains"]
    return random.choice(terrain_types)

# This method defines the max factory count depending on the terrain
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

# This method defines the max mine count depending on the terrain
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

# This method defines the max sawmill count depending on the terrain
def maxSawmillCount(terrain_type : str) -> int:
    match terrain_type:
        case "Urban":
            return 2
        case "Mountainous":
            return 10
        case "Forested":
            return 20
        case "Plains":
            return 5
        
# This method defines the max infrastructure count depending on the terrain
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